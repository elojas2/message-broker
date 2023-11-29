import socket
import sys
import random
import time

def temperature_sensor(simulation_interval):

    #host e porta para conexao TCP
    topic = "TEMPERATURE" 
    host = "127.0.0.1"
    port = 50055

    #conexao TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    #loop para envio de acordo com o tempo definido
    while True:
        message = random.randint(-10, 40)
        command = f"PUBLISH {topic} {message}"
        client.send(command.encode())

        # Aguarde o próximo intervalo de simulação
        time.sleep(simulation_interval)

        confirmation = client.recv(1024).decode()

        if confirmation == "PUBLISH_ACCEPTED":
            print(f"Message published: {message} \n in Topic: {topic}")
        else:
            print(f"message rejected: {message} \n in topic: {topic}")
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: python3 sensor1_emu.py <simulation_interval>")
        sys.exit(1)

    interval = int(sys.argv[1])
    temperature_sensor(interval)
