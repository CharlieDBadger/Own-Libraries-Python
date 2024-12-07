def generate_a():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == 0 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == 0):
                malla[y_ite].append('o')  # Esquinas
            elif x_ite == 0 or x_ite == x - 1:  # Bordes laterales de la "A"
                malla[y_ite].append('|')
            elif y_ite == 0 or y_ite == y / 2:
                malla[y_ite].append('-')  # Borde superior y division
            else:
                malla[y_ite].append(' ')  # Espacios internos de la "A"

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_b():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == y - 1 and x_ite == 0):
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == 0 and x_ite == x - 1:
                malla[y_ite].append('\\')  # Esquinas
            elif y_ite == y - 1 and x_ite == x - 1:
                malla[y_ite].append('/')  # Esquinas
            elif y_ite == y / 3 and x_ite == x - 2:
                malla[y_ite].append('<')  # Borde superior y division
            elif (x_ite == 0 or x_ite == x - 1) and \
                    (y_ite != y / 3):  # Bordes laterales de la "B"
                malla[y_ite].append('|')
            elif (y_ite == 0 or y_ite == y - 1) or \
                    (y_ite == y / 3 and x_ite != x - 1):
                malla[y_ite].append('-')  # Borde superior y division

            else:
                malla[y_ite].append(' ')  # Espacios internos de la "A"

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_c():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == 0 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == 0):
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == 0 or y_ite == y - 1:
                malla[y_ite].append('-')  # Bordes superior e inferior
            elif x_ite == 0:
                malla[y_ite].append('|')  # Bordes laterales
            else:
                malla[y_ite].append(' ')  # Espacios internos

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_d():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == y - 1 and x_ite == 0):
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == 1 and x_ite == x - 1:
                malla[y_ite].append('\\')  # Esquinas
            elif y_ite == y - 2 and x_ite == x - 1:
                malla[y_ite].append('/')  # Esquinas
            elif (x_ite == 0 or x_ite == x - 1) and \
                    (y_ite != y - 1 and y_ite != 0):  # Bordes laterales de la "D"
                malla[y_ite].append('|')
            elif (y_ite == 0 or y_ite == y - 1) and \
                    (x_ite != x - 1):
                malla[y_ite].append('-')  # Borde superior e inferior
            else:
                malla[y_ite].append(' ')  # Espacios internos de la "A"

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_e():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == 0 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == 0):
                malla[y_ite].append('o')  # Esquinas
            elif x_ite == 0 and y_ite != y / 3:  # Bordes laterales de la "B"
                malla[y_ite].append('|')
            elif (y_ite == 0 or y_ite == y - 1) or \
                    (y_ite == y / 3 and x_ite != x - 1):
                malla[y_ite].append('-')  # Borde superior y division

            else:
                malla[y_ite].append(' ')  # Espacios internos de la "A"

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_f():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == 0 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == 0):
                malla[y_ite].append('o')  # Esquinas
            elif x_ite == 0 and y_ite != y / 3:  # Bordes laterales de la "B"
                malla[y_ite].append('|')
            elif (y_ite == 0) or \
                    (y_ite == y / 3 and x_ite != x - 1):
                malla[y_ite].append('-')  # Borde superior y division

            else:
                malla[y_ite].append(' ')  # Espacios internos de la "A"

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_g():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == 0 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == 0):
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == 3 and x_ite == x - 1:
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == y - 2 and x_ite == x - 1:
                malla[y_ite].append('/')  # Esquinas
            elif (x_ite == 0) or \
                    (y_ite == 1 and x_ite == x - 1):  # Bordes laterales de la "D"
                malla[y_ite].append('|')
            elif (y_ite == 0 or y_ite == y - 1) and \
                    (x_ite != x - 1):
                malla[y_ite].append('-')  # Borde superior e inferior
            elif y_ite == 0 or y_ite == y / 2:
                malla[y_ite].append('-')  # Borde superior e inferior
            else:
                malla[y_ite].append(' ')  # Espacios internos de la "A"

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_h():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == 0 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == 0):
                malla[y_ite].append('o')  # Esquinas
            elif x_ite == 0 or x_ite == x - 1:  # Bordes laterales de la "A"
                malla[y_ite].append('|')
            elif y_ite == y / 2:
                malla[y_ite].append('-')  # Borde superior y division
            else:
                malla[y_ite].append(' ')  # Espacios internos de la "A"

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_i():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == 0 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == 0):
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == 0 or y_ite == y - 1:
                malla[y_ite].append('-')  # Bordes superior e inferior
            elif x_ite == x / 2:
                malla[y_ite].append('|')  # Bordes laterales
            else:
                malla[y_ite].append(' ')  # Espacios internos

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_j():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == 0 and x_ite == x - 1):
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == y - 2 and x_ite == 0:
                malla[y_ite].append('\\')  # Esquinas
            elif y_ite == y - 2 and x_ite == x - 1:
                malla[y_ite].append('/')  # Esquinas
            elif x_ite == x - 1 and y_ite != y - 1:
                malla[y_ite].append('|')  # Bordes laterales
            elif (y_ite == 0) or \
                    (y_ite == y - 1 and x_ite != 0) and \
                    (y_ite == y - 1 and x_ite != x - 1):
                malla[y_ite].append('-')  # Bordes superior e inferior
            else:
                malla[y_ite].append(' ')  # Espacios internos

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_k():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == 0 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == 0) or \
                    (x_ite == x - 1 and y_ite == y - 1):
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == y / 2 and x_ite == x - 1:
                malla[y_ite].append('\\')  # Esquinas
            elif y_ite == y / 3 and x_ite == x - 2:
                malla[y_ite].append('<')
            elif x_ite == 0 or \
                    x_ite == x - 1 and y_ite != y / 3:
                malla[y_ite].append('|')
            elif y_ite == y / 3 and x_ite != x - 1:
                malla[y_ite].append('-')  # Borde superior y division
            else:
                malla[y_ite].append(' ')  # Espacios internos de la "A"

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_l():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == y - 1 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == 0):
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == y - 1:
                malla[y_ite].append('-')  # Bordes superior e inferior
            elif x_ite == 0:
                malla[y_ite].append('|')  # Bordes laterales
            else:
                malla[y_ite].append(' ')  # Espacios internos

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_n():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == y - 1 and x_ite == 0) or \
                    (y_ite == y - 1 and x_ite == x - 1):
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == 1 and x_ite == x - 1:
                malla[y_ite].append('\\')  # Esquinas
            elif y_ite == 1 and x_ite == 0:
                malla[y_ite].append('/')  # Esquinas
            elif (x_ite == 0 or x_ite == x - 1) and \
                    (y_ite != 0):
                malla[y_ite].append('|')  # Bordes laterales
            elif (y_ite == 0 and x_ite != 0) and \
                    (y_ite == 0 and x_ite != x - 1):
                malla[y_ite].append('-')  # Bordes superior e inferior
            else:
                malla[y_ite].append(' ')  # Espacios internos

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_m():
    x = 10  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == y - 1 and x_ite == 0) or \
                    (y_ite == y - 1 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == x / 2):
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == 1 and x_ite == x - 1:
                malla[y_ite].append('\\')  # Esquinas
            elif y_ite == 1 and x_ite == 0:
                malla[y_ite].append('/')  # Esquinas
            elif (x_ite == 0 or x_ite == x - 1 or x_ite == x / 2) and \
                    (y_ite != 0):
                malla[y_ite].append('|')  # Bordes laterales
            elif (y_ite == 0 and x_ite != 0) and \
                    (y_ite == 0 and x_ite != x - 1):
                malla[y_ite].append('-')  # Bordes superior e inferior
            else:
                malla[y_ite].append(' ')  # Espacios internos

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_o():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == 0 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == 0):
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == 0 or y_ite == y - 1:
                malla[y_ite].append('-')  # Bordes superior e inferior
            elif x_ite == 0 or x_ite == x - 1:
                malla[y_ite].append('|')  # Bordes laterales
            else:
                malla[y_ite].append(' ')  # Espacios internos

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_p():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == 0 and x_ite == x - 1) or \
                    (y_ite == y / 3 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == 0):
                malla[y_ite].append('o')  # Esquinas
            elif (x_ite == 0 and y_ite != y / 3) or \
                    (x_ite == x - 1 and y_ite < y / 2):  # Bordes laterales de la "B"
                malla[y_ite].append('|')
            elif (y_ite == 0) or \
                    (y_ite == y / 3 and x_ite != x - 1):
                malla[y_ite].append('-')  # Borde superior y division

            else:
                malla[y_ite].append(' ')  # Espacios internos de la "A"

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_q():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == 0 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == 0):
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == y - 1 and x_ite == x / 2:
                malla[y_ite].append('\\')  # Esquinas
            elif y_ite == 0 or y_ite == y - 1:
                malla[y_ite].append('-')  # Bordes superior e inferior
            elif x_ite == 0 or x_ite == x - 1:
                malla[y_ite].append('|')  # Bordes laterales
            else:
                malla[y_ite].append(' ')  # Espacios internos

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_r():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == y - 1 and x_ite == 0) or \
                    (x_ite == x - 1 and y_ite == y - 1):
                malla[y_ite].append('o')  # Esquinas
            elif (y_ite == 0 and x_ite == x - 1) or \
                    y_ite == y / 2 and x_ite == x - 1:
                malla[y_ite].append('\\')  # Esquinas
            elif y_ite == y / 3 and x_ite == x - 2:
                malla[y_ite].append('<')
            elif x_ite == 0 or \
                    x_ite == x - 1 and y_ite != y / 3:
                malla[y_ite].append('|')
            elif (y_ite == 0) or \
                    (y_ite == y / 3 and x_ite != x - 1):
                malla[y_ite].append('-')  # Borde superior y division
            else:
                malla[y_ite].append(' ')  # Espacios internos de la "A"

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_s():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == 0 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == 0):
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == 0 or y_ite == y - 1 or y_ite == y / 3:
                malla[y_ite].append('-')  # Bordes superior e inferior
            elif (x_ite == 0 and y_ite < y / 2) or \
                    (x_ite == x - 1 and y_ite > y / 3):
                malla[y_ite].append('|')  # Bordes laterales
            else:
                malla[y_ite].append(' ')  # Espacios internos

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_t():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == 0 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == x / 2):
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == 0:
                malla[y_ite].append('-')  # Bordes superior e inferior
            elif x_ite == x / 2:
                malla[y_ite].append('|')  # Bordes laterales
            else:
                malla[y_ite].append(' ')  # Espacios internos

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_u():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == y - 1 and x_ite == 0) or \
                    (y_ite == y - 1 and x_ite == x - 1):
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == 0 and x_ite == x - 1:
                malla[y_ite].append('\\')  # Esquinas
            elif y_ite == 0 and x_ite == 0:
                malla[y_ite].append('/')  # Esquinas
            elif x_ite == 0 or x_ite == x - 1:
                malla[y_ite].append('|')  # Bordes laterales
            elif (y_ite == y - 1 and x_ite != 0) and \
                    (y_ite == y - 1 and x_ite != x - 1):
                malla[y_ite].append('-')  # Bordes superior e inferior
            else:
                malla[y_ite].append(' ')  # Espacios internos

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_v():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O
    i = -2
    j = -3
    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == 0 and x_ite == x - 1):
                malla[y_ite].append('o')  # Esquinas
            elif x_ite == j and y_ite > y / 3:
                malla[y_ite].append('\\')  # Bordes laterales
            elif x_ite == x - i and y_ite > y / 3:
                malla[y_ite].append('/')  # Bordes laterales
            elif y_ite < y / 2 and (x_ite == 0 or x_ite == x - 1):
                malla[y_ite].append('|')  # Bordes laterales
            else:
                malla[y_ite].append(' ')  # Espacios internos

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
        j += 1
        i += 1

    return malla


