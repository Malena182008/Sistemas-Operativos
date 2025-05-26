def calcularprop():
    cuentatot = float(input("Ingresa el total de la cuenta: $"))
    propinatot = float(input("Ingresa el porcentaje de propina: "))
    
    propina = (cuentatot * propinatot) / 100
    totalpagar = cuentatot + propina
    
    print(f"La propina es: ${propina:.2f}")
    print(f"El total a pagar, incluyendo propina, es: ${totalpagar:.2f}")

calcularprop()
