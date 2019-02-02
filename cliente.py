import socket

HOST = '127.0.0.1' #coloca o host do servidor
PORT = 8000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

arq = open('configuracoes.json', 'r')

for i in arq.readlines():
    tcp.send(i)

arq.close()
tcp.close()