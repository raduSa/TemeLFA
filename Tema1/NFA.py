import collections
# citire
fin = open("input.txt", "r")
N = int(fin.readline())
edges = dict()
for node in fin.readline().split():
    edges[int(node)] = collections.defaultdict(set)# de forma {nod : {litera : nod urmator} }
M = int(fin.readline())
for i in range(M):
    l, r, chr = fin.readline().split()
    edges[int(l)][chr].add(int(r))
S = int(fin.readline())
nrF = int(fin.readline())
Fin = set()
for node in fin.readline().split():
    Fin.add(int(node))
NrCuvinte = int(fin.readline())
def dfs(curr, index):
    if index == len(s):# finalul cuvantului
        if curr in Fin:
            return True
        else: return False
    if s[index] in edges[curr]:# daca nu e dead-end
        for node in edges[curr][s[index]]:# apel recursiv pe fiecare nod urmator
            path.append(node)
            if dfs(node, index + 1):
                return True
            path.pop()
        return False
    else: return False

for i in range(NrCuvinte):
    s = fin.readline().strip()
    path = [S] # memoreaza drumul
    if dfs(S, 0):
        print("DA", path)
    else: print("NU")