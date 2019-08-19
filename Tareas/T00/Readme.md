# Tarea 0: LegoSweeper 

## Consideraciones generales :octocat:

* El juego funciona en su mayoria, al comenzar la partida se crean 2 tableros, uno con la informacion de los Legos y el otro que es el que se le muestra al usuario. 

* A veces cuando pierdes la partida en la primera baldosa que tratas de descubrir hay un bug que te pide de nuevo coordenadas para descubrir una baldosa, pero me sucedio solo 2 veces de todas las simulaciones que hice.

* En el menu de juego te permite volver al menu principal, esto sin guardar la partida.

* No implemente los mecanismos de guardar y cargar partida

* Al terminar una partida los puntajes se guardan de la siguiente forma: 'Usuario, Puntaje: X'

* En el codigo veran que tengo otras librerias implementadas como ```os``` y ```sys``` pero al no implementar las funciones de cargar y guardar partida no las utilice

### Cosas implementadas y no implementadas :white_check_mark: :x:


* Parte Menu Principal: Me faltó hacer la funcionalidad de cargar partida
    * Parte Crear Partida: Hecha completa 
    * Parte Cargar Partida: No hecha
    * Parte Ver Rankings: Hecha completa
    * Parte Salir: Hecha completa

* Parte Menu Juego: Me faltó hacer la funcionalidad de guardar partida
    * Parte Descubrir Baldosa: Hecha completa
    * Parte Guardar Partida: No hecha
    * Parte Salir de la Partida: Me faltó hacer que se le pregunte al usuario si quiere guardar o no la partida antes de salir.

* Bonus: No realizado


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  game.py

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random``` -> ```randrange()```
2. ```math``` -> ```ceil()``` 

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:

1. https://stackoverflow.com/questions/17555218/python-how-to-sort-a-list-of-lists-by-the-fourth-element-in-each-list
este codigo permite ordenar listas de listas en funcion de uno de los elementos contenidos dentro de la lista de listas y esta implementado en el archivo game.py en la linea 331 y ordena de mayor a menor la lista de listas de todos los puntajes del archivo puntajes.txt en funcion del puntaje que es el 3er elemento de la lista en las listas contenida dentro de la lista de listas
