import math
def area_circulo(ra):
   return round(math.pi * ra**2, 25)

radio=int(input("Ingrese el radio del circulo: "))
a=area_circulo(radio)
print(f"el area del circulo es: {a}")