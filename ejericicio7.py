def calcular_producto(a, b):
    """calcula el producto"""
    if a > b or a == 0 or b == 0:
        return 0
    else:
        producto = 1
        for i in range(a, b+1):
            producto *= i
        return producto

a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))

resultado = calcular_producto(a, b)

if resultado == 0:
    print("El producto no se puede calcular porque a es mayor que b o porque a o b es igual a cero.")
else:
    print(f"El producto de los números enteros desde {a} hasta {b} es {resultado}.")