salir=True
maximo=0
lista=[]
while (salir):
    texto=input("Dime números para añadir a la lista y para salir escribe fin")
    if(texto=="fin"):
        salir= False
    else:
        
        numero=int(texto)
        lista.append(numero)
 
maximo=max(lista)

print(lista) 
print(maximo)       