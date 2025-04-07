PI = 3.1416

print("Ingrese Radio y Alto: ")
radio = float( input("Radio: "))
alto = float ( input("Alto: "))

vol = PI * radio**2 * alto
area = 2*PI*radio*(radio + alto)

print("Volumen:", vol)
print("área:", area)