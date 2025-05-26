A = int(input("Ingrese un numero del 1 al 7, teniendo en cuenta que 1 es Lunes y 7 es Domingo: "))
if A > 1 and A < 5:
    print("Es un día laboral")
else:
    if A > 6 and A < 7:
        print("Es fin de semana")