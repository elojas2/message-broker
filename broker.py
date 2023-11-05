import socket
import threading

#dicionario dos topicos
topics = {}
#dicionario dos subscribers
subs = {}


def controller_client(client):
    while True:
        try:
            data = client.recv(1024).decode().strip()
            if not data:
                break
            process_command_data(data, client)
        except Exception as e:
            print(f"Error {e}")
            break

    client.close()


def process_command_data(data, client):
    
    #le o comando
    read = data.split()
    command = read[0]
    #print(command)

    #caso a variavel command for SUBSCRIBE
    if command == "SUBSCRIBE":
        for topic in read[1:]:
            subs.setdefault(topic, set()).add(client)
        #retorna que foi aceito
        client.send("SUBSCRIBE_ACCEPTED".encode())

    #caso a variavel command for PUBLISHER
    elif command == "PUBLISH":
        topic = read[1]
        message = ' '.join(read[2:])
        #escreve a mensagem no topico existente
        if topic in subs:
            for s in subs[topic]:
                s.send(f"topic:{topic} and message: {message}\n".encode())
        client.send("PUBLISH_ACCEPTED".encode())

    #caso a variavel command for LIST
    elif command == "LIST":
        topic_list = "\n".join([f"Topic: {topic}, Subscribers: {len(subs[topic])}" for topic in subs])
        client.send(topic_list.encode())

    #caso a variavel command nao for nenhuma existente
    else:
        client.send("Command invalid".encode())


#controle do cliente/servidor (fica imprimindo no broker)
def handle_client(client, address):
    print(f"Accepted connection from {address}")
    controller_client(client)
    print(f"Closed connection from {address}")


def main():
    #conexao tcp do broker
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 50004))
    server.listen(5)

    print("Broker listening")

    while True:
        client, address = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client, address))
        client_thread.start()

if __name__ == '__main__':
    main()
