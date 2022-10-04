import numpy as np
import random

u_1 = np.arange(1,122).reshape(11,-1)
u_1 = np.where(u_1, " ", u_1)
u_1[-1:]=[1,2,3,4,5,6,7,8,9,10,0]
u_1[::,-1:]=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],['']]

tablero_pc=u_1.copy()
u_empty = u_1.copy()
    
#Función para lo tableros
#def tableros():
    #u_1 = np.arange(1,122).reshape(11,-1)
    #u_1 = np.where(u_1, " ", u_1)
    #u_1[-1:]=[1,2,3,4,5,6,7,8,9,10,0]
    #u_1[::,-1:]=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],['']]

    #tablero_pc=u_1.copy()
    #u_empty = u_1.copy()

    #return u_1, tablero_pc, u_empty

#Funciones que hacen los barcos
def barco1():

    while True:
        rand1=random.randint(0,9)
        rand2=random.randint(0,9)

        pos_1=[rand1,rand2]

        if u_1[pos_1[0],pos_1[1]]=="O":
            continue

        else:
            u_1[pos_1[0],pos_1[1]]="O"
            break
def barco1_pc():

    while True:
        rand1=random.randint(0,9)
        rand2=random.randint(0,9)

        pos_1=[rand1,rand2]

        if tablero_pc[pos_1[0],pos_1[1]]=="O":
            continue

        else:
            tablero_pc[pos_1[0],pos_1[1]]="O"
            break

def barco2():

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
def barco2_pc():

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

def barco3():

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
def barco3_pc():

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

def barco4():
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
def barco4_pc():
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
def inicio():
    #tablero 1
    barco1()
    barco1()
    barco1()
    barco1()
    barco2()
    barco2()
    barco2()
    barco3()
    barco3()
    barco4()
    #tablero 2
    barco1_pc()
    barco1_pc()
    barco1_pc()
    barco1_pc()
    barco2_pc()
    barco2_pc()
    barco2_pc()
    barco3_pc()
    barco3_pc()
    barco4_pc()

#Funciones de disparo
def disparo():
    count1=np.count_nonzero(tablero_pc=="O")
    while True:
        print("Estos son tus barcos \n", u_1)
        print("Elige las coordenadas donde disparar \n", u_empty )
        x=int(input("Dime la fila "))-1
        y=int(input("Dime la columna "))-1
        try:
            if tablero_pc[x,y]=="O":
                u_empty[x,y]="X"
                tablero_pc[x,y]="X"
                if count1 ==0:
                    print("Ganador!")
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
def disparo_random():
    count2=np.count_nonzero(u_1=="O")
    while True:

        print("Es el turno de la máquina")
        #print("Estos son tus barcos \n", u_1)

        x= random.randint(0,9)
        y= random.randint(0,9)

        if u_1[x,y]=="O":
            u_1[x,y]="X"
            print('Disparo en: ('+ str(x+1)+ "," +str(y+1) + ")")#nuevo
            if count2 == 0:
                print("Has perdido :(")
                break
            else:
                print("Te han alcanzado, te quedan", count2, "localizaciones") 
                continue
        

        elif u_1[x,y]==" ":
            u_1[x,y]="-"
            print('Disparo en: ('+ str(x+1)+ "," +str(y+1) + ")")#nuevo
            print("Tu turno")
            break
        else:
            continue

#Función principal donde se junta todo
def battleship():
    #Lo primero que hace la función es crear los tableros. Tres vacios, en dos estarán los barcos y otro servirá para marcar los disparos del jugador.
    #Por algun motivo desconocido, al meter los comandos de creacion de tablero aqui dentro el resto de funciones dejan de reconocerlo
    #tableros()

    
    
    #Después se ejecuta la funcion inicio dentro de la cual se encuentran las funciones que van a colocar cada barco en ambos tableros
    inicio()

    #Con un bucle while se van alternando las funciones de disparo hasta que uno de los dos pierda
    print("hola")
    while True:
        disparo()
        disparo_random()
        count1=np.count_nonzero(tablero_pc=="O")
        count2=np.count_nonzero(u_1=="O")
        if count1 ==0 or count2 ==0:
            break
    print("Gracias por jugar. Hasta pronto!")
    return

battleship()
