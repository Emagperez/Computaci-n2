import argparse
import os
import mmap
import sys
import signal



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--ruta", type = str, help = "Pasar ruta del archivo", required = True)
    args = parser.parse_args()
    hijo1 = 0
    hijo2 = 0
    mem = mmap.mmap(-1,1024)
    print("PID Padre: %d" % os.getpid())
    signal.signal(signal.SIGUSR1, padre) 
    signal.signal(signal.SIGUSR2, hijo1_avisa_al_padre) 

    global hijo1
    hijo1 = os.fork()
    if not hijo1:
        file.close()
        print("(Proceso Hijo 1 PID %d) Ingrese linea por teclado: " % os.getpid())
        for line in sys.stdin: 
            if line == "bye\n": 
                print("Ingresaste bye... terminando procesos")
                os.kill(os.getppid(), signal.SIGUSR2) 
                break 
            
            shared_mem.resize(len(line)) 
            shared_mem.seek(0) 
            shared_mem.write(line.encode()) 
            shared_mem.seek(0) 
            os.kill(os.getppid(), signal.SIGUSR1) 
            print("Ingrese linea por teclado: ")
        print("Proceo hijo1 PID %d saliendo" % os.getpid())
        os._exit(0) 
        
    global hijo2
    hijo2 = os.fork() 
    
    if not hijo2: 
        signal.signal(signal.SIGUSR1, hijo2) 
        signal.signal(signal.SIGUSR2, hijo2_terminar) 
        while True: 
            signal.pause()
        os._exit(0)

def padre(numero, frame): 
    shared_mem.seek(0) 
    leer = shared_mem.readline() 
    print("(PID %d) Linea leida: %s" % (os.getpid(),leer.decode())) 
    os.kill(hijo2, signal.SIGUSR1)

def Hijo1(numero, frame): 
    print("Proceso padre PID: %d      Mi hijo1 PID: %d va a terminar" % (os.getpid(), hijo1))
    os.kill(hijo2, signal.SIGUSR2) 
    signal.signal(signal.SIGUSR1, signal.SIG_DFL) 

def hijo2(numero, frame): 
    shared_mem.seek(0) 
    leer = shared_mem.readline().decode().upper().encode() 
    print("(PID %d) Linea en mayus: %s" % (os.getpid(), (leer.decode()))) 
    file.write(leer) 
    file.flush() 

def hijo2_terminar(nro, frame):
    print("Soy el hijo2 PID: %d     recibi la señal de terminar. Terminando..." % os.getpid())
    os._exit(0)
    args = 0
    os.wait()
    os.wait() 
    print("Padre PID %d Saliendo" % os.getpid())



if __name__ == "__main__":
    main()