import socket
import socketserver
import subprocess
import os
import argparse
import threading


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            comando_a_ejecutar = self.request.recv(1024)

            p = subprocess.Popen(comando_a_ejecutar, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
            salida , error = p.communicate()

            if salida:
                sefl.request.sendall(salida)
                print(salida)

            if error:
                self.request.sendall(error)
                print(error)

class ForkedTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", type = int, help = "puerto donde va a atender el servidor")
    parser.add_argument("-c", type = str, help ="modo de concurrencia" )
    args = parser.parse_args()

    puerto = args.p
    tipo_de_concurrencia = args.c
    direccion =("localhost",puerto)


    if tipo_de_concurrencia.lower() == "p":
        socketserver.TCPServer.allow_reuse_address = True
        with ForkedTCPServer(direccion, MyTCPHandler) as servidor:
            servidor.serve_forever()

    if tipo_de_concurrencia.lower() == "t":
        socketserver.TCPServer.allow_reuse_address = True
        with ThreadedTCPServer(direccion, MyTCPHandler) as servidor:
            servidor.serve_forever()