    #---Listas
List=["Miguel","Andrea","Milagro","Luis"]

key=int(input("Escribre un numero"+"\n"+">"))
print(List[key])

print("\n"+"Estos son todos los nombres de la lista")
print (List[:])

#.append(""); sirve para agregrar un valor a nuestra lista sin
 #necesidad de parametros

#.insert(int,str); sirve para agregrar un valor a nuestra lista con
 #parametros, el primero el numero del indice y el segundo
 #el valor que queremos a agregar
 
#.extend([""]); sirve para agregrar una gran cantidad de valores
 #basicamente concatena nuestra lista con otra que le
 #agregramos.

#.index(""); sirve para consultar la posición/indice
 # en el que se encuentra el valor que consultamos


#in; función que sirve para consultar si existe un valor
 #en nuestra lista con True (sí está) o Fasle (no está).
  #E.j: print("Miguel" in List)

#.remove(); sirve para eliminar valores de una lista

#.pop(); elimina el ultimo elemento de la lista