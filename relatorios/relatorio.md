#### Alunos: Caio Marcio e Eloyse Fernanda

### Visão geral
O sistema consiste em um Message broker com conexão TCP para a
comunicação entre os mesmos.
Esse trabalho foi constituído em 4 módulos que serão explicados melhor ao decorrer
do relatório. 


Para o desenvolvimento desses módulos foram utilizadas as ´´´bibliotecas de
Sockets´´´ para que seja possível fazer a comunicação Servidor-Cliente, também foi
utilizado a ´´´biblioteca de threading´´´ para que seja possível fazer conexões paralelas e
não atrapalhar o fluxo de cada módulo em execução.


O protocolo de comunicação entre eles é definido em algumas etapas
simples, em primeira ocasião, o servidor precisa estar rodando em estado de
"escuta" para que possa receber conexão dos clientes, ao entrar nesse estado, os
clientes podem se conectar ao servidor e podem fazer a comunicação e a troca de
informações necessárias.


Quando o cliente se conecta, o servidor lança uma mensagem de confirmação para
o cliente que indica se o comando do cliente foi aceito ou não. Em caso de
afirmação, o servidor manda os dados para o cliente, podendo conter informações
sobre os tópicos, lista, etc. O cliente, por sua vez, fica responsável por receber
esses dados do servidor e utilizá-los da maneira que for necessária.

## Para entender um pouco sobre cada módulo:

#### Broker
Esse é o módulo mais complexo, pois ele funciona basicamente como um
servidor onde receberá as conexões e ficará intermediando com os outros módulos
(clientes), logo será necessário algumas funcoes para garantir o funcionamento do
mesmo e dos clientes. Nele está presente algumas funções:


Inicialmente, esse módulo há a criacao de dois dicionários vazios, um para
guardar os topicos e outro para os subscribers, seguindo entao para a função de
get_remote_adress que fica responsável apenas por coletar o número de IP e porta
do cliente para fins de identificação.


´´´Controller_client´´´ lida com a comunicação entre o cliente-servidor, ele irá
verificar se há dados, se houver, chamará a proxima funcao, o
proccess_command_data. Essa função será responsável por analisar e fazer as
ações necessárias a partir dos comandos que são recebidos dos clientes, seja ele
publishers, subscribers e command sera responsavel tambem em enviar
mensagens de confirmacao para o cliente, para que possam ser executadas as
determinadas funções e funcionalidades de cada cliente.
client_server lida com a comunicação de um cliente e seu endereço. Ela fica
responsável por chamar a função controller_client e imprimir mensagens de início e
encerramento de conexões.


Por fim, há a funçao main, que irá abrir o servidor e deixar em modo de
espera, e nessa funcao que é chamada o controller_client para iniciar todas as
outras funções.


#### Broker Subscriber
Aqui ele será um dos clientes. O Subscriber irá se conectar com o Broker e
fazer a "assinatura" de algum tópico escolhido pelo próprio usuário via terminal.
Ao ser feito a assinatura, o módulo subscriber se mantera ativo aguardando as
mensagens que serão publicadas pelo Publisher, toda vez que o metodo publisher
publicar alguma mensagem no topico escolhido, o terminal do subscriber irá retornar
o topico e a mensagem publicada.


#### Broker Publisher
Outro cliente que tambem se conectará com o Broker. A função desse
módulo é publicar mensagens em tópicos específicos já existentes e que foram
criados pelo módulo anterior, em seguida, encerra a conexao para que seja possivel
mandar mais mensagens para outros topicos.


#### Broker Command
Outro cliente que irá conectar com o Broker. Esse módulo permite que seja
possível que os clientes enviem comandos para o servidor. Nesse caso, foi criado
somente o List, esse comando irá listar os tópicos e os assinantes desses tópicos,
isso permite uma ampla visão e transparencia dos dados.

Broker, broker_com e relatorio feito por Eloyse e broker_pub e broker_sub feito por
Caio Marcio.