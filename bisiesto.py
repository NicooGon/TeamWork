def calcular_antiguedad(sueldo_acordado, antiguedad):
    if antiguedad >= 20:
        return sueldo_acordado * 0.2
    else:
        return sueldo_acordado * (antiguedad / 100)
        
def calcular_seguro_retiro(sueldo_total):
    return sueldo_total * 0.11
    
def calcular_seguro_medico(sueldo_total):
    return sueldo_total * 0.06
    
def calcular_impuesto_ganancia(sueldo_total):
    if sueldo_total > 120000:
        return sueldo_total * 0.25
    elif sueldo_total > 70000:
        return sueldo_total * 0.2
    else:
        return 0
def calcular_sueldo_final(sueldo_acordado, antiguedad):
    sueldo_total = sueldo_acordado + calcular_antiguedad(sueldo_acordado, antiguedad)
    sueldo_total -= calcular_seguro_retiro(sueldo_total)
    sueldo_total -= calcular_seguro_medico(sueldo_total)
    sueldo_total -= calcular_impuesto_ganancia(sueldo_total)
    return sueldo_total
sueldo_acordado = float(input("Ingrese el sueldo acordado: "))
antiguedad = int(input("Ingrese los años de antigüedad: "))

sueldo_final = calcular_sueldo_final(sueldo_acordado, antiguedad)
print("El sueldo final del trabajador es:", sueldo_final)