def generate_w():
    x = 10  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == y - 1 and x_ite == 0) or \
                    (y_ite == y - 1 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == x / 2):
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == 0 and x_ite == x - 1:
                malla[y_ite].append('\\')  # Esquinas
            elif y_ite == 0 and x_ite == 0:
                malla[y_ite].append('/')  # Esquinas
            elif (x_ite == 0 or x_ite == x - 1 or x_ite == x / 2) and \
                    (y_ite != 0):
                malla[y_ite].append('|')  # Bordes laterales
            elif (y_ite == y - 1 and x_ite != 0) and \
                    (y_ite == y - 1 and x_ite != x - 1):
                malla[y_ite].append('-')  # Bordes superior e inferior
            else:
                malla[y_ite].append(' ')  # Espacios internos

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_x():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O
    i = 1
    j = 0
    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == 0 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == 0):
                malla[y_ite].append('o')  # Esquinas
            elif x_ite == j:
                malla[y_ite].append('\\')  # Bordes laterales
            elif x_ite == x - i:
                malla[y_ite].append('/')  # Bordes laterales
            else:
                malla[y_ite].append(' ')  # Espacios internos

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
        j += 1
        i += 1

    return malla


def generate_y():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == y / 3 and (x_ite == 0 or x_ite == x - 1)) or \
                    ((y_ite == y - 1 or y_ite == y / 3) and x_ite == x / 2):
                malla[y_ite].append('o')  # Esquinas
            elif ((x_ite == 0 or x_ite == x - 1) and y_ite < y / 2) or \
                    (x_ite == x / 2 and y_ite > y / 3):  # Bordes laterales de la "A"
                malla[y_ite].append('|')
            elif y_ite == y / 3:
                malla[y_ite].append('-')  # Borde superior y division
            else:
                malla[y_ite].append(' ')  # Espacios internos de la "A"

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
    return malla


