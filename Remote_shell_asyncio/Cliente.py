import socket
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-h", help = "dirección IP o nombre del servidor al que conectarse", required = True)
parser.add_argument("-p", help = " número de puerto del servidor")
args = parser.parse_args()
host = args.h
puerto = args.p

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.connect((host,puerto))


while True:
    comando_a_ejecutar = input("Comando que quiere realizar: ")
    mi_socket.send(comando_a_ejecutar)
    mensaje = mi_socket.recv(1024)
    print(mensaje)










