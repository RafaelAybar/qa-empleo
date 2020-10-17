"""Package Qa Empleo

Returns:
    estado: ['bien', 'mal']
"""
__version__ = "0.1"

import sys
import matplotlib.pyplot as plt
import numpy as np

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
    
    def grafico_radar(self):
    
        labels=['Tipo contrato', 'Ubicación cliente', 'Requerimientos cliente', 'Vacaciones', 'Salario', 'Horario', 'Teletrabajo']
        markers = [0, 2.5, 5, 7.5, 10]
        claves_notas = list(self.params.keys())
        claves_notas.remove('nombre_empresa')
        stats=[]
        for clave_nota in claves_notas:
            stats.append(self.params[clave_nota])

        angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
        stats = np.concatenate((stats,[stats[0]]))
        angles = np.concatenate((angles,[angles[0]]))

        fig= plt.figure()
        ax = fig.add_subplot(111, polar=True)
        ax.plot(angles, stats, 'o-', linewidth=2)
        ax.fill(angles, stats, alpha=0.25)
        ax.set_thetagrids(angles * 180/np.pi, labels, color='dimgray')
        plt.yticks(markers)
        ax.grid(True)
        ax . set_ylim (0, 10)
        for label, angle in zip(ax.get_xticklabels(), angles):
            if angle in (0, np.pi/2):
                label.set_horizontalalignment('left')
            elif np.pi/4 < angle < np.pi/2:
                label.set_horizontalalignment('left')
            elif np.pi/2 < angle < 5*np.pi/6:
                label.set_horizontalalignment('center')
            elif 5*np.pi/3 < angle < 2*np.pi:
                label.set_horizontalalignment('left')
            else:
                label.set_horizontalalignment('right')
            ax.set_title('{}'.format(self.params['nombre_empresa']),y=1.08, size=15,color='Black',)
        return plt.show()


def ejecutar():
    params = AnalizadorSintactico.parsear_entrada()
    MiEmpresa = Empresa(params=params)
    MiEmpresa.obtener_estado()
    MiEmpresa.grafico_radar()


if __name__ == '__main__':
    ejecutar()