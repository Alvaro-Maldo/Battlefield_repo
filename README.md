# Battlefield_

El trabajo se ha realizado de la siguiente forma entre sus creadores:

Alvaro: 
  Encargado de la parte de creación del tablero junto de forma aleatoria, la cual se ha realizado creando diversas funciones (dependiendo del tamaño de eslora del barco).  La metodología es la siguiente: Primero, buscamos una coordenada que no estuviera previamente marcada con un barco, posteriormente, iteramos con el array de las orientaciones; si el barco es de eslora 4, multiplicamos por 4 la orientación y comprobamos que desde la coordenada principal hasta la coordenada del final de la eslora no hay ningun barco y/o no se sale de los limites de la matriz. Si alguna de estas cosas ocurriese, iteraría a la siguiente orientación, creando un barco horizontal.
  PD: Si ninguna de las orientaciones fuesen validas, volveríamos a buscar una nueva coordenada inicial
  
  Nico:
