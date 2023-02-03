## Conección via fast api a GRBL CNC 3 Axis router

- Este repo es una prueba para enviar codigo G en GRBL a placa controlador de SparkFun Stepoko. https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide?_ga=2.75854482.665198805.1675355316-438911775.1675355316
- La palaca controladora se conectacon flask api via pueerto USB. Se ejecuta comando GRBL para moverse en el eje x 10mm a la izquierda.
- Ejecutar con:
        Flask run