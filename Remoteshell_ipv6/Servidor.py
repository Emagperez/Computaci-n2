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
    address_family = socket.AF_INET6
    pass

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    address_family = socket.AF_INET6
    pass

def socket_ipv6_procesos(direccion):
    if direccion[0] == socket.AF_INET6:
        
        with ForkedTCPServer(direccion[6], MyTCPHandler) as servidor:
            servidor.serve_forever()

def socket_ipv6_hilos(direccion):
    hilo_6 = threading.current_thread().nombre
    hilo_numero_6 = threading.get_native_id()
    with ThreadedTCPServer()(direccion[6], MyTCPHandler) as servidor:
            servidor.serve_forever()




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", type = int, help = "puerto donde va a atender el servidor")
    parser.add_argument("-c", type = str, help ="modo de concurrencia p o t" )
    args = parser.parse_args()

    puerto = args.p
    tipo_de_concurrencia = args.c
    direccion = []
    direcciones = socket.getaddrinfo(("localhost", puerto,socket.AF_INET6,1)[0])


    if tipo_de_concurrencia.lower() == "p":
        for i in direcciones:
            direcciones.append(threading.Thread(target = socket_ipv6_procesos, args =(i,))).start()

    if tipo_de_concurrencia.lower() == "t":
        for i in direcciones:
            direcciones.append(threading.Thread(target= socket_ipv6_hilos, args= (i,))).start()
        