# Pokemon_api

## Tabla de contenido

- Descripción del proyecto
- Requisitos
- Instalación
- Rastreador de problemas
- Convenciones de código
- API
- Ejemplo/Ejecución de prueba
- Contribución
- Colaboradores
- Contacto
- Registro de cambios

### Descripción del proyecto

Este proyecto será un juego de adivinanzas de pokemon completamente automatizado.
Toda la información requerida para el juego se tomará de la API de Pokémon.
El programa comenzará preguntando al usuario si quiere jugar (input = str sí o no).
Si la respuesta es sí, que quieren jugar, entonces la primera ronda comenzará con ronda (ronda = 1).
El usuario estará adivinando "¿quién es ese pokemon?" (mientras quieren jugar) y obtener sucesivamente más y más pistas con cada suposición incorrecta hasta que no queden más pistas para dar (se contará con cada bucle y se darán pistas dependiendo del contador).
Acto seguido, después de que se hayan mostrado todas las pistas, el usuario tendrá 2 intentos restantes (si cuenta = x entonces el juego termina).
Después de que el usuario haya adivinado incorrectamente demasiadas veces, la ronda terminará y le preguntará al usuario si quiere continuar jugando o salir (entrada = salir o jugar).
Si el usuario decide continuar jugando, el contador de rondas aumentará (ronda += 1).

### Requisitos

- Python.
- módulo de solicitud.
- módulo aleatorio.

### Instalación

Pokemon_api se hizo con __Python 3.7+__. Puede descargar la última versión de Python [aquí] (https://www.python.org/downloads/).

Los tres paquetes (aleatorio, solicitudes y navegador web) se pueden instalar en su IDE (Entorno de desarrollador integrado).
Tenga en cuenta que cada IDE tiene una forma diferente de instalar paquetes.
De lo contrario, puede usar el símbolo del sistema y cambiar el directorio donde está instalado Python y en la carpeta de scripts, escriba `pip install request`, `pip install random` y `pip install webbrowser`

### Rastreador de problemas/Oportunidades de mejora

El programa actual no tiene una interfaz gráfica que hubiera sido preferible. En su lugar, utiliza los paquetes del navegador web para mostrar el sprite del pokemon. Esto es algo que se está desarrollando actualmente.

### Convenciones de código

**Organización de archivos:** El código está dividido en diferentes archivos, por orden de funciones, para facilitar la interacción y facilitar las contribuciones.

**Convención de nomenclatura:** Todos los archivos usan **snake_case** para la variable Nombres.

### API

![Pokémon_UML drawio (1)](https://user-images.githubusercontent.com/96413210/154050589-eab9e130-c8b2-4807-909c-2dabcf3277f5.png)

Todos los métodos devuelven una variable específica.

### Ejemplo/prueba

```powershell
Esto es "¡Adivina ese Pokémon!"


Round 1
Nombre: _ _ _ _ _ _ _ _ _      
Generacion: 3
Abilidad: ['enjambre', 'rivalidad']

Quien es ese pokemon: pikachu


Round 2
Nombre: B _ _ _ _ _ _ _ _ 
Generacion: 3
Abilidad: ['enjambre', 'rivalidad']
Type: ['bug', 'flying']
Index: 267
Previous guesses: ['pikachu']

quien es ese pokemon: beedrill

Round 3
Nombre: B _ _ _ _ _ _ _ _
Generacion: 3
Abilidad: ['enjambre', 'rivalidad']
Type: ['bug', 'flying']
Index: 267
Previous guesses: ['pikachu', 'beedrill']

Quien es ese pokemon: Beautifly
Así es, el pokémon era hermoso
Deseas seguir jugando: no

```







### Changelog

Patch 0: 24-02-2022.
The game is fully functioning. The next patch will contain a graphics update as well as better UI with different options buttons. 

## License

[MIT](https://choosealicense.com/licenses/mit/)
