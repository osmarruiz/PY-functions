def fahrenheit_a_celsius(grados_fahrenheit):
    grados_celsius = (grados_fahrenheit - 32) * 5/9
    return grados_celsius

fahrenheit=int(input("ingresa los grados(fahrenheit): "))
r = round(fahrenheit_a_celsius(fahrenheit),2)
print(f"{fahrenheit} grados fahrenheit son {r} grados celsius")