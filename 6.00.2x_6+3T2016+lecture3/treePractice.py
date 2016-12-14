"""
Recreated some of the methods in lecture3segment3 class notes for practice.
"""

from lecture3segment3.lecture3_segment3 import *


def buildChineseCityGraph(graphType):
    g = graphType()
    for city in ('Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'HongKong', 'Chengdu'):
        g.addNode(Node(city))

    g.addEdge(Edge(g.getNode('Chengdu'), g.getNode('Beijing')))
    g.addEdge(Edge(g.getNode('Shanghai'), g.getNode('Beijing')))
    g.addEdge(Edge(g.getNode('Beijing'), g.getNode('Guangzhou')))
    g.addEdge(Edge(g.getNode('Shanghai'), g.getNode('Chengdu')))
    g.addEdge(Edge(g.getNode('Chengdu'), g.getNode('Shenzhen')))
    g.addEdge(Edge(g.getNode('Guangzhou'), g.getNode('Shanghai')))
    g.addEdge(Edge(g.getNode('Shenzhen'), g.getNode('Guangzhou')))
    g.addEdge(Edge(g.getNode('HongKong'), g.getNode('Shenzhen')))
    g.addEdge(Edge(g.getNode('Shanghai'), g.getNode('HongKong')))

    return g


def DFS(graph, start, end, path, shortest, toPrint=False):
    path = path + [start]
    if toPrint:
        print('Current DFS path: ', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest is None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
            if newPath is not None:
                shortest = newPath
        elif toPrint:
            print('Already visited', node)
    return shortest


def shortestPathDFS(graph, start, end, toPrint=False):
    return DFS(graph, start, end, [], None, toPrint)


def testSPDFS(source, destination):
    g = buildChineseCityGraph(Digraph)
    sp = shortestPathDFS(g, g.getNode(source), g.getNode(destination), toPrint=True)
    if sp is not None:
        print('Shortest path from ', source, ' to ', destination, ' is ', printPath(sp))
    else:
        print('There is no path from ', source, ' to ', destination)


def BFS(graph, start, end, toPrint=False):
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)

        if toPrint:
            print('Current BFS path: ', printPath(tmpPath))

        lastNode = tmpPath[-1]

        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            newPath = tmpPath + [nextNode]
            pathQueue.append(newPath)
    return None


def shortestPathBFS(graph, start, end, toPrint=False):
    return BFS(graph, start, end, toPrint)


def testSPBFS(source, destination):
    g = buildChineseCityGraph(Digraph)
    sp = shortestPathBFS(g, g. getNode(source), g.getNode(destination), toPrint=True)
    if sp is not None:
        print('Shortest path from ', source, ' to ', destination, ' is ', printPath(sp))
    else:
        print('There is no path from ', source, ' to ', destination)

if __name__ == '__main__':
    testSPDFS('Shanghai', 'Shenzhen')
    testSPBFS('Shanghai', 'Shenzhen')
