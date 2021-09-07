#Carlos Peña Gutiérrez A01661455

n=int(input("Enter a number: "))

a=0
b=1
inicial=1
suma=0

while inicial<=n:
 if n>=0:
    inicial+=1
    a=b
    b=suma
    suma=a+b
 else: 
     continue

print(suma)

def main():
    #escribe tu código abajo de esta línea
    pass

if __name__=='__main__':
    main()
