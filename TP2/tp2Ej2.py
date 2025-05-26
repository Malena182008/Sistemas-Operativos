def convunid():
    print("Conversor de unidades:")
    print("1. Libras a kilogramos")
    print("2. Kilómetros a millas")
    print("3. Grados Celsius a Fahrenheit")
    
    opcion = int(input("Elige la opción (1/2/3): "))
    
    if opcion == 1:
        libras = float(input("Ingresa el valor en libras: "))
        kilogramos = libras * 0.453592
        print(f"{libras} libras son {kilogramos:.2f} kilogramos.")
        
    elif opcion == 2:
        kilometros = float(input("Ingresa el valor en kilómetros: "))
        millas = kilometros * 0.621371
        print(f"{kilometros} kilómetros son {millas:.2f} millas.")
        
    elif opcion == 3:
        celsius = float(input("Ingresa el valor en grados Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit.")
    else:
        print("Opción no válida.")

convunid()
