import math

def logaritmo_en_base(b, x):
    """calcula el logaritmo"""
    return math.log(x, b)

b = float(input("Ingresa la base del logaritmo: "))
x = float(input("Ingresa el valor para el cual deseas calcular el logaritmo: "))

if b <= 0 or b == 1:
    print("Error: La base debe ser un número positivo distinto de 1.")
elif x <= 0:
    print("Error: El valor para el cual se desea calcular el logaritmo debe ser un numero positivo.")
else:
    resultado = logaritmo_en_base(b, x)
    print(f"El logaritmo en base {b} de {x} es {resultado}.")