import socket
import sys

def main():
    if len(sys.argv)<4:
        print("Use: python3 publisher.py -t <topic> -m <message>")
        return
    

    topic = sys.argv[2]
    message = sys.argv[4]

    host = "127.0.0.1"
    port = 5000

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    command = f"PUBLISH {topic} {message}"

    client.send(command.encode())

    confirmation = client.recv(1024).decode()

    if confirmation == "PUBLISH_ACCEPTED":
        print(f"message published: {message} topic: {topic}")


if __name__ == "__main__":
    main()
