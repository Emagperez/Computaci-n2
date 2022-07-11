import argparse
import os
import time

def main():
    parser = argparse.ArgumentParser(descripcion = "Procesos escritores")
    parser.add_argument("-n", help = "numero de procesos hijos que generara", type = int, required = True)
    parser.add_argument("-r", help = "cantidad de veces que el procesos almacenara en el archivo su letra", type = int, required = True)
    parser.add_argument("-f", help = "ruta del archivo", type = str, required = True)
    parser.add_argument("-v", help = "activa modo verboso", action = "store_true")
    args = parser.parse_args()















if __name__ == "__main__":
    main()