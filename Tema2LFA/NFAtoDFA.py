import collections


class Graph:
    def __init__(self):
        self.edges = collections.defaultdict(dict)
        self.S = None
        self.Fin = set()
        self.alphabet = list()

    def readGraph(self, fileName):
        fin = open("input2.txt", "r")
        self.S = int(fin.readline())
        self.Fin = {int(x) for x in fin.readline().split()}
        self.alphabet = [x for x in fin.readline().split()]
        for line in fin.readlines():
            start, end, letter = line.split()
            if letter in self.edges[int(start)]:
                self.edges[int(start)][letter].add(int(end))
            else:
                self.edges[int(start)][letter] = {int(end)}

    def getDFA(self):
        newFin = set()
        visited = set()
        q = collections.deque()
        startPos = [self.S]
        q.append(tuple(startPos))

        while q:
            curr = q.popleft()
            visited.add(curr)
            for ltr in self.alphabet:
                newState = set()
                for node in curr:
                    if ltr in self.edges[node]:
                        newState = newState.union(self.edges[node][ltr])
                for node in self.Fin:
                    if node in newState:
                        newFin.add(tuple(newState))
                        break
                newState = tuple(newState)
                print(curr, newState, ltr)
                if newState not in visited:
                    q.append(newState)
        print(f"Noi noduri finale: {newFin}")


graph = Graph()
graph.readGraph("input2.txt")
graph.getDFA()
