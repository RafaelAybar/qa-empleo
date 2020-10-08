import sys


def calculamedia(paramsList):
    total = 0
    media = 0
    # http://lineadecodigo.com/python/iterar-una-lista-en-python-con-indices/
    for a in range(2, len(paramsList)):
        total = total + paramsList[a]
    if total == 0:
        print("No hay datos suficientes")
    else:
        media = total / 7
    print(f"La puntuación media obtenida es: {media}")
    return media


def ejecutar():
    # https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-python-3
    paramsList = [sys.argv[1].strip(), int(sys.argv[2].strip()), int(sys.argv[3].strip()), int(sys.argv[4].strip()), int(sys.argv[5].strip()),
                  int(sys.argv[6].strip()), int(sys.argv[7].strip()), int(sys.argv[8].strip())]

    nota = calculamedia(paramsList)
    estado = ""
    if nota <= 6:
        estado = "mal"
    elif 6 < nota < 10:
        estado = "bien"
    else:
        print("Debes introducir valores coherentes")
        exit(1)

    print(f"La oferta está {estado}")


if __name__ == '__main__':
    ejecutar()
