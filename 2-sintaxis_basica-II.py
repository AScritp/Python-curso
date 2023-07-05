    #---Funciones DEF


def hola(a):
    print("Hola "+str(a)+"\n")
    

key=input("¿Comó te llamas?"+"\n"+">")
hola(key)

def loro(l):
    for i in range(l):
        print("\n"+"Hola")
        print("¿Comó estás?")
        print("adios"+"\n")

    return i

print("""Se ha depestado tu Loro. 
El que te saluda y despide al mismo tiempo."""+"\n")
key=int(input("¿Cuantas veces quieres que te hable?"+"\n"+">"))
loro(key)