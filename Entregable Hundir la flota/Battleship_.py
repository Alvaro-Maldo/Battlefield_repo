import numpy as np
import random

#Funciones de inicio
def barco1(u_1):

    while True:
        rand1=random.randint(0,9)
        rand2=random.randint(0,9)

        pos_1=[rand1,rand2]

        if u_1[pos_1[0],pos_1[1]]=="O":
            continue

        else:
            u_1[pos_1[0],pos_1[1]]="O"
            break
def barco1_pc(tablero_pc):

    while True:
        rand1=random.randint(0,9)
        rand2=random.randint(0,9)

        pos_1=[rand1,rand2]

        if tablero_pc[pos_1[0],pos_1[1]]=="O":
            continue

        else:
            tablero_pc[pos_1[0],pos_1[1]]="O"
            break

def barco2(u_1):

 while True:
        rand1=random.randint(0,9)
        rand2=random.randint(0,9)

        pos_1=[rand1,rand2]

        if u_1[pos_1[0],pos_1[1]]=="O":
            continue


        arr= np.array([[-1,0],[0,-1],[0,1],[1,0]])

        for i in arr: #como pongo que coja el valor aleatorio del array

            pos_2=pos_1+i

            if pos_2[0]<0 or pos_2[0]>9 or pos_2[1]<0 or pos_2[1]>9:
                continue

            elif u_1[pos_2[0],pos_2[1]]=="O":
                continue

            else:
                u_1[pos_1[0],pos_1[1]]="O"
                u_1[pos_2[0],pos_2[1]]="O"

                return
def barco2_pc(tablero_pc):

 while True:
        rand1=random.randint(0,9)
        rand2=random.randint(0,9)

        pos_1=[rand1,rand2]

        if tablero_pc[pos_1[0],pos_1[1]]=="O":
            continue


        arr= np.array([[-1,0],[0,-1],[0,1],[1,0]])

        for i in arr: 

            pos_2=pos_1+i

            if pos_2[0]<0 or pos_2[0]>9 or pos_2[1]<0 or pos_2[1]>9:
                continue

            elif tablero_pc[pos_2[0],pos_2[1]]=="O":
                continue

            else:
                tablero_pc[pos_1[0],pos_1[1]]="O"
                tablero_pc[pos_2[0],pos_2[1]]="O"
                return

def barco3(u_1):

 while True:
        rand1=random.randint(0,9)
        rand2=random.randint(0,9)

        pos_1=[rand1,rand2]

        if u_1[pos_1[0],pos_1[1]]=="O":
            continue


        arr= np.array([[-1,0],[0,-1],[0,1],[1,0]])

        for i in arr:

            pos_3=pos_1+2*i
            pos_2=pos_1+i

            if pos_3[0]<0 or pos_3[0]>9 or pos_3[1]<0 or pos_3[1]>9:
                continue

            elif u_1[pos_3[0],pos_3[1]]=="O" or u_1[pos_2[0],pos_2[1]]=="O":
                continue

            else:
                u_1[pos_1[0],pos_1[1]]="O"
                u_1[pos_3[0],pos_3[1]]="O"
                u_1[pos_2[0],pos_2[1]]="O"

                return
def barco3_pc(tablero_pc):

 while True:
        rand1=random.randint(0,9)
        rand2=random.randint(0,9)

        pos_1=[rand1,rand2]

        if tablero_pc[pos_1[0],pos_1[1]]=="O":
            continue


        arr= np.array([[-1,0],[0,-1],[0,1],[1,0]])

        for i in arr:

            pos_3=pos_1+2*i
            pos_2=pos_1+i

            if pos_3[0]<0 or pos_3[0]>9 or pos_3[1]<0 or pos_3[1]>9:
                continue

            elif tablero_pc[pos_3[0],pos_3[1]]=="O" or tablero_pc[pos_2[0],pos_2[1]]=="O":
                continue

            else:
                tablero_pc[pos_1[0],pos_1[1]]="O"
                tablero_pc[pos_3[0],pos_3[1]]="O"
                tablero_pc[pos_2[0],pos_2[1]]="O"

                return

