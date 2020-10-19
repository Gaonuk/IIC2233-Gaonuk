# Tarea 2: DCCAMPO

## Consideraciones generales :octocat:

* El juego comienza con una ventana de inicio parecida a la del enunciado, si uno introduce un nombre de mapa correcto el juego empieza y si no entonces se actualiza un label que indica que el nombre no es valido

* La ventana donde se juega esta separada de una ventana llamada Inventario que contiene toda la informacion del juego, osea el dinero, el tiempo, la energia, el boton salir y el inventario en si

* Asumi que siempre nos daran un mapa del mismo tamano pero si es posible cambiar el N del tamano de cada parte del mapa en parametros_generales con el parametro ```SIZE_TILE```

* Al no haber implementado las colisiones con objetos, la tienda aparece a penas empieza el juego dado que si esta implementada y funciona. Cuando uno compra un objeto, se activa el boton para venderlo. Un problema es que cuando uno compra semillas y luego las dropea en una tierra cultivable y luego no quedan semillas en el inventario, el boton de vender sigue activado.

* Cuando uno tiene un hacha y/o una azada disponible se pueden arar tierras para que sean cultivables y se pueden talar arboles

* Cuando la energia llega a 0 queria que aparececiera una ventana nueva que indique que uno perdio la partida y despues de unos segundos se apague el programa pero la ventana cuando aparece no aparece el texto

* Esta implementado el sistema de codigos secretos para el dinero y la energia, apretando todas las teclas juntas.

* En el gitignore puse todos los archivos que tienen que ser ignorados

* Las senales de la ventana inicio estan en el archivo ```ventanas.py``` en las lineas 16, 32 y 38, y el aviso se le da al jugar por medio de la funcion ```play()```

* Las senales de la ventana de juego estan en la clase ```VentanaJuego``` y en el metodo ```init_signals()``` en las lineas 50 a 58 y 217 a 232

* La barra de energia esta implementada en la ventana del inventario en el modulo ```ventanas2.py```, en las lineas 304 a 312 y la barra de energia se genero en designer

* Las senales del drag and drop del inventario estan el modulo ```drags.py```, en el modulo ```ventanas.py``` en donde se crean los DropLabel y en el modulo ```ventanas2.py``` en la linea 281 donde se crea un DraggableLabel y en el metodo actualizar inventario que agrega labels del tipo DraggableLabel

* las senales de la tienda estan en los modulos ```ventanas.py```, ```ventanas2.py``` y ```personaje.py```, en ventanas.py se instancia la Tienda y se conectan las senales de la tienda con el backend del personaje en ```personaje.py```, luego las senales las recibe el personaje y procesa la compra o venta de algun objeto y envia una senal al inventario para actualizarlo. Lineas ```162, 219-224, 213``` en ```ventanas.py```. Lineas 70 a 85 en ```ventanas2.py``` se conectan los botones, lineas ```26-27``` se crean las senales, y en los metodos en lineas ```93 a 100``` se envian las senales. Lineas ```129 a 206``` en el modulo ```personaje.py``` aqui el backend procesa las transacciones y revisa si hay dinero  suficiente.

* El movimiento del personaje esta en las lineas ```198 a 203, 160 y 325 a 333``` del modulo ```ventanas.py```, y el movimiento en el backend se procesa en el modulo ```personaje.py``` con las properties y el metodo ```update_window_character``` en las lineas ```50 a 57```, mas las lineas ```104 a 127```

* Los cultivos estan implementados en las lineas ```118 a 136``` del modulo ```drags.py```, y el backend de los cultivos lo procesa la clase Planta del modulo ```threads.py``` en las lineas ```79 a 84``` mediante la senal ```senal_actualizar``` 

* Hice que las apariciones aleatorias de arboles y oro fuesen segun un intervalo de tiempo que esta en el archivo ```threads.py``` en la linea 103, por ende aparecen mas frecuentemente que un evento cada nuevo dia. Estos spawns aleatorios pueden aparecer en cualquier parte del mapa, incluidos la tienda y la casa, pero no encima de las rocas. Las senales las procesa el backend con la clase Obstaculos en el modulo ```threads.py``` en las lineas ```100 a 122``` y se conecta con el frontend a traves del personaje en las lineas ```267 a 272``` en el modulo ```personaje.py``` que se conecta con la ventana juego en el modulo ```ventanas.py``` en las linea 227 con la senal ```update_from``` el cual se conecta con el metodo ```update_mapa``` en las lineas ```261 a 273```

