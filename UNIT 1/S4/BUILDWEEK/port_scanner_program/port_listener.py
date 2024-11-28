
import socket
import threading
import os
import re
import pty
import tkinter as tk

class PortListener:
    def __init__(self, log_func):
        self.listener_socket = None
        self.client_socket = None
        self.listener_thread = None
        self.running = False
        self.shell_pid = None
        self.shell_fd = None
        self.log = log_func

    def start_listener(self, ip_address, port, shell_output, send_button):
        if self.listener_thread and self.listener_thread.is_alive():
            self.log("Listener già avviato.")
            return

        self.listener_thread = threading.Thread(
            target=self.run_listener, args=(ip_address, port, shell_output, send_button), daemon=True
        )
        self.running = True
        self.listener_thread.start()
        self.log(f"Listener avviato su {ip_address}:{port}.")

    def run_listener(self, ip_address, port, shell_output, send_button):
        try:
            self.listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.listener_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.listener_socket.bind((ip_address, port))
            self.listener_socket.listen(1)
            self.log("In attesa di connessioni...")

            self.client_socket, client_address = self.listener_socket.accept()
            self.log(f"Connessione ricevuta da {client_address}.")

            self.shell_pid, self.shell_fd = pty.fork()
            if self.shell_pid == 0:
                os.putenv("PS1", "$ ")
                os.execv("/bin/sh", ["sh"])
            else:
                threading.Thread(target=self.forward_shell_output, args=(shell_output,), daemon=True).start()
                threading.Thread(target=self.receive_messages, daemon=True).start()

        except Exception as e:
            self.log(f"Errore Listener: {e}")

    def stop_listener(self):
        self.running = False
        if self.client_socket:
            self.client_socket.close()
        if self.listener_socket:
            self.listener_socket.close()
        if self.shell_fd:
            os.close(self.shell_fd)
        self.log("Listener fermato.")

    def send_command(self, command_entry, shell_fd):
        command = command_entry.get()
        if command.strip() == "":
            self.log("Comando vuoto. Inserisci un comando valido.")
            return

        try:
            os.write(shell_fd, (command + "\n").encode("utf-8"))
            self.log(f"Comando inviato: {command}")
            command_entry.delete(0, tk.END)
        except Exception as e:
            self.log(f"Errore nell'invio del comando: {e}")

    def forward_shell_output(self, shell_output):
        try:
            ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
            while self.running:
                output = os.read(self.shell_fd, 1024).decode(errors="ignore")
                output = ansi_escape.sub("", output)
                if output:
                    self.client_socket.sendall(output.encode("utf-8", errors="ignore"))
                    shell_output.config(state="normal")
                    shell_output.insert(tk.END, output)
                    shell_output.config(state="disabled")
                    shell_output.yview(tk.END)
        except Exception as e:
            self.log(f"Errore nella lettura dell'output della shell: {e}")

    def receive_messages(self):
        try:
            while self.running:
                message = self.client_socket.recv(1024).decode("utf-8")
                if not message:
                    break
                os.write(self.shell_fd, (message + "\n").encode("utf-8"))
        except Exception as e:
            self.log(f"Errore nella ricezione del messaggio: {e}")
        finally:
            self.client_socket.close()
            self.client_socket = None
            self.log("Connessione chiusa dal client.")
