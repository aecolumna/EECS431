
nodes, edges = (int(i) for i in input().split())

dic = {i : set() for i in range(nodes)}

for _ in range(edges):
    a, b = (int(i) for i in input().split())
    dic[a].add(b)
    dic[b].add(a)



maxSetLen = 0

for vertex, vSet in dic.items():
    for v2 in vSet:
        tempLen = len(vSet | dic[v2])
        if tempLen > maxSetLen:
            maxSetLen = tempLen

print((maxSetLen - 1) * maxSetLen  // 2)












