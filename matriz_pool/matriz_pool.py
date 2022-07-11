import argparse
import os
import math
from multiprocessing import get_context
from multiprocessing import Pool


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--procesos", type = int, help = "numero de procesos", required =True)
    parser.add_argument("-f","--ruta", type = str, help = "ruta del archivo", default = "/tmp/matriz.txt")
    parser.add_argument("-c","--calculos" ,type = str, help = "calculos a realizar en la matriz", required  = True)
    args = parser.parse_args()

    matriz = open(args.ruta, "r")
    filas = matriz.readlines()

    pool = get_context("fork").Pool(args.procesos)

    def funcion_calculo(fila,calculo):
        resultado = []
        if calculo == "raiz":
            for i in fila:
                if i.isdigit():
                    resultado.append(math.sqrt(i), 2)
            return resultado
            matriz = pool.map(raiz, filas)
        if calculo == "potencia":
            for i in fila:
                if i.isdigit():
                    resultado.append(int(i) ** int(i))
            return resultado
            matriz = pool.map(potencia, filas)
        if calculo == "log":
            for i in fila:
                if i.isdigit():
                    resultado.append(math.log(int(i)))            
            return resultado
            matriz = pool.map(log, filas)
    











if __name__ == "__main__":
    main()