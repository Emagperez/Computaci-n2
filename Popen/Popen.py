import argparse as ap
import subprocess as sp
from datetime import datetime
import os

parser = ap.ArgumentParser(description="Ejecutor de comandos")

parser.add_argument("-c", type=str, help="Comando a ejecutar")
parser.add_argument("-f",type=str,help="Archivo de salida")
parser.add_argument("-l", type=str, help="Archivo Log")
args = parser.parse_args()
output_file = args.f
logfile = args.l

outputFile = os.open( args.output_file, os.O_RDWR|os.O_APPEND|os.O_CREAT )
logFile = os.open( args.log_file, os.O_RDWR|os.O_APPEND|os.O_CREAT )
with sp.Popen([args.command], shell=True, stdout=outputFile, stderr=sp.PIPE) as p:
    time = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    error = p.stderr.read()
    if error:
        os.write(logFile, str.encode(time)+error)
    else:
        os.write(logFile, str.encode(time+' | COMANDO: \'' + args.command + '\' ejecutado correctamente.\n'))
os.close(outputFile)
os.close(logFile)