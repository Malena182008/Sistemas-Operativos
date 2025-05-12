Año = int(input("Ingrese año: "))

if(Año%400==0) or (Año%4==0) and (Año%100!=0):
    print("El año es Bisisesto")
else:
    print("El año no es Bisiesto")