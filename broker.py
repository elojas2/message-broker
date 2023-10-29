import socket

HOST = 'localhost'
PORT = 50000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen()
#s.connect((serverName, serverPort))

print('Waiting connection with a client...')

conn, ender = s.accept()

print('Conected with: ', ender)

while True:

    data = conn.recv(1024)

    if not data: 
        print('Close connection')
        conn.close()
        break

    conn.sendall(data)