def barco4(u_1):
    while True:
        rand1=random.randint(0,9)
        rand2=random.randint(0,9)

        pos_1=[rand1,rand2]

        if u_1[pos_1[0],pos_1[1]]=="O":
            continue

        arr= np.array([[-1,0],[0,-1],[0,1],[1,0]])

        for i in arr: 

                pos_4=pos_1+3*i
                pos_3=pos_1+2*i
                pos_2=pos_1+i

                if pos_4[0]<0 or pos_4[0]>9 or pos_4[1]<0 or pos_4[1]>9:
                    continue

                elif u_1[pos_4[0],pos_4[1]]=="O" or u_1[pos_3[0],pos_3[1]]=="O" or u_1[pos_2[0],pos_2[1]]=="O":
                    continue

                else:
                    u_1[pos_1[0],pos_1[1]]="O"
                    u_1[pos_4[0],pos_4[1]]="O"
                    u_1[pos_3[0],pos_3[1]]="O"
                    u_1[pos_2[0],pos_2[1]]="O"

                    return
def barco4_pc(tablero_pc):
    while True:
        rand1=random.randint(0,9)
        rand2=random.randint(0,9)

        pos_1=[rand1,rand2]

        if tablero_pc[pos_1[0],pos_1[1]]=="O":
            continue

        arr= np.array([[-1,0],[0,-1],[0,1],[1,0]])

        for i in arr: 

                pos_4=pos_1+3*i
                pos_3=pos_1+2*i
                pos_2=pos_1+i

                if pos_4[0]<0 or pos_4[0]>9 or pos_4[1]<0 or pos_4[1]>9:
                    continue

                elif tablero_pc[pos_4[0],pos_4[1]]=="O" or tablero_pc[pos_3[0],pos_3[1]]=="O" or tablero_pc[pos_2[0],pos_2[1]]=="O":
                    continue

                else:
                    tablero_pc[pos_1[0],pos_1[1]]="O"
                    tablero_pc[pos_4[0],pos_4[1]]="O"
                    tablero_pc[pos_3[0],pos_3[1]]="O"
                    tablero_pc[pos_2[0],pos_2[1]]="O"

                    return
def inicio(u_1,tablero_pc):
    #tablero 1
    barco1(u_1)
    barco1(u_1)
    barco1(u_1)
    barco1(u_1)
    barco2(u_1)
    barco2(u_1)
    barco2(u_1)
    barco3(u_1)
    barco3(u_1)
    barco4(u_1)
    #tablero 2
    barco1_pc(tablero_pc)
    barco1_pc(tablero_pc)
    barco1_pc(tablero_pc)
    barco1_pc(tablero_pc)
    barco2_pc(tablero_pc)
    barco2_pc(tablero_pc)
    barco2_pc(tablero_pc)
    barco3_pc(tablero_pc)
    barco3_pc(tablero_pc)
    barco4_pc(tablero_pc)


#Funciones de disparo
def disparo(tablero_pc,u_empty,u_1):
    
    while True:
        count1=np.count_nonzero(tablero_pc=="O")-1
        print("Estos son tus barcos \n", u_1, '\n')
        print("Elige las coordenadas donde disparar \n", u_empty ,'\n')
        x=int(input("Dime la fila "))-1
        y=int(input("Dime la columna "))-1
        try:
            if tablero_pc[x,y]=="O":
                u_empty[x,y]="X"
                tablero_pc[x,y]="X"
                if count1 ==0:
                    print("¡Enhorabuena Capitán! Ha conseguido salvar a la flota y hundir al enermigo. Podemos regresar a puerto a celebrar la victoria")
                    break
                else:
                    print("Has alcanzado un barco, te quedan ", count1, " localizaciones por hundir") 
                    continue
        

            elif tablero_pc[x,y]==" ":
                u_empty[x,y]="-"
                tablero_pc[x,y]="-"
                print(u_empty)
                print("Agua")
                break

            else: #nuevo
                print('El disparo no es valido, por favor, introduce un valor del 1-10 tanto en filas como en columnas, donde no se haya disparado')
        except IndexError:
            print("El disparo no es valido, por favor, introduce un valor del 1-10 tanto en filas como en columnas")
            continue