* Las senales de los clicks se procesan en el modulo ```ventanas.py``` en el metodo ```item_clicked```

* La clase ```Recurso``` maneja los recursos en el modulo ```ventanas2.py``` y la clase ```Actualizador``` en el modulo ```threads.py``` se encarga de verificar si el tiempo definido ya paso y tiene que desaparecer un recurso, lineas ```41 a 59```

* El tiempo esta implementado en la clase ```Calendario``` en el modulo ```threads.py```

* Las funcionalidades extras de las teclas estan implementadas en el modulo ```ventanas.py``` en las lineas ```243 a 253 y 258-259```  y utiliza la senal ```restaurar_energia``` para restaurar la energia en la otra ventana, lineas 309 a 311 del modulo ```ventanas2.py``` y el backend del personaje es el que maneja los cambios en el dinero

* La mayoria de las senales se conectan en el modulo ```main.py``` 



### Cosas implementadas y no implementadas :white_check_mark: :x:

* Parte Entidades: Hecha completa
* Parte Interfaz: Hecha completa
* Parte Interaccion Usuario: Me faltó hacer chocar, recoger, pararse:
    * Parte Drag and Drop: Hecha Completa
    * Parte Click: Hecha Completa
    * Parte Pararse: No realizada
    * Parte Recoger: No realizada
    * Parte Chocar: El personaje puede chocar con el borde del mapa pero no con los arboles y las piedras
* Parte Archivos: Utilizados todos los archivos entregados y se genero el archivo parametros_generales.py
* Parte Funcionalidades Extras: Me falto hacer la Pausa
    * Parte K + I + P: Hecha Completa
    * Parte M + N + Y: Hecha Completa
    * Parte Pausa: No realizada
* Parte Sprites: Sprites utilizados en el juego
* Parte Bonus: Bonus no realizado



## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. 

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5.Qt```: ```QTest, QRect``` en los modulos ventanas2.py, drags.py, personaje.py y threads.py
2. ```PyQt5.QtGui```: ```QPixmap, QFont, QDrag, QPainter, QCursor``` en los modulos ventanas.py, ventanas2.py y drags.py
3. ```PyQt5.QtCore```: ```pyqtSignal, Qt, QRect, QTimer, QMimeData, QThread``` modulos ventanas.py, ventanas2.py, drags.py y threads.py, parametros_generales.py
4. ```PyQt5.QtWidgets```: ```QWidget, QLabel, QLineEdit, QPushButton, QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QSizePolicy``` esta libreria fue usada en todos los modulos
5. ```random```: ```randint``` en los modulos ventanas.py y threads.py
6. ```sys```: en modulos: ventanas y ventanas2, drags y threads
7. ```os.path```: ```join`` en el modulo parametros_generales.py, ventanas.py
8. ```collections```: ```deque``` en el modulo ventanas.py
9. ```PyQty```: ```uic``` en los modulos ventana.py y ventanas2.py
10. ```time```: ```sleep, time``` en los modulos threads y ventanas2
11. ```threading```: ```Lock``` en el modulo personaje.py

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```ventanas.py```: Contiene a ```VentanaInicio```, ```VentanaJuego```
2. ```ventanas2.py```: Contiene a ```VentanaTienda```, ```Inventario```, ```Recurso```, ```ClickLabel``` y ```VentanaPerder```
3. ```drags.py```: Contiene a ```DropLabel``` y ```DraggableLabel```
4. ```threads.py```: Contiene a ```Calendario```. ```Obstaculos```, ```Actualizador``` y ```Planta```
5. ```personaje.py```: Contiene a ```Personaje```
6. ```parametros_generales.py```: Contiene todos los parametros generales usados en el juego

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://stackoverflow.com/questions/55636860/drag-and-drop-qlabels-with-pyqt5-pixmap-and-text: Utilice este codigo para poder hacer el drag and drop y que al mismo tiempo se puedan pasar las imagenes y el texto, esto esta implementado en el archivo drags.py

2. https://stackoverflow.com/questions/50955182/pyqt5-which-qlabel-was-pressed-by-mousepressevent: Utilice este codigo para que pueda obtener que objeto esta siendo clickeado y processar la interfaz y el juego acorde a esto. Este codigo esta implementado en ```ventanas2.py``` a partir de la linea ```235``` hasta la linea ```256```

3. https://stackoverflow.com/questions/49013010/enabling-disabling-buttons: Utilice este codigo para que en mi tienda se puedan apagar y encender los botones segun si tiene o no un item

