import argparse

class AnalizadorSintactico(argparse.ArgumentParser):

    @classmethod
    def parsear_entrada(cls) -> dict:
        """
        parsear_entrada() recibe los parámetros de la línea de comandos, realiza el análisis
        sintáctico de cada entrada (en función del tipo y alternativas de valores) y retorna 
        un diccionario con sus valores.

        """
        parser = cls(prog='qa-empleo', add_help=False)
        parser.add_argument('nombre_empresa', type=str)
        parser.add_argument('nota_tipo_contrato', type=int, choices=[-10, 1, 5, 10])
        parser.add_argument('nota_ubicacion_cliente', type=int, choices=[0, 5, 10])
        parser.add_argument('nota_requerimientos_cliente', type=int, choices=[0, 5, 10])
        parser.add_argument('nota_vacaciones', type=int, choices=[0, 5, 10])
        parser.add_argument('nota_salario', type=int, choices=[-10, 0, 5, 10])
        parser.add_argument('nota_horario', type=int, choices=[0, 5, 10])
        parser.add_argument('nota_teletrabajo', type=int, choices=[0, 5, 10])
        entrada = vars(parser.parse_args())
        return entrada