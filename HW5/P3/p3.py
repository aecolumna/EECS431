# 10/8/18

from collections import deque

numVertices, edges = (int(i) for i in input().split())

# implicit dictionary mapping index i.e. vertex to adjacency list
dic = [[] for i in range(numVertices)]

vertices = list(range(numVertices))

for _ in range(edges):
    a, b = (int(i) for i in input().split())
    dic[a].append(b)
    dic[b].append(a)

# breadth first search
def bfs(vertices, dic):
    clusters = 0
    visited = set()
    deck = deque()

    while vertices:
        deck.append(vertices[0])

        while deck:
            v = deck.popleft()
            for neighbor in dic[v]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    deck.append(neighbor)
        # vertices not reached are in different cluster
        vertices = list(set(vertices) - visited)
        clusters += 1

    print(clusters)

bfs(vertices, dic)




