    #---Operaciones
#->suma
suma=6+5
print(suma,"\n")

#->resta
resta=9-2
print(resta,"\n")

#->division
div=10/2
print(div,"\n")

#->modulo (es el resto de una división)
mod=10%2
print(mod,"\n")

#->potencia
pont=5**3
print(pont,"\n")

#->división absoluta (resultado sin de)

#---Tipos de objetos
#->numero
num=5
a=type(num)
print(a,"\n")

#->numero con decimales
num=5.2
a=type(num)
print(a,"\n")

#->Texto
num="Miguel"
a=type(num)
print(a,"\n")

#->Texto de 3 comillas
num="""

Esto es un mensaje
de tres comillas
:)

"""
print(num,"\n")
a=type(num)
print(a,"\n")

    #---Condicionales 
num1=7
num2=20

if num1>num2:
    print (str(num1)+" es mayor que "+str(num2))
else:
    print (str(num1)+" no es mayor que "+str(num2))