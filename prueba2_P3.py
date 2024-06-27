paises={}
for x in range(5):
    pais=input("Ingrese un pais :")
    capital=input("Ingrese capital del pais : ")
    paises[pais]=capital
nombre=input("Ingrese su nombre :")
pais_origen=input("Ingrese pais de procedencia :")
for pais, capital in paises.items():
    if pais==pais_origen:
        break
      
print("el turista",nombre,"viene del pais",pais,"y su capital es",capital)