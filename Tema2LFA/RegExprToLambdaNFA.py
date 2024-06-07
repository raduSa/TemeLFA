import collections
cnt = [0]


class Node:
    def __init__(self, val):
        self.val = val
        self.edges = collections.defaultdict(set)


class Graph:
    def __init__(self, counter):
        self.startNode = Node(counter[0] + 1)
        self.finalNode = Node(counter[0] + 2)
        counter[0] += 2

    @staticmethod
    def createEmptyExpr():
        graph = Graph(cnt)
        graph.startNode.edges['0'].add(graph.finalNode)
        return graph

    @staticmethod
    def createSymbol(symbol):
        graph = Graph(cnt)
        graph.startNode.edges[symbol].add(graph.finalNode)
        return graph

    @staticmethod
    def createUnion(graph1, graph2):
        newGraph = Graph(cnt)
        newGraph.startNode.edges['0'].add(graph1.startNode)
        newGraph.startNode.edges['0'].add(graph2.startNode)
        graph1.finalNode.edges['0'].add(newGraph.finalNode)
        graph2.finalNode.edges['0'].add(newGraph.finalNode)
        del graph1
        del graph2
        return newGraph

    @staticmethod
    def createConcatenation(graph1, graph2):
        newGraph = Graph(cnt)
        newGraph.startNode = graph1.startNode
        graph1.finalNode.edges['0'].add(graph2.startNode)
        newGraph.finalNode = graph2.finalNode
        del graph1
        del graph2
        return newGraph

    @staticmethod
    def createStarExpr(graph1):
        newGraph = Graph(cnt)
        newGraph.startNode.edges['0'].add(graph1.startNode)
        newGraph.startNode.edges['0'].add(newGraph.finalNode)
        graph1.finalNode.edges['0'].add(graph1.startNode)
        graph1.finalNode.edges['0'].add(newGraph.finalNode)
        del graph1
        return newGraph

    @staticmethod
    def parseExpression():  # reverse Polish notation
        graphStack = list()
        with open("input3.txt", "r") as fin:
            s = fin.readline()
        for ltr in s:
            if ltr == '*':
                graph1 = graphStack.pop()
                newGraph = Graph.createStarExpr(graph1)
                graphStack.append(newGraph)
            elif ltr == '|':
                graph1, graph2 = graphStack.pop(), graphStack.pop()
                newGraph = Graph.createUnion(graph1, graph2)
                graphStack.append(newGraph)
            else:
                newGraph = Graph.createSymbol(ltr)
                graphStack.append(newGraph)

        q = collections.deque(graphStack)
        while len(q) > 1:
            graph1, graph2 = q.popleft(), q.popleft()
            newGraph = Graph.createConcatenation(graph1, graph2)
            q.appendleft(newGraph)
        return q.pop()

    def bfs(self):
        q = collections.deque([self.startNode])
        visited = set()
        while q:
            curr = q.popleft()
            for ltr in curr.edges.keys():
                for node in curr.edges[ltr]:
                    print(curr.val, node.val, ltr)
                    if node not in visited:
                        visited.add(node)
                        q.append(node)


graph = Graph.parseExpression()
graph.bfs()
print(graph.finalNode.val)
