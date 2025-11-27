diccionario={"maximo":max(lista)}
lista=[]
try:
    numero=int(input("ingresa numero entero para lalista:\n"))
    lista.append(numero)
except ValueError as e:
    print("dato invalido" ,e)