import socket
import threading

#dicionario de topic
topics = {}
#dicionario das inscricoes
subs = {}

#pega o io
def get_remote_address(client):
    ip = f'{client.getpeername()[0]} : {client.getpeername()[1]}'
    return ip
    
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

#principal, aqui tera o tratamento dos comandos
def process_command_data(data, client):
    #leitura do comando
    read = data.split()
    command = read[0]
    #comando subscribe
    if command == "SUBSCRIBE":
        #verifica a segunda palavra do read pra frente
        for topic in read[1:]:
            #verifica se já esxite
            subs.setdefault(topic, set()).add(client)
        client.send("SUBSCRIBE_ACCEPTED".encode())
        print("received and subscribed")
    
    #comando publish
    elif command == "PUBLISH":
        topic = read[1]
        message = ' '.join(read[2:])

        if topic in subs:
            for s in subs[topic]:
                s.send(f"topic: {topic} message: {message}\n".encode())
        client.send("PUBLISH_ACCEPTED".encode())
        print("received and published")
    #comando LIST
    elif command == "LIST":
        client.send("COMMAND_ACCEPTED".encode())
        topic_list = "\n".join([f"Topic: {topic}, Subscriber: {', '.join(map(get_remote_address, subs[topic]))}" for topic in subs])
        client.send(topic_list.encode())

    else:
        client.send("Command invalid".encode())


def client_server(client, address):
    print(f"Accepted connection from {address}")
    controller_client(client)
    print(f"Closed connection from {address}")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 50055))
    server.listen(5)

    print("Broker listening")

    while True:
        client, address = server.accept()
        client_thread = threading.Thread(target=client_server, args=(client, address))
        client_thread.start()

#chama o main
main()
