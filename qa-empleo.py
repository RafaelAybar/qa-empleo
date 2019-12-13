import sys

paramsList = [sys.argv[1].strip(), sys.argv[2].strip(), sys.argv[3].strip(), sys.argv[4].strip(), sys.argv[5].strip(),
              sys.argv[6].strip(), sys.argv[7].strip(), sys.argv[8].strip()]


def menuinicial():
    print("Bienvenidos a qa-empleo, introduce el número para seleccionar una opción")


def calculamedia():
    total = 0
    media = 0
    # http://lineadecodigo.com/python/iterar-una-lista-en-python-con-indices/
    for a in range(1, len(paramsList)):
        total += paramsList[a]
    if total == 0:
        print("No hay datos suficientes")
    else:
        media = total / 7
    print("La puntuación media obtenida es: " + media)
    return media
