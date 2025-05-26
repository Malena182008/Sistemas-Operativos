Vel = int(input("Cuál es la velocidad de su vehiculo?: "))

if Vel <= 60:
    print("Está dentro del límite de velocidad permitida")
else:
    if Vel > 61 and Vel < 80:
        print("Está en exceso leve")
    else:
        if Vel >= 80:
            print("Está en exceso grave")