import collections
fin = open("inputCYK.txt", "r")
cnt = int(fin.readline())
Map = collections.defaultdict(set)
for i in range(cnt):
    line = fin.readline().split()
    nonTerm = line[0]
    productions = line[1:]
    for prod in productions:
        Map[prod].add(nonTerm)
print(Map)

cnt = int(fin.readline())
for k in range(cnt):
    word = fin.readline().split()[0]
    #creare matrice
    table = [[0] * k for k in range(1, len(word) + 1)]
    n = len(word)

    #initializare ultima linie
    for i in range(n):
        table[n - 1][i] = Map[word[i]]

    for i in range(n - 2, -1, -1):# linii in ordine inversa
        for j in range(i + 1):# coloane in ordine normala
            length = n - i # lunigmea subsirului pe care il construiesc
            table[i][j] = set()
            for l in range(1, length):# l = lungimea primei partitii (subsirul se partitioneaza in 2 bucati)
                for first in table[n - l][j]:# linia corespunzatoare lungimii primei partitii, coloana corespunzatoare
                    for second in table[n - length + l][j + l]:
                        aux = first + second# concatenare
                        if aux in Map:
                            table[i][j] = table[i][j].union(Map[aux])# adaug neterminalele din care pot sa vin

    if 'S' in table[0][0]:
        print('DA')
    else:
        print('NU')
    print(table)
