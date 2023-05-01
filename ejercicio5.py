def dias_en_año(año):
    if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        return 366  # El año es bisiesto, tiene 366 días
    else:
        return 365  # El año no es bisiesto, tiene 365 días

año = int(input("Ingresa el año que quieres calcular: "))
dias = dias_en_año(año)
print(f"El año {año} tiene {dias} días.")