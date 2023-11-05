import socket
import threading

topics = {}
subs = {}

def get_remote_address(client):
    ip = f'{client.getpeername()[0]}:{client.getpeername()[1]}'
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


def process_command_data(data, client):
    read = data.split()
    command = read[0]

    if command == "SUBSCRIBE":
        for topic in read[1:]:
            subs.setdefault(topic, set()).add(client)
        client.send("SUBSCRIBE_ACCEPTED".encode())

    elif command == "PUBLISH":
        topic = read[1]
        message = ' '.join(read[2:])

        if topic in subs:
            for s in subs[topic]:
                s.send(f"topic={topic} and message={message}\n".encode())
        client.send("PUBLISH_ACCEPTED".encode())

    elif command == "LIST":
        #topic_list = "\n".join([f"Topic: {topic}, Subscribers: {', '.join(map(str, subs[topic]))}" for topic in subs])
        topic_list = "\n".join([f"Topic: {topic}, Subscribers: {', '.join(map(get_remote_address, subs[topic]))}" for topic in subs])
        #client.send("")
        client.send(topic_list.encode())

    else:
        client.send("Command invalid".encode())


def handle_client(client, address):
    print(f"Accepted connection from {address}")
    controller_client(client)
    print(f"Closed connection from {address}")


def main():
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
