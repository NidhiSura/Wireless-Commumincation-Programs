#1/2 Convolution Encoder
#k=3, g1 = [1,1,1], g2 =  [1,0,1]
#User inputs - g1,g2,message bits
#m = [0,1,0,0]
g1 = input("Enter g1 bits space separated\t").split(" ")
g2 = input("Enter g2 bits space separated\t").split(" ")
mlst = [0,0]
n = int(input('Enter no. of message bits\t'))
print("Enter message bits separated by an 'enter'")
for _ in range(n):
    mlst.append(int(input()))
for _ in range(4):
    mlst.append(0)
Og1seq = []
Og2seq = []
for x in range(n+2):
    mseq = mlst[x:(3+x)]
    Og1 = 0
    Og2 = 0
    for x in range(3):
        m1 = mseq[x] * int(g1[x])
        m2 = mseq[x] * int(g2[x])
        Og1 = Og1 ^ m1
        Og2 = Og2 ^ m2
        #print(m1,m2,Og1,Og2)
    Og1seq.append(Og1)
    Og2seq.append(Og2)
#print(Og1seq,Og2seq)
finalseq = []
for x in range(len(Og1seq)):
    finalseq.append(Og1seq[x])
    finalseq.append(Og2seq[x])
print(finalseq)
