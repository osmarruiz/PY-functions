import math
def area_circulo(ra):
   """retorna el area de un circulo"""
   return round(math.pi * ra**2, 2)

radio=int(input("Ingrese el radio del circulo: "))
a=area_circulo(radio)
print(f"el area del circulo es: {a}")