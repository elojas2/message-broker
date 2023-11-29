import socket
import sys
import random
import time

def humidity_sensor(simulation_interval):

    #host e porta para conexao TCP
    topic = "HUMIDITY" 
    host = "127.0.0.1"
    port = 50055

    #conexao TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    #loop para envio de acordo com o tempo definido
    while True:
        try:
            message = random.randint(0, 100)
            command = f"PUBLISH {topic} {message}"
            client.send(command.encode())

            # Aguarde o próximo intervalo de simulação
            time.sleep(simulation_interval)

            confirmation = client.recv(1024).decode()

            if confirmation == "PUBLISH_ACCEPTED":
                print(f"Message published: {message} \nin Topic: {topic}")
            else:
                print(f"message rejected: {message} \nin topic: {topic}")
        except Exception as e:
            print(f"Error in humidity_sensor: {e}")
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: python3 sensor2_emu.py <simulation_interval>")
        sys.exit(1)

    interval = int(sys.argv[1])
    humidity_sensor(interval)
