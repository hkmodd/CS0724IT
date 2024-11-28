
import requests
import tkinter as tk

class HTTPMethods:
    def __init__(self, log_func):
        self.http_results = []
        self.log = log_func

    def send_http_request(self, method, url, http_response_output):
        try:
            if method == "GET":
                response = requests.get(url, timeout=5)
            elif method == "POST":
                response = requests.post(url, timeout=5)
            elif method == "PUT":
                response = requests.put(url, timeout=5)
            elif method == "DELETE":
                response = requests.delete(url, timeout=5)
            else:
                self.log("Metodo HTTP non supportato.")
                return

            self.http_results.append({
                "method": method,
                "url": url,
                "status_code": response.status_code,
                "response": response.text
            })

            http_response_output.config(state="normal")
            http_response_output.delete(1.0, tk.END)
            http_response_output.insert(tk.END, f"Status Code: {response.status_code}\n")
            http_response_output.insert(tk.END, response.text)
            http_response_output.config(state="disabled")

        except requests.RequestException as e:
            self.log(f"Errore nella richiesta HTTP: {e}")
