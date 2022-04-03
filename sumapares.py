import os 
import argparse



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, help="Numero de procesos que se quieren generar", required=True)
    parser.add_argument("-v",help="-v para habiltiar modo verboso",action="stroe true",default=False)
    args = parser.parse_args()
    numero = args.numero
    verboso = args.verboso




pid = os.fork

def suma(pid):
    sumapares = 0
    for n in range(pid):
        if n%2 == 0:
            sumapares += n
    return sumapares

    


if __name__ == "__main__:"
    main()