def disparo_random(u_1,diff):
    
    while True:
        
        count2=np.count_nonzero(u_1=="O")-1

        x= random.randint(0,9)
        y= random.randint(0,9)

        if u_1[x,y]=="O":
            u_1[x,y]="X"
            print('Disparo en: ('+ str(x+1)+ "," +str(y+1) + ")")
            if count2 == 0:
                print('''Aunque luchamos ferozmente en la batalla no hempos sido capaces de estar a la altura. Regresemos a puerto y preparemos el contrataque.''')
                break
            else:
                if diff==2:
                    print("Te han alcanzado, te quedan", count2, "localizaciones") 
                    diff = diff-1 #Si el ordenador acierta no se entra en el if de la segunda oportunidad para el ordena
                    continue
                else:
                    print("Te han alcanzado, te quedan", count2, "localizaciones") 
                    break

        elif u_1[x,y]==" ":
            u_1[x,y]="-"
            print('Disparo en: ('+ str(x+1)+ "," +str(y+1) + ")")
            #Cuando se selecciona dificultad 2 el ordenador tiene dos turnos en caso de que el primero caiga en agua
            if diff == 2:
                diff = diff-1
                continue

            print("\nTu turno")

            break
        else:
            continue

#Función del juego, con todo en común
def battleship():
    print('''Bienvenido al puente de mandos Capitán!
.
.
.
El enemigo lleva toda la mañana atacando sin cesar, aunque creemos por lo inpreciso de sus disparos que su radar debe de haberse dañado en la batalla. Casi parece que disparan de forma aleatoria. 
Hemos localizado 4 corbetas, 3 fragatas, 2 destructores y un portaaviones, hemos de destruirlos a todos antes de que acaben con nuestra flota.
.
.
.
La situación es crítica Capitán, la antena del barco se ha roto y la comunicación con el resto de la flota se ha reducido drástricamente. Los ingenieros trabajan en
la reparación sin descanso, mientras tanto confiamos en su sentido de la estrategia para descubrir y destruir a la flota enemiga. Solo díganos las coordenadas donde disparar y le seguiremos hasta el final. 
.
.
.
¡Buena suerte Capitán!''')

    #Lo primero que hace la función es crear los tableros. Tres vacios, en dos estarán los barcos y otro servirá para marcar los disparos del jugador.
    u_1 = np.arange(1,122).reshape(11,-1)
    u_1 = np.where(u_1, " ", u_1)
    u_1[-1:]=[1,2,3,4,5,6,7,8,9,10,0]
    u_1[::,-1:]=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],['']]

    tablero_pc=u_1.copy()
    u_empty = u_1.copy()
    
    #Después se ejecuta la funcion inicio dentro de la cual se encuentran las funciones que van a colocar cada barco en ambos tableros
    inicio(u_1, tablero_pc)

    #Se puede seleccionar entre varios niveles de dificultad
    
    diff = int(input('''.\n.\n.\n¿Con que dificultad te gustaría jugar?
    
    Pulsa 1 para el modo fácil.
    Pulsa 2 para el modo difícil.
    '''))

    #Con un bucle while se van alternando las funciones de disparo hasta que uno de los dos pierda
    while True:

            disparo(tablero_pc,u_empty,u_1)
            count1=np.count_nonzero(tablero_pc=="O")
            if count1 ==0:
                break

            print("El enemigo está disparando \n")
            disparo_random(u_1,diff)
            count2=np.count_nonzero(u_1=="O")
            if count2 ==0:
                break
    
    print("Gracias por jugar. Hasta pronto!")
    return

battleship()