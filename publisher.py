import socket
import sys

def publisher():
    #caso seja digitado o comando errado
    if len(sys.argv)<4:
        print("Use: python3 publisher.py -t <topic> -m <message>")
        return
    
    #pega o nome do topico e mensagem
    topic = sys.argv[2]
    message = sys.argv[4]

    #host e porta para conexao TCP
    host = "127.0.0.1"
    port = 50055
    #conexao TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    #comando para publicar a mensagem no topico
    command = f"PUBLISH {topic} {message}"
    #print(command)

    #envia o comando
    client.send(command.encode())
    #pega a confirmacao, caso seja aceito, entra no if e imprime a mensagem e o topico publicados
    confirmation = client.recv(1024).decode()

    if confirmation == "PUBLISH_ACCEPTED":
        print(f"Message published: {message} \n in Topic: {topic}")
    else:
        print(f"message rejected: {message} \n in topic: {topic}")

publisher()
