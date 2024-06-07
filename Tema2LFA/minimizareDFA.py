import collections


class Graph:
    def __init__(self):
        self.edges = collections.defaultdict(dict)
        self.edgesRev = collections.defaultdict(dict)
        self.S = None
        self.Fin = set()
        self.visitedRev = set()
        self.visited = set()
        self.newGraph = collections.defaultdict(dict)
        self.newFin = set()

    def readGraph(self, fileName):
        fin = open("input.txt", "r")
        self.S = int(fin.readline())
        self.Fin = {int(x) for x in fin.readline().split()}
        for line in fin.readlines():
            start, end, letter = line.split()
            self.edges[int(start)][letter] = int(end)
            if letter in self.edgesRev[int(end)]:
                self.edgesRev[int(end)][letter].add(int(start))
            else:
                self.edgesRev[int(end)][letter] = {int(start)}

    def printGraph(self):
        print(self.edges)

    def dfs(self, curr):
        if curr in self.visited:
            return True
        if curr not in self.visitedRev:
            return False
        ok = False
        self.visited.add(curr)
        for ltr in self.edges[curr].keys():
            if self.dfs(self.edges[curr][ltr]):
                self.newGraph[curr][ltr] = self.edges[curr][ltr]
                ok = True
        if curr in self.Fin:
            self.newFin.add(curr)
            return True
        return ok

    def dfsRev(self, curr):
        if curr in self.visitedRev:
            return True
        ok = False
        self.visitedRev.add(curr)
        for ltr in self.edgesRev[curr].keys():
            for node in self.edgesRev[curr][ltr]:
                if self.dfsRev(node):
                    ok = True
        if curr == self.S:
            return True
        return ok

    def getValidNodes(self):
        for finalNode in self.Fin:
            self.dfsRev(finalNode)
        self.dfs(self.S)

    def minimizeDFA(self):
        nodes = {node for node in self.newGraph.keys()}
        nodes = nodes.union(self.newFin)
        nodes = list(nodes)
        matrix = [[0] * len(nodes) for i in range(len(nodes))]
        deleted = set()
        ok = True
        while ok:
            ok = False
            for i in range(len(nodes) - 1):
                for j in range(i + 1, len(nodes)):
                    if i not in deleted and j not in deleted and self.newGraph[nodes[i]] == self.newGraph[nodes[j]]:
                        ok = True
                        del self.newGraph[i]
                        deleted.add(i)
                        for node in self.newGraph.keys():
                            for ltr in self.newGraph[node].keys():
                                if i == self.newGraph[node][ltr]:
                                    self.newGraph[node][ltr] = j
                        if i == self.S:
                            self.S = j
                        if i in self.newFin:
                            self.newFin.remove(i)
                            self.newFin.add(j)


graph = Graph()
graph.readGraph("input.txt")
graph.getValidNodes()
graph.minimizeDFA()
print(graph.newGraph, graph.S, graph.newFin)
