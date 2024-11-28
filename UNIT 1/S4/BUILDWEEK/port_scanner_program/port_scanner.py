
import socket
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import threading

class PortScanner:
    def __init__(self, log_func, result_func, lock):
        self.port_queue = Queue()
        self.results = {}
        self.open_ports = []
        self.scanning = False
        self.log = log_func
        self.add_result = result_func
        self.lock = lock

    def start_scan(self, target_ip, scan_button, stop_scan_button, result_table):
        self.open_ports = []
        self.results = {}
        self.scanning = True
        scan_button.setEnabled(False)  # Corretto da config() a setEnabled(False)
        stop_scan_button.setEnabled(True)  # Corretto da config() a setEnabled(True)
        for port in range(1, 1025):
            self.port_queue.put(port)

        threading.Thread(target=self.perform_scan, args=(target_ip,), daemon=True).start()


    def stop_scan(self, scan_button, stop_scan_button):
        self.scanning = False
        scan_button.setEnabled(True)  # Corretto da config() a setEnabled(True)
        stop_scan_button.setEnabled(False)  # Corretto da config() a setEnabled(False)
        self.log("Scansione fermata.")


    def perform_scan(self, target_ip):
        with ThreadPoolExecutor(max_workers=50) as executor:
            while not self.port_queue.empty() and self.scanning:
                executor.submit(self.scan_worker, target_ip)

        self.log("Scansione completata.")

    def scan_worker(self, target_ip):
        if not self.port_queue.empty() and self.scanning:
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
        except Exception as e:
            self.log(f"Errore durante la scansione della porta {port}: {e}")
