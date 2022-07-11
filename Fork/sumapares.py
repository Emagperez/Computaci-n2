import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n","--numero",type=int, help = "escriba -n y numero de procesos que quiere crear", required = True)
    parser.add_argument("-v","--verboso", help = "-v activa el modo verboso", action = "store_true")
    args = parser.parse_args()
    procesos(args.numero,args.verboso)
    
def suma(pid):
    sumas = 0
    for i in range(pid):
        if i % 2 == 0:
            sumas = sumas + i
    return sumas
def procesos(numero,verboso):
    for i in range(numero):
       if(os.fork() == 0):
        padre_pid = os.getpid()
        if verboso is True:
            print("\nStarting process", os.getpid())
            print("\nEnding process", os.getpid())
            print("\n", os.getpid, " - ", os.getppid(), ": ", suma(os.getpid()))
        else:
            print("\n", os.getpid(), " - ", os.getppid(), " : ", suma(os.getpid()))
            
        os._exit(0)
    os.wait
    
if __name__=="__main__":
    main()