# Trabalho da disciplina de Redes - 2023.2 - UFF

## Construcao um message broker com a biblioteca socket em python

### Descrição Geral
A atividade prática da disciplina consiste no desenvolvimento de uma versão simplificada de um Message Broker que deve implementar o padrão de mensagens publish/subscribe e que será utilizado na construção e simulação de um ambiente de sensoriamento remoto.
Um Message Broker é um software que possibilita que aplicativos, sistemas e serviços se comuniquem e troquem informações. Ele permite que serviços interdependentes "conversem" uns com os outros diretamente, mesmo que tenham sido criados em linguagens diferentes ou tenham sido implementados em plataformas diferentes. Eles atuam como intermediários entre outros aplicativos, permitindo que os remetentes emitam mensagens sem saber onde estão os destinatários, se eles estão ativos ou não ou quantos deles existem. Isso facilita o desacoplamento de processos e serviços dentro de sistemas.
A implementação do Message Broker deve ser feita utilizando-se sockets, permitindo que as aplicações, sejam elas locais ou distribuídas, possam se conectar a ele. O Broker deve implementar o padrão de mensagem conhecido como publish/subscribe onde os publishers categorizam as mensagens em classes (tópicos) que são recebidas pelos subscribers.

## Para rodar:

Será necessário um terminal Linux, caso seja Windows, basta instalar o WSL.
Além disso, será necessário adicionar a biblioteca streamlit do python para a visualização do gráfico.

Para adicionar a biblioteca, digite no terminal o seguinte comando: ´´´pip install streamlit´´´.



Primeiro passo: Entrar na pasta onde está armazenado os códigos, basta digitar no terminal
``` cd codigo ```.

Segundo passo, basta iniciar o broker:


    Digite no terminal o ``` python3 broker.py ```

Terceiro passo: 


    Digite no terminal o ``` python3 sensor1_emu.py <um_numero_valor_em_segundos> ```

Terceiro passo: 


    Digite no terminal o ``` python3 sensor2_emu.py <um_numero_valor_em_segundos> ```

Quarto passo:


    Digite no terminal o ``` python3 sensor3_emu.py <um_numero_valor_em_segundos> ```

Quinto e último passo:

    Digite no terminal o ``` streamlit run dashboard.py ```