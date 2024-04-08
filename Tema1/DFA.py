# citire
fin = open("input.txt", "r")
N = int(fin.readline())
edges = dict()
for node in fin.readline().split():
    edges[int(node)] = dict()
M = int(fin.readline())
for i in range(M):
    l, r, chr = fin.readline().split()
    edges[int(l)][chr] = int(r)
S = int(fin.readline())
nrF = int(fin.readline())
Fin = set()
for node in fin.readline().split():
    Fin.add(int(node))
NrCuv = int(fin.readline())

for i in range(NrCuv):
    s = fin.readline().strip()
    curr = S
    for chr in s:
        curr = edges[curr][chr]
    if curr in Fin:
        print("DA")
    else: print("NU")