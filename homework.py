import numpy as np

list=np.arange(3000,3901)
for i in list:
    if i %2==1:
        print(i,end="/")
print()
matrix=np.random.randint(1,10,500).reshape(50,10)
for i in matrix.flat:
    if i %2==0:
        print(i,end=" ")
