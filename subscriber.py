import socket
import sys


def subscribe():
    #caso seja digitado o comando errado
    if len(sys.argv) < 2:
        print("Use: python3 subscribe.py -t <topic1> <topic2>")
        return
    
    topics = sys.argv[2:]

    #host e porta
    host = "127.0.0.1"
    port = 50055

    #conexao TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    #commando de inscricao dos topicos
    command = "SUBSCRIBE " + ' '.join(topics)
    client.send(command.encode())

    #recebe a confirmacao ou nao do servidor
    confirmation = client.recv(1024).decode()

    if confirmation == "SUBSCRIBE_ACCEPTED":
        print("Subscribed topic.")
        print(f"topics: {', '.join(topics)}")

    while True:
        message = client.recv(1024).decode()

        if message.startswith("topic:") and "message:" in message:
            topic, msg = message.split("message:")
            print(f"TOPIC: {topic.strip()}       MESSAGE: {msg.strip()}")


subscribe()