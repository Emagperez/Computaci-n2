import getopt
import sys

(opt,arg)=getopt.getopt(sys.argv[1:],'o:n:m:')

for o, a in opt:
    if o == "-o":
        op = a
    elif o == "-n":
       primer = int(a)
    elif o == "-m":
        segundo = int(a)
    else:
        print("Error")

print(eval(str(primer) + op + str(segundo)))