def celsius_a_fahrenheit(grados_celsius):
    """calcula y retorna los grados fahrenheit con los grados celsius ingresado"""
    grados_fahrenheit = (grados_celsius * 9/5) + 32
    return grados_fahrenheit

celsius=int(input("ingresa los grados(fahrenheit): "))
r = round(celsius_a_fahrenheit(celsius),2)
print(f"{celsius} grados fahrenheit son {r} grados celsius")