from modules import Irasas

zurnalas = []

while True:
    pasirinkimas = int(input("1 - Ivesti pajamas\n2 - Ivesti islaidas\n3 - Atvaizduoti zurnala\n0 - Iseiti\n"))
    match pasirinkimas:
        case 1:
            suma = int(input("Iveskite suma: "))
            irasas = Irasas(suma, "Pajamos")
            zurnalas.append(irasas)
        case 2:
            suma = int(input("Iveskite suma: "))
            irasas = Irasas(suma, "Islaidos")
            zurnalas.append(irasas)
        case 3:
            print(zurnalas)
        case 0:
            print("Viso gero")
            break
