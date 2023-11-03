import socket

topics = {}
subs = {}


def controller_client(client):

    while True:
        try:
            data = client.recv(1024).decode().strip()
            if not data: break
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
    
    else:
        client.send("Command invalid".encode())


def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5000))
    server.listen(5)

    print("broker listening")

    while True:
        client, address = server.accept()
        controller_client(client)

if __name__ == '__main__':
    main()
