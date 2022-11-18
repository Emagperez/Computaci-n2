from calc_config import app
from math import sqrt

@app.task
def raiz(filas):
    nuevos_numeros = []
        if calculo == "raiz":
            for i in fila:
                if i.isdigit():
                    resultado.append(math.sqrt(i), 2)
            return resultado
            matriz = pool.map(raiz, filas)
        
        

@app.task
def potencia(filas):
    nuevos_numeros = []
    if calculo == "potencia":
            for i in fila:
                if i.isdigit():
                    resultado.append(int(i) ** int(i))
            return resultado
            matriz = pool.map(potencia, filas)

@app.task
def log(filas):
    nuevos_numeros = []
    if calculo == "log":
            for i in fila:
                if i.isdigit():
                    resultado.append(math.log(int(i)))            
            return resultado
            matriz = pool.map(log, filas)

#@app.task
#def mult(a, b):
    #return a*b

#@app.task
#def div(a, b):
 #   if b!=0:
  #      return a/b
   # return 0


