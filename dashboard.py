import streamlit as st
from stqdm import stqdm
import socket
import json
import threading
import time

class SensorDashboard:
    def __init__(self):
        self.temperature_value = st.empty()
        self.humidity_value = st.empty()
        self.co2_value = st.empty()

    def update_sensor_values(self, data):
        self.temperature_value.text(f"Temperature: {data['TEMPERATURE']} °C")
        self.humidity_value.text(f"Humidity: {data['HUMIDITY']}%")
        self.co2_value.text(f"CO2 Level: {data['CO2']} ppm")

def receive_data(client, dashboard):
    while True:
        try:
            data = client.recv(1024).decode()
            if not data:
                break
            data_dict = json.loads(data)
            dashboard.update_sensor_values(data_dict)
        except Exception as e:
            print(f"Error receiving data: {e}")
            break

if __name__ == "__main__":
    st.set_page_config(page_title="Sensor Dashboard", page_icon="🌡️")
    st.title("Sensor Dashboard")

    dashboard = SensorDashboard()

    # Conectar ao broker
    host = "127.0.0.1"
    port = 50055

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    # Inscrever-se nos tópicos desejados
    command = "SUBSCRIBE TEMPERATURE HUMIDITY CO2"
    client.send(command.encode())

    confirmation = client.recv(1024).decode()
    if confirmation == "SUBSCRIBE_ACCEPTED":
        print("Dashboard subscribed to topics.")

    # Iniciar thread para receber dados do broker em tempo real
    receive_thread = threading.Thread(target=receive_data, args=(client, dashboard))
    receive_thread.start()

    # Aguardar alguns segundos para permitir que o aplicativo Streamlit inicialize
    time.sleep(5)

    # Use o stqdm para forçar atualizações em tempo real
    stqdm(None)

    # Aguarde a conclusão do aplicativo Streamlit
    receive_thread.join()

    # Fechar o socket quando o programa terminar
    client.close()