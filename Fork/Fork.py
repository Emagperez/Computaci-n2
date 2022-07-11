import argparse
import os

def main():
    parser = argparse.ArgumentParser(descripcion = "PROCESOS")
    parser.add_argument("-n", help = "escriba -n y numero de procesos que quiere crear", required = True)
    parser.add_argument("-h")
    parser.add_argument("-v", help = "-v activa el modo verboso", action = "store_true")
    args = parser.parse_args()




if __name__ == "__main__":
    main()