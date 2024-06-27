lista=[]

for x in range(10):
    precio_producto=int(input("Ingrese precio del producto en USD "))
    lista.append(precio_producto)
multiplicador=950
for i in range(len(lista)):
    print("el dolar",lista[i]," fue convertido a",lista[i]*multiplicador,"CLP")