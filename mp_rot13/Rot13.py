import multiprocessing
import sys
import os
import time

def main():
    r , w = multiprocessing.Pipe()
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target = hijo1, args = (w, q))
    p2 = multiprocessing.Process(target = hijo2, args = (q,r))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

def hijo1(w,q):
    print("mensaje para leer: ")
    sys.stdin = open(0)
    datos = sys.stdin.readline()
    w.send(datos)
    print("El mensaje encriptado es{q.get}")

def hijo2(r,q):
    datos_ingresados = r.recv()
    r.close()
    mensaje_encriptado = rot13(str(datos_ingresados))
    q.put(mensaje_encriptado)

def rot13():
    mensaje_encriptado = []
    for letra in mensaje[:-1]:
        i = ord(letra) + 13
        if ord(letra) >=97 and ord(letra) <= 122:
            if i > 122:
                i = i -122 + 97 -1
        else:
            if i > 90:
                i = i - 90 + 65 -1
        l_encriptada = chr(i)
        mensaje_encriptado.append(l_encriptada)
    return "".join(mensaje_encriptado)





if __name__ == "__main__":
    main()