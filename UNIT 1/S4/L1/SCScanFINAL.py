import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, ttk
from PIL import Image, ImageTk
from queue import Queue
import subprocess
import pty
import os
import re


class SplashScreen(tk.Toplevel):
    def __init__(self, master, logo_path, on_complete):
        super().__init__(master)
        self.master = master
        self.on_complete = on_complete
        self.overrideredirect(True)
        self.geometry("600x400+400+200")
        self.attributes("-alpha", 0.0)
        self.fade_value = 0.0

        logo_image = Image.open(logo_path).resize((400, 300), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(logo_image)

        self.logo_label = tk.Label(self, image=self.logo, bg="#2e3440")
        self.logo_label.pack(expand=True)
        self.after(50, self.fade_in)

    def fade_in(self):
        self.fade_value += 0.05
        if self.fade_value <= 1.0:
            self.attributes("-alpha", self.fade_value)
            self.after(50, self.fade_in)
        else:
            self.after(2000, self.fade_out)

    def fade_out(self):
        self.fade_value -= 0.05
        if self.fade_value >= 0.0:
            self.attributes("-alpha", self.fade_value)
            self.after(50, self.fade_out)
        else:
            self.destroy()
            self.on_complete()


class PortScannerListenerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("PortWatch - Scanner e Listener con Shell")
        self.master.geometry("900x700")

        self.listener_socket = None
        self.client_socket = None
        self.listener_thread = None
        self.running = False
        self.shell_pid = None
        self.shell_fd = None

        self.scanning = False
        self.port_queue = Queue()
        self.results = {}
        self.open_ports = []

        self.create_widgets()

    def create_widgets(self):
        self.scanner_frame = ttk.LabelFrame(self.master, text="Port Scanner")
        self.scanner_frame.pack(fill="x", padx=10, pady=5)

        self.ip_label = ttk.Label(self.scanner_frame, text="Indirizzo IP:")
        self.ip_label.pack(side="left", padx=5)

        self.ip_entry = ttk.Entry(self.scanner_frame, width=30)
        self.ip_entry.insert(0, "localhost")
        self.ip_entry.pack(side="left", padx=5)

        self.scan_button = ttk.Button(self.scanner_frame, text="Avvia Scansione", command=self.start_scan)
        self.scan_button.pack(side="left", padx=5)

        self.stop_scan_button = ttk.Button(self.scanner_frame, text="STOP Scansione", command=self.stop_scan)
        self.stop_scan_button.pack(side="left", padx=5)

        self.result_table = ttk.Treeview(self.master, columns=("Porta", "Stato", "Protocollo"), show="headings")
        self.result_table.heading("Porta", text="Porta")
        self.result_table.heading("Stato", text="Stato")
        self.result_table.heading("Protocollo", text="Protocollo")
        self.result_table.pack(fill="both", expand=True, padx=10, pady=5)

        self.listener_frame = ttk.LabelFrame(self.master, text="Gestione Listener")
        self.listener_frame.pack(fill="x", padx=10, pady=5)

        self.port_label = ttk.Label(self.listener_frame, text="Porta Listener:")
        self.port_label.pack(side="left", padx=5)

        self.port_entry = ttk.Entry(self.listener_frame, width=10)
        self.port_entry.insert(0, "9000")
        self.port_entry.pack(side="left", padx=5)

        self.start_button = ttk.Button(self.listener_frame, text="Avvia Listener", command=self.start_listener)
        self.start_button.pack(side="left", padx=5)

        self.stop_button = ttk.Button(self.listener_frame, text="Ferma Listener", command=self.stop_listener)
        self.stop_button.pack(side="left", padx=5)

        self.shell_frame = ttk.LabelFrame(self.master, text="Shell Interattiva")
        self.shell_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.shell_output = scrolledtext.ScrolledText(self.shell_frame, width=80, height=15, state="disabled")
        self.shell_output.pack(pady=5)

        self.command_entry = ttk.Entry(self.shell_frame, width=80)
        self.command_entry.pack(side="left", padx=5)

        self.send_button = ttk.Button(self.shell_frame, text="Invia", command=self.send_command)
        self.send_button.pack(side="left", padx=5)

        self.log_frame = ttk.LabelFrame(self.master, text="Log")
        self.log_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.log_area = scrolledtext.ScrolledText(self.log_frame, width=80, height=10, state="disabled")
        self.log_area.pack(pady=5)

    def log(self, message):
        self.log_area.config(state="normal")
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.config(state="disabled")
        self.log_area.yview(tk.END)

    def start_scan(self):
        target_ip = self.ip_entry.get()
        self.result_table.delete(*self.result_table.get_children())
        self.open_ports = []
        self.results = {}
        self.scanning = True

        for port in range(1, 1025):
            self.port_queue.put(port)

        threading.Thread(target=self.perform_scan, args=(target_ip,), daemon=True).start()

    def stop_scan(self):
        self.scanning = False
        self.log("Scansione fermata.")

    def perform_scan(self, target_ip):
        threads = []
        for _ in range(100):
            thread = threading.Thread(target=self.scan_worker, args=(target_ip,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        self.log("Scansione completata.")

    def scan_worker(self, target_ip):
        while not self.port_queue.empty() and self.scanning:
            port = self.port_queue.get()
            self.scan_port(target_ip, port, protocol="TCP")
            self.scan_port(target_ip, port, protocol="UDP")

    def scan_port(self, target_ip, port, protocol):
        try:
            if protocol == "TCP":
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.1)
                    result = s.connect_ex((target_ip, port))
                    if result == 0:
                        self.add_result(port, "OPEN", protocol)
            elif protocol == "UDP":
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.settimeout(0.1)
                    s.sendto(b"", (target_ip, port))
                    try:
                        s.recvfrom(1024)
                        self.add_result(port, "OPEN", protocol)
                    except socket.timeout:
                        pass
        except Exception:
            pass

    def add_result(self, port, state, protocol):
        if port not in self.results:
            self.results[port] = {"stato": state, "protocollo": protocol}
            self.result_table.insert("", "end", values=(port, state, protocol))
            if state == "OPEN":
                self.open_ports.append(port)

    def start_listener(self):
        if self.listener_thread and self.listener_thread.is_alive():
            self.log("Listener già avviato.")
            return

        port = int(self.port_entry.get())
        self.listener_thread = threading.Thread(target=self.run_listener, args=(port,), daemon=True)
        self.running = True
        self.listener_thread.start()
        self.log(f"Listener avviato sulla porta {port}.")

    def run_listener(self, port):
        try:
            self.listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.listener_socket.bind(("0.0.0.0", port))
            self.listener_socket.listen(1)
            self.log("In attesa di connessioni...")

            self.client_socket, client_address = self.listener_socket.accept()
            self.log(f"Connessione ricevuta da {client_address}.")

            self.shell_pid, self.shell_fd = pty.fork()
            if self.shell_pid == 0:
                os.putenv("PS1", "$ ")  # Set a simple shell prompt
                os.execv("/bin/sh", ["sh"])
            else:
                threading.Thread(target=self.forward_shell_output, daemon=True).start()
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

    def send_command(self):
        if not self.client_socket:
            self.log("Nessun client connesso.")
            return

        command = self.command_entry.get()
        if command.strip() == "":
            self.log("Comando vuoto. Inserisci un comando valido.")
            return

        try:
            os.write(self.shell_fd, (command + "\n").encode("utf-8"))
            self.log(f"Comando inviato: {command}")
            self.command_entry.delete(0, tk.END)
        except Exception as e:
            self.log(f"Errore nell'invio del comando: {e}")

    def forward_shell_output(self):
        try:
            ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
            while self.running:
                output = os.read(self.shell_fd, 1024).decode(errors="ignore")
                output = ansi_escape.sub('', output)  # Remove ANSI escape sequences
                output = re.sub(r'\r\n|\r|\n', '\n', output)  # Normalize line endings
                if output:
                    self.client_socket.sendall(output.encode("utf-8", errors="ignore"))
                    self.shell_output.config(state="normal")
                    self.shell_output.insert(tk.END, output)
                    self.shell_output.config(state="disabled")
                    self.shell_output.yview(tk.END)
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


def main():
    root = tk.Tk()
    root.withdraw()

    def show_main_app():
        root.deiconify()
        PortScannerListenerApp(root)

    splash = SplashScreen(root, logo_path="logo.png", on_complete=show_main_app)
    root.mainloop()


if __name__ == "__main__":
    main()
