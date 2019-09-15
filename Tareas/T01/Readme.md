# Tarea 1: INICIAL P    

## Consideraciones generales :octocat:

* Considere que cuando alguien quiere salir de una partida y no ha guardado la partida, el juego le va a preguntar si es que quiere guardar y salir o salir sin guardar.

* Como en ningun lado aparecia algo sobre le dinero inicial de un piloto, decidi darles un dinero inicial de $500

* En mi juego, no alcance a implementar nada del flujo de la carrera, osea lo unico que uno puede hacer es crear un nuevo piloto junto con su vehiculo o cargar una partida, luego en el Menu Principal se puede ir hacia el menu de preparacion, escoger un vehiculo y una pista y entrar en el menu de carrera que lo unico que hace es acceder directamente al menu de los pits el cual solo imprime las opciones en la pantalla pero no fueron implementadas ninguna de las opciones. Por otro lado esta implementado el poder comprar nuevos vehiculos, y guardar partida.

* Implemente el bonus de buenas practicas en su totalidad, en los modulos menus1 a menus3 y en el modulo funciones

* Para guardar y cargar las partidas se generaba un diccionario basado en la primera linea de los archivos .csv dado que en estos se encontraba el orden de los atributos de las entidades y asi era posible mantener el orden sin importar cual fuese.

* De nervioso por hacer el ultimo push se paso que cuando uno entra al menu Carrera luego de haber seleccionado la pista y el vehiculo a utilizar en la carrera, el codigo entra en un while True del cual nunca va a salir, lo unico que hace es enviar a uno al menu de los pits

* Todas las clases abstractas se encuentran en el modulo abstracts y todos los otros modulos importan este para poder generar las clases de las entidades utilizadas en el programa y que heredan de sus clases madres que son abstractas

* En el modulo pista se encuentra la multiherencia con la clase PistaSuprema que hereda de PistaHielo y PistaRocosa

* Utilize relaciones de agregacion entre las entidades Piloto y Vehiculo, en que un Piloto tiene como atributo una lista llamada vehiculos que contiene todos los vehiculos que le pertenecen. Tambien entre las entidades Contrincantes y Pista, ya que cada pista tiene una lista de todos los Contrincantes que participan en esa pista.

* El codigo para cargar las partidas se encuentra en el modulo ```menus1.py``` en las lineas 220-309

* El modulo parametros es importado los modulos abstracts, funciones, menus1, menus2 y menus3

### Cosas implementadas y no implementadas :white_check_mark: :x:

* Parte Menus: Me falto implementar funcionalidades en los menus: Menu Pits y Menu Carrera
    * Parte Menu Carrera : Me falto hacer todo, lo unico que hace este menu es enviarte al menu Pits en un loop infinito 
    * Parte Menu Pits: En esta parte se imprime el menu pero solo funciona la opcion de salir de ese menu 
    * Parte Menu Principal: Hecha Completa
    * Parte Menu Sesion: Hecha Completa
    * Parte Menu Compras: Hechas Completa
    * Parte Menu Preparacion: Hecha Completa

* Parte Flujo de la Carrera: No Realizada

* Parte Entidades: Hecha Completa

* Parte Archivos: Hecha Completa

* Parte Formulas: Hecha Completa

* Bonus: Me falto hacer power-ups
    * Parte Buenas Practicas: Hecha Completa
    * Parte Power-Ups: No Realizada

* Parte Diagrama: Me falto agregar unos menus al diagrama de clases y unas cuantas relaciones

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además puse todos los archivos ```.csv``` en una carpeta llamada 'base_datos' por ende para el buen funcionamiento del programa todos los archivos .csv deben ser guardados en una carpeta con ese nombre



## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint() / menus1 y menus2```, ```sample() / menus1```
2. ```math```: ```floor() y ceil() / funciones``` 
3. ```collections```: ```defaultdict() / menus1, menus2 y menus3```
4. ```abc```: ```ABC y abstractmethod / abstracts```
5. ```os```: ```path.join() / parametros```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```abstract```: Contiene a las clases abstractas ```Menu```, ```Vehiculo```, ```Persona``` y ```Pista```
2. ```menus1```: Contiene la clase ```MenuSesion```
3. ```menus2```: Contiene la clase ```MenuPrincipal``` y ```MenuCompras```
4. ```vehiculos```: Contiene las clases de todos los tipos de vehiculos del juego
4. ```pilotos```: Contiene las clases de ```Piloto``` y ```Contrincante```
5. ```pista```: Contiene las clases de los distintos tipos de Pistas 
6. ```funciones```: Contiene todas las funciones necesarias para la ejecucion de la carrera
7. ```parametros```: Contiene todos los parametros usados dentro del programa
8. ```menus3```: Contiene ```MenuPreparacion```, ```MenuCarrera``` y ```MenuPits```


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://stackoverflow.com/questions/4710067/using-python-for-deleting-a-specific-line-in-a-file, este codigo sirve para poder eliminar una linea especifica en un archivo txt, esta implementado en ```menus2.py``` en los metodos ```guardar_piloto()``` y ```guardar_vehiculo()``` 

