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

def lambdaInc(node): # calculeaza lambda inchiderea nodului
    lambdaNodes = list()
    for lambdaNode in edges[node]['0']:  # verific nodurile legate imediat de nodul original
        if lambdaNode not in lambdaVisited:
            lambdaVisited.add(lambdaNode)
            lambdaNodes.append(lambdaNode)

    i = 0
    while i < len(lambdaNodes):  # caut cu bfs toate nodurile cu legaturi lambda prin care nu s.a trecut deja
        if '0' in edges[lambdaNodes[i]]:
            for lambdaNode in edges[lambdaNodes[i]]['0']:
                if lambdaNode not in lambdaVisited:
                    lambdaVisited.add(lambdaNode)
                    lambdaNodes.append(lambdaNode)
        i += 1
    # avem toate nodurile in care putem sa jungem cu lambda din nodul original
    for node in lambdaNodes:
        currStep.add(node)
    # si le adaugam in currStep
    del lambdaNodes
    return

#lambda = '0'
for i in range(NrCuvinte):
    currStep = {S}
    index = 0
    s = fin.readline().strip()
    while index < len(s):
        nextStep = set()# urmatoarea multime de noduri in care pot ajunge
        lambdaVisited = currStep.copy()# pentru a memora cu ce noduri am inchis starea curenta
        for node in currStep.copy():# fac lambda inchiderea starii curente
            if '0' in edges[node]:
                lambdaInc(node)
        del lambdaVisited

        for node in currStep:# calculez urmatoarea stare
            if s[index] in edges[node]:
                nextStep = nextStep.union(edges[node][s[index]])
        if not nextStep:# daca urmatoarea stare nu are noduri, nu mai am unde sa ma duc
            print("NU")
            break
        else: currStep = nextStep
        index += 1

    else:# daca se termina cuvantul
        lambdaVisited = currStep.copy()
        for node in currStep.copy():# mai trebuie facuta o lambda deschidere
            if '0' in edges[node]:
                lambdaInc(node)
        del lambdaVisited
        for node in Fin:
            if node in currStep:
                print("DA")
                break
        else: print("NU")

