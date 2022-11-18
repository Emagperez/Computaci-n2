import argparse
import os
from calc_config import Celery
from calc import raiz, potencia, log




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help = "ruta del archivo")
    parser.add_argument("-f","--ruta", type = str, help = "ruta del archivo", default = "/tmp/matriz.txt")
    parser.add_argument("-c","--calculos" ,type = str, help = "calculos a realizar en la matriz", required  = True)
    args = parser.parse_args()

    matriz = open(args.ruta, "r")
    filas = matriz.readlines()



def funcion_calculo(calculos):
        if calculos == "raiz":
            numero_con_Raiz = calc.raiz.delay()

        elif calculos == "potencia":
            numero_con_Potencia = calc.potencia.delay()

        elif calculos == "log":
            resultado = calc.log.delay()
         
            
        
            
            




if __name__ == "__main__":
    main()


