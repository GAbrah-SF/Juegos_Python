def free(fila, columna, n):
    """ Determina si la casilla (fila)(columna) está libre de ataques.
        @param fila: Fila
        @param columna: Columna
        @return: True si la casilla está libre de ataques por otras reinas.
    """
    for i in range(n):
        if tablero[fila][i] == "[Q]" or tablero[i][columna] == "[Q]":
            return False

    if fila <= columna:
        c = columna - fila
        f = 0
    else:
        f = fila - columna
        c = 0
    while c < n and f < n:
        if tablero[f][c] == "[Q]":
            return False
        f += 1
        c += 1

    if fila <= columna:
        f = 0
        c = columna + fila
        if c > n - 1:
            f = c - (n - 1)
            c = n - 1
    else:
        c = n - 1
        f = fila - ((n - 1) - columna)

    while c >= 0 and f < n:
        if tablero[f][c] == "[Q]":
            return False
        f += 1
        c -= 1

    return True


def agregar_reina(n, m):
    """ Agrega n reinas al tablero.
        @param: n El número de reinas a agregar
        @return True si se pudo agregar las reinas requeridas
    """
    if m < 1:
        return True

    for idx_fila in range(n):
        for idx_columna in range(n):
            if free(idx_fila, idx_columna, n):
                tablero[idx_fila][idx_columna] = "[Q]"
                if agregar_reina(n, m - 1):
                    return True
                else:
                    tablero[idx_fila][idx_columna] = "[ ]"

    return False


n = int(input("Dame el número de Reinas a agregar: "))
m = n
tablero = []
for i in range(n):
    tablero.append(["[ ]"] * n)
agregar_reina(n, m)
for fila in tablero:
    print(*fila)


if __name__ == '__main__':
    agregar_reina(n, m)
