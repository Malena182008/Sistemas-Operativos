A = int(input("Cuál es tu edad?: "))

if A <= 18:
    print("Eres menor de edad")
else:
    if A > 18 and A < 64:
        print("Eres un adulto")
    else:
        if A >= 65:
            print("Eres un adulto mayor")