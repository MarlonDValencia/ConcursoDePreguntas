# ConcursoDePreguntas
Repositorio para modelar el reto del concurso de preguntas (SOFKA)

Para modelar el proyecto se usaron conceptos de OOP (Programación orientada a objetos), como clases, instancias, referencias a la instancia actual, métodos, atributos, etc..., el código está escrito en su totalidad en Python3.

## Ejecución
Para ejecutar el programa se debe tener instalado python3, posteriormente de asegurarse que tiene instalado Python3 en su equipo, abrir el ejecutable Jugar.bat e ingresar la opción correspondiente a la acción que quiere realizar (asegurarse de usar valores enteros).

La carpeta del proyecto cuenta con 7 elementos (5 Carpetas y dos archivos).

Para insertar la opción elegido se debe poner el número y presionar la tecla Enter.

## Pantalla Inicial
En la primera pantalla verás tres opciones: 
1. Crear un nuevo usuario: Luego de validar que no existe otro jugador con el nombre ingresado. crea un nuevo usuario con el nombre que ingreses.
2. Ingresar con un nuevo usuario: Iniciar sesión con un jugador que ya esté registrado en la base de datos
3. Ver la lista de ganadores: Despliega por pantalla los usuarios que han ganado y el número de veces que hayan ganado
0. Salir: Cierra el programa

## Carpetas
La carpeta inProgress contiene los juegos sin terminar de los usuarios que hayan guardado su progreso en medio de la partida.

La carpeta Questions contiene el banco de preguntas y sus respuestas(tres incorrectas y una correcta).

La carpeta src contiene el código fuente y todas las clases empleadas.

La carpeta users contiene la base de datos de usuarios registrados.

La carpeta winners contiene la base de datos de los jugadores que hayan terminado el juego en sus 5 rondas.

## Archivos
El archivo Jugar.bat es el ejecutable que inicia el juego y muestra por pantalla el desarrollo de la partida dependiendo de las opciones seleccionadas por el usuario.

El archivo main.py es el archivo que contiene la pantalla inicial del juego (No abrir para jugar, abrir el archivo Jugar.bat).

## Código Fuente
El código fuente cuenta con comentarios en todas las funciones definidas para dejar claro qué acción realizan.
