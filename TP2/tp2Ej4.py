def calculadora_presupuesto():
    ingresos = float(input("Ingresa tus ingresos mensuales: $"))
    gastos = {}
    
    while True:
        categoria = input("Ingresa la categoría de gasto (o 'salir' para terminar): ")
        if categoria.lower() == "salir":
            break
        monto = float(input(f"Ingresa el monto de gasto para {categoria}: $"))
        gastos[categoria] = monto
    
    total_gastos = sum(gastos.values())
    saldo = ingresos - total_gastos
    
    print(f"\nTotal de ingresos: ${ingresos:.2f}")
    print(f"Total de gastos: ${total_gastos:.2f}")
    print(f"Saldo disponible: ${saldo:.2f}")
    
    print("\nDistribución de gastos por categoría:")
    for categoria, monto in gastos.items():
        porcentaje = (monto / total_gastos) * 100
        print(f"{categoria}: ${monto:.2f} ({porcentaje:.2f}%)")

calculadora_presupuesto()
