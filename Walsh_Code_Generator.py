#Walsh Code Generation
#Parameters:bases function H2 = [[1,1],[1,-1]]
#H4 = [[H2,H2],[H2,-H2]]
import math

def walshcode(Hn):
    newlst = []
    H2 = [[1,1],[1,-1]]
    for x in range(len(H2)):
        for i in Hn:
            lst1 = []
            for y in range(len(H2)):
                for j in i:
                    lst1.append(j*H2[x][y])
            newlst.append(lst1)
    return newlst

n = int(input("Enter the no. of Walsh sequences you want to generate eg. 4, 8, 16, 32...\t"))
n = math.log(n,2)
Hnext =  [[1,1],[1,-1]]
for _ in range(int(n)-1):
    Hnext = walshcode(Hnext)
#print(Hnext)
for i in Hnext:
    for j in i:
        if j==1:
            print(" ", end="")
        print(j,end=" ")
    print("")
