#Queens Attack

print("Ingrese la longitud del tablero y la cantidad de obstáculos: (separado por un espacio)")
n, k = map(int, input().split(' '))     #   n: la longitud de los lados del tablero.  k: la cantidad de obstáculos.
print("Ingrese la fila y columna de la posición de la reina: (separado por un espacio)")
r_q, c_q = map(int, input().split(' ')) # r_q: la posicion de la fila de la reina.  c_q: la posición de la columna de la reina.

p = n - r_q   # p: parte superior.  
f = r_q - 1   # f: fondo.
d = n - c_q   # d: derecha.
i = c_q - 1   # i: izquierda.

# diagonales
p_i = min(n - r_q, c_q - 1)  # p_i: parte superior izquierda
p_d = n - max(c_q, r_q)      # p_d: parte superior derecha
f_i = min(r_q, c_q) - 1      # f_i: fondo izquierda
f_d = min(r_q - 1, n - c_q)  # f_d: fondo derecha

# Ciclo For para ingresar los obstáculos del tablero.
for i in range(k):
    print("Ingrese el obstáculo de la fila y de la columna: (separado por un espacio)")
    obst_r, obst_c = map(int, input().split(' ')) # obst_r: obstáculo de la fila.   obst_c: obstáculo de la columna. 
    
    # horizontal
    if obst_r == r_q:
        if obst_c > c_q:
            p = min(p, obst_c - c_q - 1)
        else:
            f = min(f, c_q - obst_c - 1)
    # vertical
    elif obst_c == c_q:
        if obst_r > r_q:
            d = min(d, obst_r - r_q - 1)
        else:
            i = min(i, r_q - obst_r - 1)
    # diagonales
    elif abs(obst_c - c_q) == abs(obst_r - r_q):
        # parte superior derecha
        if obst_c > c_q and obst_r > r_q:
            p_d = min(p_d, obst_c - c_q - 1)
        # fondo derecha
        elif obst_c > c_q and obst_r < r_q:
            f_d = min(f_d, obst_c - c_q - 1)
        # parte superior izquierda
        elif obst_c < c_q and obst_r > r_q:
            p_i = min(p_i, c_q - obst_c - 1)
        # fondo izquierda
        elif obst_c < c_q and obst_r < r_q:
            f_i = min(f_i, c_q - obst_c - 1)
    
# el número de cuadrados que la reina puede atacar desde su posición
print ("El numero de cuadrados que la reina puede atacar es:")
print (p + f + d + i + p_i + p_d + f_i + f_d)
