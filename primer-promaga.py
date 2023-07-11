def mylist():
    content=["Miguel","Alejandro","Jose","Jesus","Luis"]
    return content

def mylist2(l):
    print(l)

def comprobar():
    key=input(">")
    if key.isdigit():
        var=int(key)
        return var
    else:
        print("""Se ha producido un error.
        Debe ingresar uno de los valores mostrados""")

def add(l):
    l
    print("La lista actual es:"+"\n"+str(l))
    key=input("Escriba el nombre que deseas registrar"+"\n"+"> ")
    
    l.append(key)
    print(l[:])

  
a=True
while a==True:
    print("\n"+"Bienvenido a la interfaz de usuario."+"\n"+"¿Que desea hacer?")
    print("""
    1) Mostrar lista de usuarios
    2) Registrar solo un usuario
    3) Registrar varios usuarios

    
     
    4) Salir
    """)
    mylist()
    key=comprobar()

    if key==1:
        mylist2(mylist())
    elif key==2:
        add(mylist())
    elif key==3:
        break