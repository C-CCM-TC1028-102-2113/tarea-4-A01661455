#Carlos Peña Gutiérrez A01661455

n=0
suma=0 
cuenta=0
total=0

while n>=0:
 n=float(input())
 if n>0:
    suma=suma+n
    cuenta=cuenta+1
 elif n<0:
    prom= suma/cuenta
    print(prom)
   
def main():
    #escribe tu código abajo de esta línea
    pass
if __name__=='__main__':
    main()
