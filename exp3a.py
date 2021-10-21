#Experiment 3 Part A
import math
import matplotlib.pyplot as plt
import numpy as np

F = float(input('Enter the Frequency\t'))
Pt = float(input('Enter the power transmitted\t'))
Gt = float(input('Enter the transmitted antenna gain\t'))
Gr = float(input('Enter the received antenna gain \t'))
L = float(input('Enter the value of L\t'))
d = float(input('Enter the value of d\t'))
lamda=300000000/F
A1=(Pt*Gt*Gr)/L
A2=(lamda/(4*3.14*d))**2

Pr1=A1*A2


print('The value is', Pr1)
DB=10*math.log(Pr1,10)+30
print('The value in dbm', DB)

p=[]
K=[]
for D in range(1, 1000):
  Pr=A1*((lamda/(4*3.14*D))**2)
  Dbm=10*math.log(Pr,10)+30
  p.append(Dbm)
  K.append(D)

plt.plot(K,p)
