import numpy as np

def numpy_linear(file):
    mat = np.loadtxt(file,dtype = int, delimiter=',')   
    mat_shape = mat.shape                               #return a tuple (rows_num, col_num)
    last_cols = mat_shape[1]-1                          #calculate last column index
    a = mat[:,:last_cols]                               #extract all column except last one
    b = mat[:, last_cols]                               #extract last column

    x = np.linalg.solve(a, b)                           #solve the linear equation

    print(x)

numpy_linear("mat.txt")
