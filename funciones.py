def validador(lista):
    ap = input("Escriba su apellido: ")
    año = int(input("Escriba su año de nacimiento: "))
    alt = int(input("Escriba su altura en centimetros: "))
    if año > 2010:
        año = "verdadero"
    else:
        año = "falso"
    if alt > 180:
        alt = "verdadero"
    else:
        alt= "falso"
    lista = [ap, año, alt]