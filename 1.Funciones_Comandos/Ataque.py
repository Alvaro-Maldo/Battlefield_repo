import numpy as np

pc_12=np.repeat(" ",90).reshape(9,10)
pc_stack=np.array(["O","O","O","O","O","O","O","O","O","O"])
pc_1=np.vstack((pc_12,pc_stack))

u_1=np.repeat(" ",100).reshape(10,10)
u_empty=np.repeat(" ",100).reshape(10,10)

count=np.count_nonzero(pc_1=="O")
print(count)


#FALTA COMPROBAR QUE EL COUNT FUNCIONE EN LA FUNCIÓN (SALE NONE)

def disparo():


    while True:
        print("Estos son tus barcos \n", u_1)
        print("Elige las coordenadas donde disparar \n", u_empty )
        x=int(input("Dime la fila "))-1
        y=int(input("Dime la columna "))-1

        if pc_1[x,y]=="O":
            u_empty[x,y]="X"
            pc_1[x,y]="X"
            print("Has alcanzado un barco, te quedan ",print(str(count)), " localizaciones por hundir") 
            

            continue
        

        elif pc_1[x,y]==" ":
            u_empty[x,y]="-"
            pc_1[x,y]="-"
            print(u_empty)
            print("El disparo no es valido")
            break

        else:
            print("El disparo no es valido, por favor, introduce un valor del 1-10 tanto en filas como en columnas")
            continue
disparo()
