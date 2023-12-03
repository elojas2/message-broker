import streamlit as st
import socket

# Função principal para executar o aplicativo
def main():
    # Configurar a página uma vez no início do script
    st.set_page_config(page_title='Monitoramento em Tempo Real', page_icon=':chart_with_upwards_trend:')

    st.title("Monitoramento em Tempo Real")
    
    #host e porta
    host = "127.0.0.1"
    port = 50055

    #conexao TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    command = "SUBSCRIBE TEMPERATURE HUMIDITY CO2"
    client.send(command.encode())

    #recebe a confirmacao ou nao do servidor
    confirmation = client.recv(1024).decode()

    if confirmation == "SUBSCRIBE_ACCEPTED":
        print("Subscribed topic.")
    

    # Criar placeholders iniciais para os valores e criar gráficos iniciais
    temperatura_placeholder = st.empty()
    temperatura_chart = st.line_chart()
    umidade_placeholder = st.empty()
    umidade_chart = st.line_chart()
    co2_placeholder = st.empty()
    co2_chart = st.line_chart()

    st.text("")  # Adicionar espaço para melhorar a aparência

    historico_temperatura = []
    historico_umidade = []
    historico_co2 = []

    temperatura = 0
    umidade = 0
    co2 = 0

    while True:
        message = client.recv(1024).decode()

        if message.startswith("topic:") and "message:" in message:
            topic, msg = message.split("message:")
            print(topic)
            print(msg)
        
        if "TEMPERATURE" in topic:
            temperatura = float(msg.strip())
        elif "HUMIDITY" in topic:
            umidade = float(msg.strip())
        elif "CO2" in topic:
            co2 = float(msg.strip())

        # Atualizar os placeholders com os novos valores
        temperatura_placeholder.text(f"Temperatura: {temperatura} °C")
        umidade_placeholder.text(f"Umidade: {umidade} %")
        co2_placeholder.text(f"CO2: {co2} ppm")

        # Adicionar novos pontos aos gráficos
        historico_temperatura.append(temperatura)
        historico_umidade.append(umidade)
        historico_co2.append(co2)

        temperatura_chart.line_chart(historico_temperatura)
        umidade_chart.line_chart(historico_umidade)
        co2_chart.line_chart(historico_co2)

main()