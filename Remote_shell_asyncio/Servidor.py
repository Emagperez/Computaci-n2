import socket
import socketserver
import subprocess
import os
import argparse
import threading
import asyncio

import asyncio
import time

async def handle(reader, writer):
        while True:
            comando_a_ejecutar = self.request.recv(1024)
            addr = writer.get_extra_info('peername')

            p = subprocess.Popen(comando_a_ejecutar, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
            salida , error = p.communicate()

            if salida:
                self.request.sendall(salida)
                print(salida)

            if error:
                self.request.sendall(error)
                print(error)
    

async def main():
     parser = argparse.ArgumentParser()
    parser.add_argument("-p", type = int, help = "puerto donde va a atender el servidor")
    parser.add_argument("-c", type = str, help ="modo de concurrencia procesos o hilos" )
    args = parser.parse_args()
    puerto = args.p

    addr = server.sockets[0].getsockname()
    #print(f'Serving on {addr} {asyncio.current_task()}')

#    async with server:
    #print(f"Tareas:\n{asyncio.all_tasks()}")
    #await server.serve_forever()
    async with server:
        print("Tareas: {}".format(asyncio.current_task())))
                await server.serve_forever()






if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", type = int, help = "puerto donde va a atender el servidor")
    parser.add_argument("-c", type = str, help ="modo de concurrencia procesos o hilos" )
    args = parser.parse_args()
     server = await asyncio.start_server(handle, '127.0.0.1', puerto)

    
    
    asyncio.run(main())

    #for t in asyncio.all_tasks():
    #    print(f"Tarea: {t}")
    #data = await reader.read(100)
    #message = data.decode()
    #addr = writer.get_extra_info('peername')

    #print(f"Received {message!r} from {addr!r}")

    #print(f"Send: {message!r}")
    #writer.write(data)
    #print("encolando el mayuscula")
    #writer.write(data.upper())
    #print("ejecutando el drain()")
    #await writer.drain()

    #print("Close the connection")
    #writer.close()
    #for t in asyncio.all_tasks():
     #   print(f"Cerrando Tarea: {t}")
        