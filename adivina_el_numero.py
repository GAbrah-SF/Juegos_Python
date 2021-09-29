import random


def run():
    contador = 0
    numero_aleatorio = random.randint(1, 100)
    contador += 1
    numero_elegido = int(input(f'\n{str(contador).zfill(2)}.- Elige un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            contador += 1
            print(f'{str(contador).zfill(2)}.- MÁS, ', end="")
        else:
            contador += 1
            print(f'{str(contador).zfill(2)}.- MENOS, ', end="")
        numero_elegido = int(input('Elige otro número: '))
    print(f'\n¡¡¡GANASTES!!!, El número es el {numero_aleatorio}.')


if __name__ == '__main__':
    run()