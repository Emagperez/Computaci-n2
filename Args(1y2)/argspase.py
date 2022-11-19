import argparse
import os


parser = argparse.ArgumentParser()

parser.add_argument("-i", type = str,help = "Archivo Origen")
parser.add_argument("-o", type = str, help = "Archivo Destino")
args = parser.parse_args()

with open(args.i, 'r') as inputfile:
    mensaje = inputfile.read()
    with open(args.o, 'w') as output:
        output.write(mensaje)         

print("El archivo", args.i, "se copió a", args.o)

#print('File %s.' % args.file)
#print('Size %d.' % args.size)
