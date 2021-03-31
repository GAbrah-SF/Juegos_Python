contador = 0
discos = int(input("\nDame el número de discos: "))


def Torre_Hanoi(n, TorreA="A", TorreB="B", TorreC="C"):
    global contador
    if n > 0:
        Torre_Hanoi(n - 1, TorreA, TorreC, TorreB)
        contador += 1
        print(f"{contador}.- Mover el Disco {n} de la Torre {TorreA} a la Torre {TorreC}")
        Torre_Hanoi(n - 1, TorreB, TorreA, TorreC)


if __name__ == '__main__':
    Torre_Hanoi(discos)
    if discos <= 0:
        print("\nNO HAY DISCOS!!!")
    else:
        print(f"\nREALIZADO CON UN MÍNIMO DE {2 ** discos - 1} MOVIMIENTOS")