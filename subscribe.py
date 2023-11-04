import socket
import sys


def main():
    if len(sys.argv) < 2:
        print("Use: python3 subscribe.py -t <topic1> <topic2>")
        return
    
    topics = sys.argv[2:]

    host = "127.0.0.1"
    port = 50004

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    command = "SUBSCRIBE " + ' '.join(topics)
    print(command)
    client.send(command.encode())

    confirmation = client.recv(1024).decode()

    if confirmation == "SUBSCRIBE_ACCEPTED":
        print(f"in topics: {', '.join(topics)}")

    
    while True:
        message = client.recv(1024).decode()

        if message.startswith("topic=") and "message=" in message:
            topic, msg = message.split("message=")
            print(f"{topic.strip()} {msg.strip()}")


if __name__ == "__main__":
    main()