import numpy as np

pc_12=np.repeat(" ",90).reshape(9,10)
pc_stack=np.array(["O","O","O","O","O","O","O","O","O","O"])

pc_1=np.vstack((pc_12,pc_stack))

pc_empty=np.repeat(" ",100).reshape(10,10)

u_1=np.repeat(" ",100).reshape(10,10)
u_empty=np.repeat(" ",100).reshape(10,10)

print(pc_1)