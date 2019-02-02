import socket

HOST = '127.0.0.1'      #Endereco do servidor
PORT = 8000             #porta para conexao com o servidor

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

conn, addr = tcp.accept()

print("Iniciando Servidor")

while 1:
    arq = open('configuracoes_medidor.json', 'w')

    dados = conn.recv(1024)
    if not dados:
        break
    arq.write(dados)

arq.close()
conn.close()
