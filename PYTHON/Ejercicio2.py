#cadena=input("Dime la cadena de la cual quieres que cuente las letra")


def contarLetra():
    rutaFichero=input("Dime la ruta del fichero ")
    letra=input("Ahora dime la letra la cual quieres buscar")
    num=0
    fichero=open(rutaFichero,"r")
    contenido=fichero.read()
    contenido=contenido.lower()
    for c in contenido:
        if(c==letra):
            num+=1

    fichero.close()
    print("El número de veces que aparece la letra "+ letra+ " es de: "+ str(num))

def contarLetra2(vocal,rutaFichero):
    
    #letra=input("Ahora dime la letra la cual quieres buscar")
    num=0
    fichero=open(rutaFichero,"r")
    contenido=fichero.read()
    contenido=contenido.lower()
    for c in contenido:
        if(c==vocal):
            num+=1

    fichero.close()
    print("El número de veces que aparece la letra "+ vocal+ " es de: "+ str(num))

def contarVocales():
    rutaFichero=input("Dime la ruta del fichero ")
    a=0
    e=0 
    i=0
    o=0
    u=0
    fichero=open(rutaFichero,"r")
    contenido=fichero.read()
    contenido=contenido.lower()
    for c in contenido:
        if(c=='a'):
            a+=1
        elif(c=='e'):
            e+=1
        elif(c=='i'):
            i+=1
        elif(c=='o'):
            o+=1
        elif(c=='u'):
            u+=1

    fichero.close()
    print(f"La vocal a : {a} La vocal e :  {e} La vocal i: {i} \nla vocal o: {o} La vocal u: {u}")

vocales="aeiou"
rutaFichero=input("Dime la ruta del fichero ")
for vocal in vocales:
    contarLetra2(vocal,rutaFichero)