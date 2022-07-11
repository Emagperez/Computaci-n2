import argparse
import os
import time
import string

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n","--numero", help = "numero de procesos hijos que generara", type = int, required = True)
    parser.add_argument("-r", "--recursivo",help = "cantidad de veces que el procesos almacenara en el archivo su letra", type = int, required = True)
    parser.add_argument("-f","--ruta", help = "ruta del archivo", type = str, required = True)
    parser.add_argument("-v", "--verboso",help = "activa modo verboso", action = "store_true")
    args = parser.parse_args()

    with open(args.ruta, "w+") as file:
        for x in range(args.numero):
            if os.fork() == 0:
                letra = chr(65 + x)
                for x in range(args.recursivo):
                    if args.verboso is True:
                        print(f"Proceso {os.getpid()} escribiendo letra {letra}")
                        file.write(letra)
                        file.flush()
                        time.sleep(1)
                    else: 
                        file
                        file.write(letra)
                        file.flush()
                    os._exit(0)
    for i in range(args.numero):
        os.wait()
    print("termino padre")


if __name__ == "__main__":
    main()