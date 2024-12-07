def print_rectangle(x, y):
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            cord_x += 1
            print("X", end="")
        print()


def print_a():
    x = 6  # Ancho de la A
    y = 6  # Alto de la A
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "A"
            if cord_y == 1 or cord_y == (y // 2):  # Línea superior y línea media de la "A"
                print("*", end="")
            elif cord_x == 0 or cord_x == x - 1:  # Bordes laterales de la "A"
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la "A"
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_b():
    x = 7  # Ancho de la G
    y = 6  # Alto de la G
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "G"
            if cord_x == 0:  # Lado izquierdo de la G
                print("*", end="")
            elif cord_y == 1:  # Línea superior de la G
                print("*", end="")
            elif cord_y == (y // 2):  # Línea media de la G
                print("*", end="")
            elif cord_y == y and cord_x != x - 1:  # Línea inferior de la G, sin el borde derecho
                print("*", end="")
            elif cord_x == x - 1 and (cord_y != 1 and cord_y != (y // 2) and cord_y != y):  # Curvas de la G
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la G
            cord_x += 1
            print()  # Salto de línea al terminar cada fila


def print_c():
    x = 7  # Ancho de la C
    y = 6  # Alto de la C
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "C"
            if cord_y == 1 or cord_y == y:  # Líneas superior e inferior de la C
                print("*", end="")
            elif cord_x == 0:  # Lado izquierdo de la C
                print("*", end="")
            elif cord_y != 1 and cord_y != y and cord_x == x - 1:  # Espacios internos de la C
                print(" ", end="")
            else:
                print(" ", end="")  # Espacios internos de la C
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_d():
    height = 6
    width = 6

    for row in range(height):
        for col in range(width):
            if (col == 0) or \
                    (row == 0 and col < width - 1) or \
                    (row == height - 1 and col < width - 1) or \
                    (col == width - 1 and (row != 0 and row != height - 1)):
                print('*', end='')
            else:
                print(' ', end='')
        print()


def print_e():
    x = 7  # Ancho de la E
    y = 6  # Alto de la E
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "E"
            if cord_x == 0:  # Lado izquierdo de la E
                print("*", end="")
            elif cord_y == 1 or cord_y == (y // 2) or cord_y == y:  # Líneas superior, media y base de la E
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la E
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_f():
    x = 7  # Ancho de la F
    y = 6  # Alto de la F
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "F"
            if cord_x == 0:  # Lado izquierdo de la F
                print("*", end="")
            elif cord_y == 1 or cord_y == (y // 2):  # Líneas superior y media de la F
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la F
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_g():
    height = 6
    width = 6

    for row in range(height):
        for col in range(width):
            if (col == 0 and (row != 0 and row != height - 1 and row != height // 2)) or \
                    (row == 0 and col != 0 and col != width - 1) or \
                    (row == height - 1 and col != 0 and col != width - 1) or \
                    (row == height // 2 and col >= width // 2) or \
                    (col == width - 1 and row >= height // 2 and row != height - 1):
                print('*', end='')
            else:
                print(' ', end='')
        print()


def print_h():
    x = 6  # Ancho de la H
    y = 6  # Alto de la H
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "H"
            if cord_x == 0 or cord_x == x - 1:  # Bordes laterales de la H
                print("*", end="")
            elif cord_y == (y // 2):  # Línea media de la H
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la H
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_i():
    x = 5  # Ancho de la I
    y = 6  # Alto de la I
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "I"
            if cord_y == 1 or cord_y == y:  # Líneas superior e inferior de la I
                print("*", end="")
            elif cord_x == (x // 2):  # Lado central de la I
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la I
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_j():
    x = 8  # Ancho de la J
    y = 7  # Alto de la J
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "J"
            if cord_x == (x // 2) and cord_y < y - 1:  # Línea vertical de la "J"
                print("*", end="")
            elif cord_y == y - 1 and cord_x < (x // 2):  # Línea inferior de la "J"
                print("*", end="")
            elif cord_y == y - 1 and cord_x == (x // 2):  # Punto final de la "J"
                print("*", end="")
            elif cord_y == 1 and cord_x == 0:  # Parte superior de la curva de la "J"
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la "J"
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_k():
    x = 6  # Ancho de la K
    y = 6  # Alto de la K
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "K"
            if cord_x == 0:  # Línea vertical de la "K"
                print("*", end="")
            elif cord_y - cord_x == 2:  # Diagonal superior de la "K"
                print("*", end="")
            elif cord_y + cord_x == 5:  # Diagonal inferior de la "K"
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la "K"
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_l():
    x = 6  # Ancho de la L
    y = 6  # Alto de la L
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "L"
            if cord_x == 0:  # Línea vertical de la "L"
                print("*", end="")
            elif cord_y == y:  # Línea inferior de la "L"
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la "L"
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_m():
    x = 8  # Ancho de la M
    y = 6  # Alto de la M
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "M"
            if cord_x == 0 or cord_x == x - 1:  # Bordes laterales de la "M"
                print("*", end="")
            elif cord_x == cord_y and cord_x < x // 2:  # Parte izquierda de la "M"
                print("*", end="")
            elif cord_x == (x - cord_y - 1) and cord_x > x // 2:  # Parte derecha de la "M"
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la "M"
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_n():
    x = 6  # Ancho de la N
    y = 6  # Alto de la N
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "N"
            if cord_x == 0 or cord_x == (x - 1):  # Bordes verticales de la "N"
                print("*", end="")
            elif cord_x == cord_y:  # Diagonal de la "N"
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la "N"
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_enie():
    x = 6  # Ancho de la Ñ
    y = 6  # Alto de la Ñ
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "Ñ"
            if cord_x == 0 or cord_x == (x - 1):  # Bordes verticales de la "Ñ"
                print("*", end="")
            elif cord_x == cord_y:  # Diagonal de la "Ñ"
                print("*", end="")
            elif cord_y == 1 and (cord_x == 2 or cord_x == 3 or cord_x == 4):  # Tilde de la "Ñ"
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la "Ñ"
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_o():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "O"
            if cord_y == 1 or cord_y == y:  # Línea superior e inferior de la "O"
                print("*", end="")
            elif cord_x == 0 or cord_x == (x - 1):  # Bordes laterales de la "O"
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la "O"
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_p():
    x = 6  # Ancho de la P
    y = 6  # Alto de la P
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "P"
            if cord_x == 0:  # Borde izquierdo de la "P"
                print("*", end="")
            elif (cord_y == 1 or cord_y == (y // 2)):  # Líneas superior y media de la "P"
                print("*", end="")
            elif cord_x == x - 1 and cord_y < (y // 2):  # Borde derecho de la parte superior de la "P"
                print("*", end="")
            elif cord_x == 0 and cord_y > (y // 2):  # Borde izquierdo de la parte inferior de la "P"
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la "P"
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_q():
    x = 6  # Ancho de la Q
    y = 6  # Alto de la Q
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "Q"
            if cord_y == 1:  # Línea superior de la "Q"
                print("*", end="")
            elif cord_y == y:  # Línea inferior de la "Q"
                print("*", end="")
            elif cord_x == 0 or cord_x == (x - 1):  # Bordes laterales de la "Q"
                print("*", end="")
            elif cord_y == 2 and cord_x == 1:  # Espacio interno de la "Q"
                print(" ", end="")
            elif cord_y == 3 and cord_x == 1:  # Espacio interno de la "Q"
                print(" ", end="")
            elif cord_y == 4 and (cord_x == 1 or cord_x == 2):  # Parte diagonal de la "Q"
                print(" ", end="")
            elif cord_y == 5 and cord_x == 2:  # Cola de la "Q"
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la "Q"
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_r():
    x = 6  # Ancho de la R
    y = 6  # Alto de la R
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "R"
            if cord_y == 1 or cord_y == (y // 2):  # Línea superior y línea media de la "R"
                print("*", end="")
            elif cord_x == 0:  # Borde izquierdo de la "R"
                print("*", end="")
            elif cord_y < (y // 2) and cord_x == (x - 1):  # Línea diagonal de la "R"
                print("*", end="")
            elif cord_y > (y // 2) and cord_x == (x - 2):  # Borde en la parte inferior de la "R"
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la "R"
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_s():
    x = 6  # Ancho de la S
    y = 6  # Alto de la S
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "S"
            if (cord_y == 1) or (cord_y == (y // 2)) or (cord_y == y):  # Línea superior, media e inferior
                print("*", end="")
            elif (cord_y < (y // 2) and cord_x == 0) or (cord_y > (y // 2) and cord_x == x - 1):  # Bordes laterales
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la "S"
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_t():
    x = 6  # Ancho de la T
    y = 6  # Alto de la T
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "T"
            if cord_y == 1:  # Línea superior de la "T"
                print("*", end="")
            elif cord_x == (x // 2):  # Línea vertical de la "T"
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la "T"
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_w():
    x = 8  # Ancho de la W
    y = 6  # Alto de la W
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "W"
            if cord_x == 0 or cord_x == x - 1:  # Bordes laterales de la "W"
                print("*", end="")
            elif cord_y == x - cord_x - 1 and cord_x < x // 2:  # Parte izquierda de la "W"
                print("*", end="")
            elif cord_y == cord_x and cord_x > x // 2:  # Parte derecha de la "W"
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la "W"
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_x():
    x = 7  # Ancho de la X
    y = 6  # Alto de la X
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "X"
            if cord_x == cord_y or cord_x == (x - cord_y - 1):  # Diagonales de la "X"
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos de la "X"
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_y():
    x = 8  # Ancho de la Y
    y = 6  # Alto de la Y
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "Y"
            if cord_y < (y // 2):  # Parte superior de la "Y"
                if cord_x == cord_y or cord_x == (x - cord_y - 1):  # Brazos de la "Y"
                    print("*", end="")
                else:
                    print(" ", end="")  # Espacios internos
            else:  # Parte inferior de la "Y"
                if cord_x == (x // 2):  # Línea vertical de la "Y"
                    print("*", end="")
                else:
                    print(" ", end="")  # Espacios internos
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


def print_z():
    x = 6  # Ancho de la Z
    y = 6  # Alto de la Z
    cord_x = 0
    cord_y = 0

    while cord_y < y:
        cord_y += 1
        cord_x = 0
        while cord_x < x:
            # Condiciones para formar la "Z"
            if cord_y == 1 or cord_y == y:  # Líneas superior e inferior de la "Z"
                print("*", end="")
            elif cord_y == (y - cord_x - 1):  # Diagonal de la "Z"
                print("*", end="")
            else:
                print(" ", end="")  # Espacios internos
            cord_x += 1
        print()  # Salto de línea al terminar cada fila


'''
print_a()
print_b()
print_c()
print_d()
print_e()
print_f()
print_g()
print_h()
print_i()
print_j()
print_k()
print_l()
print_m()
print_n()
print_enie()
print_o()
print_p()
print_q()
print_r()
print_s()
print_t()
print_w()
print_x()
print_y()
print_z()
'''
print_b()