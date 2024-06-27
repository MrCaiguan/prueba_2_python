lista=[]
suma=0
cont=0
nota=float(input("Ingrese nota  (0 para finalizar) :"))
while nota!=0:
    lista.append(nota)
    suma=suma+nota 
    nota=float(input("ingrese valor (0 para finalizar) : "))
    
valores=len(lista)    
promedio=suma/valores
print(len(lista))
print(promedio)
print(min(lista))
print(max(lista))