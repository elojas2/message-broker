Alunos: Caio Marcio e Eloyse Fernanda

### Visão geral
Para a segunda parte do trabalho, não houveram mudanças significativas no
´´´broker.py´´´ e foram removidos os módulos ´´´subscriber.py´´´, ´´´publisher.py´´´, ´´´broker_com.py´´´.
Dessa forma, foram criados novos módulos, sendo eles o ´´´dashboard.py´´´, módulos
para sensores (sensor1_emu.py, sensor2_emu.py, sensor3_emu.py).


##### Ordem dos comandos no terminal:


´´´python3 broker.py´´´


´´´python3 dashboard.py´´´


´´´python3 sensor1_emu.py´´´


´´´python3 sensor2_emu.py´´´


´´´python3 sensor3_emu.py´´´


´´´streamlit run dashboard.py´´´

#### Dashboard
Nesse módulo, foi usado como base o codigo anterior do subscriber, ele é
iniciado configurando o host e a porta para que seja feita a conexao TCP e assim,
fazendo a inscrição de alguns tópicos e manda para o broker, o broker manda uma
confirmação dizendo se foi aceito ou não.
Após as configurações, é iniciado alguns placeholders, listas (vetores) e
variáveis para inicialização dos gráficos.


Entrando em um loop para que sejam lidas os valores que são gerados e
enviados aleatoriamente pelos sensores e atualizando os placeholders com os
novos valores para cada tópico existente.
Sensores


Nos sensores foi utilizado como base o código do publisher e usamos uma
das bibliotecas que foi sugerida pelo professor chamado Streamlit. O código
inicia-se também com as configurações do host e da porta TCP para a conexão com
os outros módulos. Ao entrar no loop é gerado números aleatórios e são publicados
para o broker, esperando a confirmação do mesmo. Ao ser confirmado pelo broker,
são enviados constantemente valores aleatórios para a publicação no tópico do
sensor e no tempo que foi determinado via comando pelo terminal.