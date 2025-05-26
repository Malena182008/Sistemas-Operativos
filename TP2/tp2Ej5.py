import random
import string

def generar_contraseña():
    longitud = int(input("Ingresa la longitud de la contraseña: "))
    incluir_simbolos = input("¿Deseas incluir símbolos? (sí/no): ").lower() == "sí"
    
    caracteres = string.ascii_letters + string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    print(f"Contraseña generada: {contraseña}")

generar_contraseña()
