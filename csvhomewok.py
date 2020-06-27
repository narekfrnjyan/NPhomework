import numpy as np
import csv
import sys
x=sys.argv
if x[1]=="fill":
    matrix = np.random.randint(1, 10, 2000).reshape(50, 40)
    with open("file.csv","w") as file:
        write=csv.writer(file)
        for row in  matrix:
            write.writerow(row)
elif x[1]=="print":
    with open("file.csv") as file1:
        read=csv.reader(file1)
        for row in read:
            for elem in row:
                if int(elem)%2==0:
                    print(elem ,end=" ")


