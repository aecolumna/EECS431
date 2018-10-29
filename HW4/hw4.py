from collections import namedtuple
from itertools import chain, combinations

"""
Find minimum covering set
"""

Candidate = namedtuple("Candidate",['identifier','skills','numSkills'])


#input start
n, k = [int(i) for i in input().split()]

skillsSet = set(input().split())

candidatesArr = [None] * n

for i in range(n):
    num = int(input())
    candidateSet = set(input().split())
    candidatesArr[i] = Candidate(i ,candidateSet, num)

#input end

def Powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# sort by number of skills
# Open to further optimization
candidatesArr = sorted(candidatesArr, reverse=True, key=lambda x: x.numSkills)

s = set()

for subset in Powerset(candidatesArr):
    s.clear()

    for candidate in subset:
        s |= candidate.skills

    if s == skillsSet:
        print(len(subset))
        break