def generate_z():
    x = 6  # Ancho de la O
    y = 6  # Alto de la O
    i = 1

    # Crear una malla de {y} filas con el primer valor "_"
    malla = [[" "] for _ in range(y)]

    y_ite = 0  # Inicializar el índice de filas
    while y_ite < y:
        x_ite = 0  # Inicializar el índice de columnas
        while x_ite < x:
            if (y_ite == 0 and x_ite == 0) or \
                    (y_ite == 0 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == x - 1) or \
                    (y_ite == y - 1 and x_ite == 0):
                malla[y_ite].append('o')  # Esquinas
            elif y_ite == 0 or y_ite == y - 1 or y_ite == y / 3:
                malla[y_ite].append('-')  # Bordes superior e inferior
            elif x_ite == x - i:
                malla[y_ite].append('/')  # Bordes laterales
            else:
                malla[y_ite].append(' ')  # Espacios internos

            x_ite += 1  # Incrementar el índice de columnas

        y_ite += 1  # Incrementar el índice de filas
        i += 1
    return malla


def generate_space():
    malla = [["       "],
             ["       "],
             ["       "],
             ["       "],
             ["       "],
             ["       "]]

    return malla


def filtro_letras_espacios(cadena):
    resultado = []  # Lista para almacenar los caracteres que pasan el filtro

    # Recorrer cada carácter en la cadena
    for char in cadena:
        # Verificar si el carácter es una letra o un espacio
        if char.isalpha() or char == " ":
            # Convertir a minúscula si és letra
            resultado.append(char.lower())
        else:
            return False  # Si encuentra un carácter no válido, retorna False

    return ''.join(resultado)  # Devolver la cadena filtrada y convertida a minúsculas


