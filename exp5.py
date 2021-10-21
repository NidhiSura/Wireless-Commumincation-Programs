#Gold Sequence Generation
m = int(input('Enter the no. of shift registers'))
seed1 = []
seed2 = []
print('Enter the value of seed of m-sequence 1, each followed by an "enter"')
for i in range(m):
    seed1.append(int(input()))
print('Enter the value of seed of m-sequence 2, each followed by an "enter"')
for i in range(m):
    seed2.append(int(input()))
seq = []
for i in range((2**m) - 1):
    seq.append(seed1[4]^seed2[4])
    lst1 = []
    lst2 = []
    lst1.append(seed1[1] ^ seed1[2] ^ seed1[3] ^ seed1[4])
    lst2.append(seed2[1] ^ seed2[4])
    for j in range(m-1):
        lst1.append(seed1[j])
        lst2.append(seed2[j])
    seed1,seed2 = lst1,lst2
print(seq)
