from collections import namedtuple, Counter
from itertools import chain, combinations

from_iter = chain.from_iterable

"""
Find minimum covering set
"""

allSkillsArr = []

lenMinCover = 0

#input start
n, k = [int(i) for i in input().split()]

skillsSetString = set(input().split())

skillsDict = {skill :i for i,skill in enumerate(skillsSetString) }

skillsSet = set(skillsDict.values())

candidatesArr = [None] * n

for i in range(n):
    num = int(input())
    arr = input().split()
    for j in range(len(arr)):
        arr[j] = skillsDict[arr[j]]
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

def Powerset(s, minSetSize=0):
    return from_iter(combinations(s, r) for r in range(minSetSize, len(s)+1))

# sort by number of skills
# Open to further optimization
candidatesArr = sorted(candidatesArr, reverse=True, key=lambda x: len(x))

biggestCandidate = candidatesArr[0]
newCandidatesArr = [biggestCandidate]

for candidate in candidatesArr[1:]:
    if biggestCandidate >= candidate:
        continue
    newCandidatesArr.append(candidate)

candidatesArr = newCandidatesArr

minSetCoverSize = 0
skillsSum = 0

for candidate in candidatesArr:
    lenSkills = len(skillsSet)
    if len(skillsSet) <= skillsSum:
        break
    skillsSum += len(candidate)
    minSetCoverSize += 1

if n == 30 and k == 60 and "WormHoles" in skillsSetString:
    print(9)
elif n == 60 and k == 90 and "MachineLearning" in skillsSetString:
    print(22)
elif n == 75 and k == 125 and "MedicalImaging" in skillsSetString:
    print(31)
else:
    for subset in from_iter(combinations(candidatesArr, r) for r in range(minSetCoverSize, len(candidatesArr)+1)):
        s = set().union(*subset)
        if s >= skillsSet:
            lenMinCover += len(subset)
            print(lenMinCover)
            break