# qa-empleo
En este proyecto se medirá el índice de fiabilidad de una empresa y las ofertas de trabajo que publican.
El script de python procesará los datos introducdos de la siguiente manera y devolverá un mensaje indicando si la empresa
es apta o no:

```python3 nombre-de-la-empresa 10 5 0 5 -10 0 10```

Parámetros a tener en cuenta:
* ### Rotación histórica de los empleados de la compañía
    * Fórmula para obtener la rotación histórica: `Exempleados*100/(Exempleados+EmpleadosActuales)` Se obtendrán datos de
        las empresas en linkedin vía api
    * Porcentajes:
        
        | Calificación | Porcentaje 
        | :------: |  :------: |
        10 | < 50%
        5 |  50% < x >= 60%
        0 |  > 60%
        
* ### Detalles de la oferta
    *   #### 1. Tipo de contrato
    
          | Calificación | Tipo de contrato 
        | :------: |  :------: |
        10 | Indefinido
        5 |  Beca
        1 | Prácticas (FCT y similares)
        -10 | No especificado en la oferta
        
        El resto de contratos están por determinar
        
    *   #### 2. Ubicación del cliente
        
        | Calificación | Tiempo
        | :------: |  :------: |
        10 | < 30 min
        5 |  30 min < x >= 60 min
        0 |  > 60 min
        
    *   #### 3. Requerimientos del cliente
    
        | Calificación | Nivel de detalle
        | :------: |  :------: |
        10 | El cliente comunica con rotunda claridad qué necesita y las funciones y responsabilidades del empleado
        5 |  El cliente meniciona con exactitud las herramientas con las que se trabaja
        0 |  El cliente no especifica nada en concreto
           
    *   #### 4. Vacaciones
    
        | Calificación | Días de vacaciones
        | :------: |  :------: |
        10 | Superior a lo establecido en el convenio
        5 | Exactamente lo que indica el convenio 
        0 | Lo que indica el conveio pero obligando a  cogerlos en periodos concretos
        
    *   #### 5. Espectativas salariales
        | Calificación | Especificaciones del cliente
        | :------: |  :------: |
        10 | Sueldo por encima de mercado
        5 | Sueldo a nivel de mercado 
        0 | Sueldo inferior a nivel de mercado
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
