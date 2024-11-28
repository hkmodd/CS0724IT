import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox, QTableWidget,
    QTableWidgetItem, QGroupBox, QFileDialog, QSplashScreen
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QTimer
from port_listener import PortListener
from port_scanner import PortScanner
from http_methods import HTTPMethods
import threading
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PortWatch - Scanner e Listener con Shell")
        self.setGeometry(100, 100, 1200, 700)

        self.port_listener = PortListener(self.log)
        self.port_scanner = PortScanner(self.log, self.add_scan_result, threading.Lock())
        self.http_methods = HTTPMethods(self.log)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Sezione Scanner
        scanner_group = QGroupBox("Port Scanner")
        scanner_layout = QVBoxLayout(scanner_group)
        scanner_input_layout = QHBoxLayout()
        scanner_layout.addLayout(scanner_input_layout)

        scanner_input_layout.addWidget(QLabel("Indirizzo IP:"))
        self.ip_entry = QLineEdit("localhost")
        scanner_input_layout.addWidget(self.ip_entry)

        self.scan_button = QPushButton("Avvia Scansione")
        self.scan_button.clicked.connect(self.start_scan)
        scanner_input_layout.addWidget(self.scan_button)

        self.stop_scan_button = QPushButton("STOP Scansione")
        self.stop_scan_button.setEnabled(False)
        self.stop_scan_button.clicked.connect(self.stop_scan)
        scanner_input_layout.addWidget(self.stop_scan_button)

        self.result_table = QTableWidget()
        self.result_table.setColumnCount(3)
        self.result_table.setHorizontalHeaderLabels(["Porta", "Stato", "Protocollo"])
        scanner_layout.addWidget(self.result_table)

        self.export_button = QPushButton("Esporta Report")
        self.export_button.clicked.connect(self.export_report)
        scanner_layout.addWidget(self.export_button)

        main_layout.addWidget(scanner_group)

        # Sezione Listener
        listener_group = QGroupBox("Gestione Listener")
        listener_layout = QVBoxLayout(listener_group)
        listener_input_layout = QHBoxLayout()
        listener_layout.addLayout(listener_input_layout)

        listener_input_layout.addWidget(QLabel("Indirizzo IP Listener:"))
        self.listener_ip_entry = QLineEdit("0.0.0.0")
        listener_input_layout.addWidget(self.listener_ip_entry)

        listener_input_layout.addWidget(QLabel("Porta Listener:"))
        self.port_entry = QLineEdit("9000")
        listener_input_layout.addWidget(self.port_entry)

        self.start_button = QPushButton("Avvia Listener")
        self.start_button.clicked.connect(self.start_listener)
        listener_input_layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Ferma Listener")
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.stop_listener)
        listener_input_layout.addWidget(self.stop_button)

        self.shell_output = QTextEdit()
        self.shell_output.setReadOnly(True)
        listener_layout.addWidget(self.shell_output)

        shell_input_layout = QHBoxLayout()
        self.command_entry = QLineEdit()
        shell_input_layout.addWidget(self.command_entry)

        self.send_button = QPushButton("Invia")
        self.send_button.setEnabled(False)
        self.send_button.clicked.connect(self.send_command)
        shell_input_layout.addWidget(self.send_button)

        listener_layout.addLayout(shell_input_layout)

        self.clear_shell_button = QPushButton("Cancella Output Shell")
        self.clear_shell_button.clicked.connect(self.clear_shell_output)
        listener_layout.addWidget(self.clear_shell_button)

        main_layout.addWidget(listener_group)

        # Sezione HTTP Tester
        http_group = QGroupBox("HTTP Tester")
        http_layout = QVBoxLayout(http_group)
        http_input_layout = QHBoxLayout()
        http_layout.addLayout(http_input_layout)

        http_input_layout.addWidget(QLabel("Metodo HTTP:"))
        self.http_method_combobox = QComboBox()
        self.http_method_combobox.addItems(["GET", "POST", "PUT", "DELETE"])
        http_input_layout.addWidget(self.http_method_combobox)

        http_input_layout.addWidget(QLabel("URL:"))
        self.http_url_entry = QLineEdit()
        http_input_layout.addWidget(self.http_url_entry)

        self.http_send_button = QPushButton("Invia Richiesta")
        self.http_send_button.clicked.connect(self.send_http_request)
        http_input_layout.addWidget(self.http_send_button)

        self.http_response_output = QTextEdit()
        self.http_response_output.setReadOnly(True)
        http_layout.addWidget(self.http_response_output)

        main_layout.addWidget(http_group)

        # Sezione Log
        log_group = QGroupBox("Log")
        log_layout = QVBoxLayout(log_group)
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        log_layout.addWidget(self.log_area)

        self.clear_log_button = QPushButton("Cancella Log")
        self.clear_log_button.clicked.connect(self.clear_log)
        log_layout.addWidget(self.clear_log_button)

        main_layout.addWidget(log_group)

    def log(self, message):
        self.log_area.append(message)
        self.log_area.ensureCursorVisible()

    def add_scan_result(self, port, state, protocol):
        row_position = self.result_table.rowCount()
        self.result_table.insertRow(row_position)
        self.result_table.setItem(row_position, 0, QTableWidgetItem(str(port)))
        self.result_table.setItem(row_position, 1, QTableWidgetItem(state))
        self.result_table.setItem(row_position, 2, QTableWidgetItem(protocol))

    def start_scan(self):
        target_ip = self.ip_entry.text()
        self.result_table.setRowCount(0)
        self.port_scanner.start_scan(target_ip, self.scan_button, self.stop_scan_button, self.result_table)

    def stop_scan(self):
        self.port_scanner.stop_scan(self.scan_button, self.stop_scan_button)


    def start_listener(self):
        ip_address = self.listener_ip_entry.text()
        port = int(self.port_entry.text())
        self.port_listener.start_listener(ip_address, port, self.shell_output, self.send_button)

    def stop_listener(self):
        self.port_listener.stop_listener()

    def send_command(self):
        self.port_listener.send_command(self.command_entry, self.port_listener.shell_fd)

    def clear_shell_output(self):
        self.shell_output.clear()

    def send_http_request(self):
        method = self.http_method_combobox.currentText()
        url = self.http_url_entry.text()
        self.http_methods.send_http_request(method, url, self.http_response_output)

    def clear_log(self):
        self.log_area.clear()

    def export_report(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Salva Report", "", "CSV Files (*.csv);;PDF Files (*.pdf)")
        if not file_path:
            return

        try:
            if file_path.endswith(".csv"):
                with open(file_path, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Porta", "Stato", "Protocollo"])
                    for row in range(self.result_table.rowCount()):
                        writer.writerow([
                            self.result_table.item(row, 0).text(),
                            self.result_table.item(row, 1).text(),
                            self.result_table.item(row, 2).text()
                        ])
                self.log(f"Report CSV salvato in {file_path}")
            elif file_path.endswith(".pdf"):
                c = canvas.Canvas(file_path, pagesize=letter)
                c.setFont("Helvetica", 12)
                y = 750
                for row in range(self.result_table.rowCount()):
                    c.drawString(100, y, f"Porta: {self.result_table.item(row, 0).text()}, Stato: {self.result_table.item(row, 1).text()}, Protocollo: {self.result_table.item(row, 2).text()}")
                    y -= 15
                    if y < 50:
                        c.showPage()
                        y = 750
                c.save()
                self.log(f"Report PDF salvato in {file_path}")
        except Exception as e:
            self.log(f"Errore nell'esportazione: {e}")

def main():
    app = QApplication(sys.argv)

    # Mostra la SplashScreen
    splash_pix = QPixmap("logo.png")
    splash = QSplashScreen(splash_pix, Qt.WindowType.WindowStaysOnTopHint)
    splash.show()

    # Carica l'app principale
    def start_main():
        splash.close()
        window = MainWindow()
        window.show()

    QTimer.singleShot(2000, start_main)  # 2 secondi di SplashScreen
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
