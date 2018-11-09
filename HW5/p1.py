
nodes, edges = (int(i) for i in input().split())

frequencies = [0] * nodes # index of node -> element. Value of node -> multiplicity

for _ in range(edges):
    a, b = (int(i) for i in input().split())
    frequencies[a] += 1
    frequencies[b] += 1

maxFreq = max(frequencies) + 1
print((maxFreq - 1) * maxFreq  // 2)







