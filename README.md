# Trabalho da disciplina de Redes - 2023.2 - UFF

## Construcao um message broker com a biblioteca socket em python

### Descrição Geral


A atividade prática da disciplina consiste no desenvolvimento de uma versão simplificada de um Message Broker que deve implementar o padrão de mensagens publish/subscribe e que será utilizado na construção e simulação de um ambiente de sensoriamento remoto.
Um Message Broker é um software que possibilita que aplicativos, sistemas e serviços se comuniquem e troquem informações. Ele permite que serviços interdependentes "conversem" uns com os outros diretamente, mesmo que tenham sido criados em linguagens diferentes ou tenham sido implementados em plataformas diferentes. Eles atuam como intermediários entre outros aplicativos, permitindo que os remetentes emitam mensagens sem saber onde estão os destinatários, se eles estão ativos ou não ou quantos deles existem. Isso facilita o desacoplamento de processos e serviços dentro de sistemas.
A implementação do Message Broker deve ser feita utilizando-se sockets, permitindo que as aplicações, sejam elas locais ou distribuídas, possam se conectar a ele. O Broker deve implementar o padrão de mensagem conhecido como publish/subscribe onde os publishers categorizam as mensagens em classes (tópicos) que são recebidas pelos subscribers.

#### Esse projeto consiste em duas partes, esse readme fala somente da primeira parte do projeto. 

##### Primeira parte do projeto está na branch MAIN. para ver a segunda, basta ver a branch xxxx.


## Para rodar:

Será necessário um terminal Linux, caso seja Windows, basta instalar o WSL para que seja possível rodar.
Primeiro passo: entrar na pasta codigo, basta digitar no terminal ```cd codigo``` 


Ao entrar na pasta, basta iniciar o broker, para iniciar, basta digitar:


    Digite no terminal o ``` python3 broker.py ```

Segundo passo: (substitua o topico por algo que queira, você pode digitar mais de um)


    Digite no terminal o ``` python3 subscriber.py -t <topic_you_want> <topic_you_want1> ```

Terceiro passo: (escolha um tópico e escreva uma mensagem para ele)


    Digite no terminal o ``` python3 publisher.py -t <topic_you_want> -m <message_you_want> ```

Quarto passo:


    Digite no terminal o ``` python3 broker_com.py -c LIST ```

