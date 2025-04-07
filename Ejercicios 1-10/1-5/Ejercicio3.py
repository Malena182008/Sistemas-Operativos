print("Ingrese numero de respuestas correctas: ")
RC = int(input())
print("Ingrese numero de respuestas incorrectas: ")
RI = int(input())
print("Ingrese numero de respuestas en blanco: ")
RB = int(input())

PCR = RC*3
PRI = RI*3
PRB = RB*0
PF = PCR+PRI+PRB

print("El puntaje total es:", PF)