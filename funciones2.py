apellido = input("Ingrese el apellido del jugador: ")
año = int(input("Ingrese el año de nacimiento: "))
alt = int(input("Ingrese la altura (en cm): "))
lista = [apellido, año, alt]
def validador(lista):
    if  lista[1] >= 2010:
        lista[1] = True
    else:
        lista[1] = False
    if lista[2] >= 180:
        lista[2] = True
    else:
        lista[2] = False
        return
sas = input("quiere entrar al codigo")
if sas == "si":
    validador(lista)