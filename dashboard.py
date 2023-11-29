import tkinter as tk
from tkinter import ttk
import socket
import threading

class SensorDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sensor Dashboard")

        # Labels para exibir os valores dos sensores
        self.temperature_label = ttk.Label(self, text="Temperature: ")
        self.temperature_label.grid(row=0, column=0, padx=10, pady=10)

        self.humidity_label = ttk.Label(self, text="Humidity: ")
        self.humidity_label.grid(row=1, column=0, padx=10, pady=10)

        self.co2_label = ttk.Label(self, text="CO2 Level: ")
        self.co2_label.grid(row=2, column=0, padx=10, pady=10)

        # Iniciar a conexão com o Broker e assinar os tópicos
        threading.Thread(target=self.connect_to_broker).start()

    def connect_to_broker(self):
        host = "127.0.0.1"
        port = 50055

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        # Subscreva aos tópicos relevantes para o dashboard
        command = "SUBSCRIBE TEMPERATURE HUMIDITY CO2"
        client.send(command.encode())

        confirmation = client.recv(1024).decode()
        if confirmation == "SUBSCRIBE_ACCEPTED":
            print("Dashboard subscribed to topics.")

        while True:
            message = client.recv(1024).decode()

            if message.startswith("topic:") and "message:" in message:
                topic, msg = message.split("message:")
                self.update_sensor_value(topic.strip(), msg.strip())

    def update_sensor_value(self, topic, value):
        if topic == "TEMPERATURE":
            self.temperature_label.config(text=f"Temperature: {value} °C")
        elif topic == "HUMIDITY":
            self.humidity_label.config(text=f"Humidity: {value}%")
        elif topic == "CO2":
            self.co2_label.config(text=f"CO2 Level: {value} ppm")

if __name__ == "__main__":
    dashboard = SensorDashboard()
    dashboard.mainloop()