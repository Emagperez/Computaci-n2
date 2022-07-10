from sympy import
from cmath import sqrt , log10
import argparse
import multiprocessing as mp




def cargarArchivo(file):
  f = open(file,"r")
  filas = 0
  for linea in f:
    filas +=1
    palabras = linea.strip().split(" ")
    M = np.empty((filas,len(palabras)),dtype = "U20")
    filas,columnas = M.shape
    for i in range(filas):
      for j in range(columnas):
      M[i,j] = palabras[j]
  return M


def main():
    parser = argparse.ArgumentParser(description= 'matriz')
    parser.add_argument('-f','--file')
    parser.add_argument('-c','--cal')
    parser.add_argument('-p','--proceso')


def Calculo_raiz():


if __name__ == '__main__'
cargarArchivo()
main()