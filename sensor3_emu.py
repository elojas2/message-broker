import socket
import sys
import random
import time

def co2_sensor(simulation_interval):

    #host e porta para conexao TCP
    topic = "CO2" 
    host = "127.0.0.1"
    port = 50055

    #conexao TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    #loop para envio de acordo com o tempo definido
    while True:
        message = round(random.uniform(300, 500), 2)
        command = f"PUBLISH {topic} {message}"
        client.send(command.encode())

        # Aguarde o próximo intervalo de simulação
        time.sleep(simulation_interval)

        confirmation = client.recv(1024).decode()

        if confirmation == "PUBLISH_ACCEPTED":
            print(f"Message published: {message}\nIn Topic: {topic}")
        else:
            print(f"message rejected: {message}\nIn topic: {topic}")
    
def main():
    if len(sys.argv) < 2:
        print("Use: python3 sensor3_emu.py (value_simulation_interval)")
        sys.exit(1)

    interval = int(sys.argv[1])
    co2_sensor(interval)

main()
