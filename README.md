# Battlefield_

El trabajo se ha realizado de la siguiente forma entre sus creadores:

Alvaro: 
  Encargado de la parte de creación del tablero junto de forma aleatoria, la cual se ha realizado creando diversas funciones (dependiendo del tamaño de eslora del barco).  La metodología es la siguiente: Primero, buscamos una coordenada que no estuviera previamente marcada con un barco, posteriormente, iteramos con el array de las orientaciones; si el barco es de eslora 4, multiplicamos por 4 la orientación y comprobamos que desde la coordenada principal hasta la coordenada del final de la eslora no hay ningun barco y/o no se sale de los limites de la matriz. Si alguna de estas cosas ocurriese, iteraría a la siguiente orientación, creando un barco horizontal.
  PD: Si ninguna de las orientaciones fuesen validas, volveríamos a buscar una nueva coordenada inicial
  
  Nico:
  Encargado de las funciones de ataque. Ambas siguen una estructura similar, para la del jugador se piden las cordenadas mediante un imput y se comprueba qué hay en la posición indicada. En caso de que haya un barco enemigo se señala y se repite el turno, y en caso de que haya agua se salta al siguiente turno. En caso de dispar en una casilla repetida o fuera del tablero, se notifica al jugador y se vuelve a repetir el turno. La función de atque del ordenador es muy similar, pero se dan coordenadas aleatorias, por lo que no pueden caer fuera del tablero pero sí repetirse. Además hemos añadido la opción de seleccionar el nivel de dificultad. En el nivel 1 el ordenador jugaría un turno normal. En el 2 tira dos veces, en caso de acertar la primera repite turno pero no vuelve a tirar. 

La parte de anidar todas las funciones la hemos hecho entre los dos. Todas las funciones se encuentran dentro de la funcion battleship. Al iniciarla lo primero que hace,tras una breve introducción para entrar en ambiente, es generar el tablero y después colocar los barcos, que quedan incluidos en la función inicio. Para los turnos de juego hemos utilizado un bucle While que se rompe cuando uno de los dos tableros se queda sin barcos, que se cuenta mediante un count.
