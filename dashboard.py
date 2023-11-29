import streamlit as st
from stqdm import stqdm
import socket
import time
import threading

class SensorDashboard:
    def __init__(self):
        self.temperature_value = st.empty()
        self.humidity_value = st.empty()
        self.co2_value = st.empty()

    def update_sensor_values(self, data):
        self.temperature_value.text(f"Temperature: {data['TEMPERATURE']} °C")
        self.humidity_value.text(f"Humidity: {data['HUMIDITY']}%")
        self.co2_value.text(f"CO2 Level: {data['CO2']} ppm")

def streamlit_app():
    st.set_page_config(page_title="Sensor Dashboard", page_icon="🌡️")
    st.title("Sensor Dashboard")
    
    dashboard = SensorDashboard()

    topics = sys.argv[2:]

    #host e porta
    host = "127.0.0.1"
    port = 50055

    #conexao TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    command = "SUBSCRIBE " + ' '.join(topics)
    client.send(command.encode())

    while True:
        # Substitua este bloco com a lógica de leitura de dados do broker
        simulated_data = {
            'TEMPERATURE': '25',
            'HUMIDITY': '60',
            'CO2': '400'
        }

        dashboard.update_sensor_values(simulated_data)

        # Aguarde alguns segundos antes de atualizar novamente
        time.sleep(1)

if __name__ == "__main__":
    # Inicie a execução do aplicativo Streamlit em segundo plano usando threading
    thread = threading.Thread(target=streamlit_app)
    thread.start()

    # Aguarde alguns segundos para permitir que o aplicativo Streamlit inicialize
    time.sleep(5)

    # Use o stqdm para forçar atualizações em tempo real
    stqdm(None)

    # Aguarde a conclusão do aplicativo Streamlit
    thread.join()