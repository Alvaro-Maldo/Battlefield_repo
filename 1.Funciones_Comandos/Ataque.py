import numpy as np

pc_12=np.repeat(" ",90).reshape(9,10)
pc_stack=np.array(["O","O","O","O","O","O","O","O","O","O","O",])

pc_1=np.vstack((pc_12,pc_stack))

pc_empty=np.repeat(" ",100).reshape(10,10)

u_1=np.repeat(" ",100).reshape(10,10)
u_empty=np.repeat(" ",100).reshape(10,10)

def disparo():


    while True:

        x=int(input("Dime la fila"))
        y=int(input("Dime la columna"))

        if pc_1[x,y]=="O":
            u_empty[x,y]="X"
            pc_1[x,y]="X"
            print(u_empty)
            continue
        

        elif pc_1[x,y]==" ":
            u_empty[x,y]="-"
            pc_1[x,y]="-"
            print(u_empty)
            break

        else:
            print("El disparo no es valido")
            break
disparo()
