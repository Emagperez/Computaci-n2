import argparse
import os



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--ruta", type = str, help = "pasar ruta del archivo",required = True)
    args = parser.parse_args()

    with open(args.ruta, "r") as texto2:
        x = sum(1 for line in texto2)
        lineas = texto2.readlines()
        r , w = os.pipe()
        r0 , w0 = os.pipe()
        pid_padre = os.getpid()
        pid = os.fork()
        for l in range(x):
            if pid:
                os.close(w)
                r = os.fdopen(r)
                texto = r.read()
                os.close(r0)
                w0 = os.fdopen(w0, "w")
                ppid = os.getpid()
                w0.write("{}".join(reversed(texto)))
                w0.flush()
                w0.close()
                os._exit(0)
        os.close(r)
        w = os.fdopen(w, "w")
        

        for x in texto2.readlines():
            w.write(1)
        w.close()
        os.close(w0)
        ro = os.fdopen(r0)
        
        while True:
            textto0 = r0.read()
            print(texto0)
        
        for i in range(x):
            os.wait()

        











if __name__ == "__main__":
    main()