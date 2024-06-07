import collections
fin = open("input.txt", "r")
startNode = int(fin.readline())
Fin = {int(x) for x in fin.readline().split()}
graph = collections.defaultdict(dict)

cnt = int(fin.readline())
for i in range(cnt):
    line = fin.readline()
    start, end, ltr, stackPop, stackAppend = line.split()
    if ltr not in graph[int(start)]:
        graph[int(start)][ltr] = {stackPop: (int(end), stackAppend)}
    else:
        graph[int(start)][ltr][stackPop] = (int(end), stackAppend)
#print(graph)
#lambda = '0'

cnt = int(fin.readline())
for i in range(cnt):
    stack = ['Z']
    currNode = startNode
    word = fin.readline().strip()
    index = 0
    while True:
        if index < len(word): # daca nu mai am litere in cuvant
            ltr = word[index]
        else:
            ltr = '0' # mai verific daca sunt muchii cu lambda
        if stack:
            if ltr in graph[currNode]:
                aux = graph[currNode][ltr][stack[-1]]
            else:
                break
            stack.pop()
            currNode = aux[0]
            if aux[1] != '0':
                for symbol in aux[1][::-1]:
                    stack.append(symbol)
        else:
            break
        index += 1
    if currNode in Fin and not stack:
        print('DA')
    else: print('NU')