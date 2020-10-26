# qa-empleo

En este proyecto se medirá el índice de fiabilidad de una empresa y las ofertas de trabajo que publican.
El script de python procesará los datos introducidos de la siguiente manera y devolverá los siguientes mensajes:

`La oferta está mal` : Esto significa que **no es una empresa apta**

`La oferta está bien` : Esto significa que **si es una empresa apta**


```python3 qa_empleo.py nombre-de-la-empresa nota-tipo-contrato nota-ubicación-cliente nota-requerimientos-cliente nota-vacaciones nota-salario nota-horario nota-teletrabajo```

Ejemplo del script:
```python3 qa_empleo.py github 10 5 0 5 -10 0 10```

Parámetros a tener en cuenta:
* ### Rotación histórica de los empleados de la compañía
    * Fórmula para obtener la rotación histórica: `Exempleados*100/(Exempleados+EmpleadosActuales)` Se obtendrán datos de
        las empresas en linkedin vía api
    * Porcentajes:

        | Calificación | Porcentaje
        | :------: |  :------: |
        10 | Rotacion historica menor a 50%
        5 |  Rotacion historica **entre** 50% **y** 60%
        0 |  Rotacion historica **superior** a 60%

* ### Detalles de la oferta
    *   #### 1. Tipo de contrato

          | Calificación | Tipo de contrato
        | :------: |  :------: |
        10 | Indefinido
        5 |  Beca
        1 | Prácticas (FCT y similares)
        -10 | No especificado en la oferta

        El resto de contratos están por determinar

    *   #### 2. Ubicación del cliente respecto a su casa

        | Calificación | Tiempo
        | :------: |  :------: |
        10 | Tiempo desde la casa a ubicacion del cliente **menor** a  30 minutos
        5 |  Tiempo desde la casa a ubicacion del cliente  **entre** 30 minutos **y** 1 hora
        0 |  Tiempo desde la casa a ubicacion del cliente **superior** a 1 hora

    *   #### 3. Requerimientos del cliente

        | Calificación | Nivel de detalle
        | :------: |  :------: |
        10 | El cliente comunica con rotunda claridad lo qué necesita, las funciones y responsabilidades del empleado
        5 |  El cliente menciona con exactitud las herramientas con las que se trabaja
        0 |  El cliente no especifica nada en concreto

    *   #### 4. Vacaciones

        | Calificación | Días de vacaciones
        | :------: |  :------: |
        10 | Superior a lo establecido en el convenio
        5 | Exactamente lo que indica el convenio
        0 | Lo que indica el convenio pero obligando a usarlas en periodos especificos

    *   #### 5. Expectativas salariales
        | Calificación | Especificaciones del cliente
        | :------: |  :------: |
        10 | Sueldo por encima del mercado
        5 | Sueldo a nivel del mercado
        0 | Sueldo inferior a nivel del mercado
        -10 | No especificadas / subcontratado

    *   #### 6. Horario
        | Calificación | Tipo de horario
        | :------: |  :------: |
        10 | Jornada intensiva todo el año
        5 | Jornada intensiva en verano
        0 | Horario estándar de oficina todo el año

    *   #### 7. Teletrabajo (si tiene sentido en la categoría profesional de la oferta)
        | Calificación | Días de teletrabajo
        | :------: |  :------: |
        10 | Posibilidad de teletrabajo todos los días
        5 | Posibilidad de teletrabajo más de un día a la semana
        0 | Nada de teletrabajo

## Agradecimientos

* Empaquetado: [Iago Alonso (@ibLeDy)](https://github.com/ibLeDy)
* Refactorización de Código: [Víctor Yelicich (@vmyelicich)](https://github.com/vmyelicich)
