#in our circuit, S0 = S0 xor S2
m = int(input("Enter the no. of shift registers\t"))
G = []
print('Enter the seed, pressing enter after each input')
for i in range(m):
    G.append(int(input()))
L = (2**m) - 1
seq = [G[2]]
for i in range(L-1):
    lst = []
    if G[0]+G[2]==0 or G[0]+G[2]==2:
        lst.append(0)
    else:
        lst.append(1)
    lst.append(G[0])
    lst.append(G[1])
    G = lst
    seq.append(G[2])
print(seq)
