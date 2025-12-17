import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        print(f"Connected to server {HOST}:{PORT}")

        s.sendall(b"Can you hear me?")

        data = s.recv(1024)
        print(f"Received data from server: {data}")

    except Exception as e:
        print(f"ERROR: {e}")