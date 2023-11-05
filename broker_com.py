import socket
import sys

def main():
    if len(sys.argv) < 3:
        print("Use: python3 broker_com.py -c <command>")
        return
    
    #pega o comando
    command = sys.argv[2]

    #host e porta para conexao TCP
    host = "127.0.0.1"
    port = 50004
    #conexao TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    #comando list (unico pedido)
    if command == "LIST":
        client.send(f"LIST".encode())
        data = client.recv(4096).decode()
        print("List of topics and subscribers:")
        print(data)
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
