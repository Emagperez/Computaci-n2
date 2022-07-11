import threading
import sys
import queue

def main():
    q1 = queue.Queue()
    q2 = queue.Queue()
    hilo1 = threading.Thread(target= leer, args = (q1,q2), name = hilo1, daemon = True)
    hilo2 = threading.Thread(target= encriptar, args = (q1,q2), name = hilo2, daemon = True)
    hilo1.start()
    hilo2.start    
    hilo1.join
    hilo2.join

def leer(q1,q2):
    print("Escriba mensaje para escribir: ")
    sys.stdin = open(0)
    mensaje = sys.stdin.readline()
    encriptado = q2.get


    
def encriptar_mensaje(q1,q2):
    mensaje = q1.get
    if mensaje.lower == "bye":
        q2.put("bye")
        q2.task_done()
    encriptado = ""
    for letra in mensaje:
            letra = string.ascii_letters[string.ascii_letters.index(letra)].upper
            encriptado = encriptado + letra
    q2.put(encriptado)





if __name__ == "__main__":
    main()