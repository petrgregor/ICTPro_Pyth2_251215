import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server is listening on {HOST}:{PORT}")

    conn, addr = s.accept()


    with conn:
        print(f"connected by {conn}")
        while True:
            data = conn.recv(1024)
            print(f"Received data from client: {data}")

            response = "Hello from Python server."
            conn.sendall(response.encode())
