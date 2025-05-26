Sal = int(input("Ingrese el valor de su saldo: "))
mont = int(input("Ingrese un monto que quiera retirar:"))
restante = Sal - mont
if mont <= Sal:
    print("Usted quiere retirar ", mont, "tiene", restante, " saldo restante")
else:
    if Sal < mont:
        print("Fondos insuficientes")