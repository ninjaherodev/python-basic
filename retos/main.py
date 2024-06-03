def calcular_promedio(enero, febrero, marzo):
    promedio = round((enero + febrero + marzo) / 3,2)
    return promedio

print(calcular_promedio(100,900,300))


mes1 = int(input('¿Cual es el presupuesto de Enero?'))
mes2 = int(input('¿Cual es el presupuesto de Febrero?'))
mes3 = int(input('¿Cual es el presupuesto de Marzo?'))

prom = calcular_promedio(mes1,mes2,mes3)
print(f"promedio calculado fue {prom} de Enero {mes1}, Febrero {mes2} y Marzo {mes3}")


