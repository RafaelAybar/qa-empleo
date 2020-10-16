"""Package Qa Empleo

Returns:
    estado: ['bien', 'mal']
"""
__version__ = "0.1"

import sys

from analizadorsintactico import AnalizadorSintactico


class Empresa:

    def __init__(self, params: dict) -> None:
        self.params = params

    def _calcula_media_notas(self) -> float:
        """
        _calcula_media_notas() toma las claves de cada nota, accede a los valores
        llamando al atributo (dict) 'params' (ignorando nombre_empresa) y calcula
        la media aritmética de las notas redondeada a 1 decimal.

        """
        suma = 0
        media = 0
        claves_notas = list(self.params.keys())
        claves_notas.remove('nombre_empresa')
        for clave_nota in claves_notas:
            suma += self.params[clave_nota]
        media = round(suma / 7, 1)
        return media

    def obtener_estado(self) -> None:
        """
        obtener_estado() toma la nota media e imprime por pantalla la clasificación 
        de dicha nota.

        """
        estado = ''
        nota_media = self._calcula_media_notas()
        if -10 <= nota_media <= 6:
            estado = 'mal'
        elif 6 < nota_media <= 10:
            estado = 'bien'
        else:
            estado = 'Debes introducir valores coherentes'
            sys.exit(estado)
        print(f'La puntuación media obtenida es: {nota_media}')
        print(f'La oferta está {estado}')


def ejecutar():
    params = AnalizadorSintactico.parsear_entrada()
    MiEmpresa = Empresa(params=params)
    MiEmpresa.obtener_estado()


if __name__ == '__main__':
    ejecutar()