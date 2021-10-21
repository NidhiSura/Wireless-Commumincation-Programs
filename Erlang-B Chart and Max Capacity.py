import math
C = int(input('Enter no. of channels per cell\t\t'))
OurPr = float(input('Enter the blocking capability\t\t'))
cph = int(input('Enter no. of calls per hour\t\t'))
avgcd = int(input('Enter avg. call duration in minutes\t'))/60
N = int(input('Enter the no. of cells\t\t\t'))

#creating Erlang-B chart
ErBchart = dict()
for i in range(10000):
    A = i/100
    A = i/100
    D = 0
    for k in range(C):
        D += (A**k)/math.factorial(k)
    Pr = ((A**C)/math.factorial(C))/D
    Pr = round(Pr,2)
    ErBchart[Pr] = A
    
OurA = ErBchart[OurPr]
Au = cph*avgcd
U = OurA/Au
print('No. of users supported per cell = ' + str(round(U)) + ' Users')
maxcap = U*N
print('Max. capacity of the channel = ' + str(round(maxcap)) + ' Users')
