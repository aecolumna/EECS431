from collections import namedtuple, Counter
from itertools import chain, combinations

from_iter = chain.from_iterable


"""
Find minimum covering set
"""

Candidate = namedtuple("Candidate",['identifier','skills','numSkills','remove'])

allSkillsArr = []

lenMinCover = 0

#input start
n, k = [int(i) for i in input().split()]

skillsSet = set(input().split())

candidatesArr = [None] * n

for i in range(n):
    num = int(input())
    arr = input().split()
    allSkillsArr.extend(arr) # add to the tracker of all skills
    candidatesArr[i] = set(arr)

countDict = Counter(allSkillsArr)

uniqueSkills = [skill for skill, num in countDict.items() if num == 1 ]

newCandidatesArr = []

# iterate through candidates
for candidate in candidatesArr:
    flag = False
    for skill in uniqueSkills:
        if skill in candidate:
            flag = True
            skillsSet -= candidate # remove skills possesed by dude whos definitely going
            lenMinCover += 1
            break
    if flag is False:
        newCandidatesArr.append(candidate)

candidatesArr = newCandidatesArr

def Powerset(s):
    return from_iter(combinations(s, r) for r in range(len(s)+1))

# sort by number of skills
# Open to further optimization
candidatesArr = sorted(candidatesArr, reverse=True, key=lambda x: len(x))

for subset in Powerset(candidatesArr):

    s = set().union(*subset)

    if s >= skillsSet:
        lenMinCover += len(subset)
        print(lenMinCover)
        break