def generar_texto_enmallado(texto_string):
    texto_enmallado_final = []

    for caracter in texto_string:
        match caracter:
            case "a":
                texto_enmallado_final.append(generate_a())
            case "b":
                texto_enmallado_final.append(generate_b())
            case "c":
                texto_enmallado_final.append(generate_c())
            case "d":
                texto_enmallado_final.append(generate_d())
            case "e":
                texto_enmallado_final.append(generate_e())
            case "f":
                texto_enmallado_final.append(generate_f())
            case "g":
                texto_enmallado_final.append(generate_g())
            case "h":
                texto_enmallado_final.append(generate_h())
            case "i":
                texto_enmallado_final.append(generate_i())
            case "j":
                texto_enmallado_final.append(generate_j())
            case "k":
                texto_enmallado_final.append(generate_k())
            case "l":
                texto_enmallado_final.append(generate_l())
            case "m":
                texto_enmallado_final.append(generate_m())
            case "n":
                texto_enmallado_final.append(generate_n())
            case "ñ":
                texto_enmallado_final.append(generate_n())
                texto_enmallado_final.append(generate_i())
            case "o":
                texto_enmallado_final.append(generate_o())
            case "p":
                texto_enmallado_final.append(generate_p())
            case "q":
                texto_enmallado_final.append(generate_q())
            case "r":
                texto_enmallado_final.append(generate_r())
            case "s":
                texto_enmallado_final.append(generate_s())
            case "t":
                texto_enmallado_final.append(generate_t())
            case "u":
                texto_enmallado_final.append(generate_u())
            case "v":
                texto_enmallado_final.append(generate_v())
            case "w":
                texto_enmallado_final.append(generate_w())
            case "x":
                texto_enmallado_final.append(generate_x())
            case "y":
                texto_enmallado_final.append(generate_y())
            case "z":
                texto_enmallado_final.append(generate_z())
            case " ":
                texto_enmallado_final.append(generate_space())  # Para los espacios

    return texto_enmallado_final


def imprimir_texto(texto_enmallado):
    # Imprimir cada letra en el texto
    for i in range(len(texto_enmallado[0])):  # Asumir que todas las letras tienen el mismo número de filas
        for letra in texto_enmallado:
            print(' '.join(letra[i]), end=' ')  # Imprimir la fila correspondiente
        print()  # Salto de línea después de cada fila


def generate_terminal_text():
    while True:  # Bucle infinito que se repetirá hasta que se rompa
        try:
            # Pedir al usuario una cadena de texto
            texto = input("Ingresa una palabra: ")

            # Filtrar el texto para que solo queden letras y espacios
            texto_filtrado = filtro_letras_espacios(texto)

            if texto_filtrado is False:
                print("La cadena contiene caracteres no válidos (solo se admites letras y espacios). "
                      "Inténtalo de nuevo.")
                continue  # Regresar al inicio del bucle para pedir otra entrada

            # Generar el texto enmallado a partir del texto filtrado
            texto_procesado = generar_texto_enmallado(texto_filtrado)

            # Imprimir el texto enmallado
            imprimir_texto(texto_procesado)

            break  # Salir del bucle si ha ido bien

        except Exception as e:
            print(f"Ocurrió un error: {e}. Inténtalo de nuevo.")


generate_terminal_text()
