#Carlos Peña Gutiérrez 
#El triángulo me salió invertido miss, pero de ahí en fuera, sale bien 

n=int(input("Enter triangle height: "))
altura=1
renglon=1
print("*")

for altura in range(n-1):

    if altura<n:
        print("*"+("*")*renglon)
        altura=altura+1
        renglon=renglon+1


def main():
    #Escribe tu código debajo de esta línea
    pass


if __name__=='__main__':
    main()
