import collections
fin = open("inputFST.txt", "r")
S = int(fin.readline())
edges = collections.defaultdict(dict)
M = int(fin.readline())
for i in range(M):
    l, r, char1, char2 = fin.readline().split()
    if int(l) in edges and char1 in edges[int(l)]:
        edges[int(l)][char1].add((int(r), char2))
    else:
        edges[int(l)][char1] = {(int(r), char2)}
Fin = set()
for node in fin.readline().split():
    Fin.add(int(node))
NrCuvinte = int(fin.readline())
# input:
'''input node
   nr muchii
   muchii de forma: start end lit1 lit2
   noduri finale
   nr cuvinte
   cuvinte'''
print(edges)

def dfs(curr, index):
    if index == len(s):# finalul cuvantului
        if curr in Fin:
            res.append(''.join(word))
        return

    if s[index] in edges[curr]:# daca nu e dead-end
        for node in edges[curr][s[index]]:# apel recursiv pe fiecare nod urmator
            word.append(node[1])
            dfs(node[0], index + 1)
            word.pop()
    else:
        return

for i in range(NrCuvinte):
    s = fin.readline().strip()
    res = [] # multimea rezultatelor
    word = [] # memoreaza cuvantul
    dfs(S, 0)
    print(res)
