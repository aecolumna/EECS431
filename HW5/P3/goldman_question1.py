def winner(erica, bob):

    ericaDict = {'S' : 0, 'E' : 0, 'M' : 0, 'H' : 0}
    bobDict = {'S' : 0, 'E' : 0, 'M' : 0, 'H' : 0}

    pointsDict = {'S' : 0, 'E' : 1, 'M' : 3, 'H' : 5}

    ericaPoints = 0
    bobPoints = 0


    # Populate scores
    for i in range(len(erica)):
        ericaPoints += pointsDict[erica[i]]
        ericaDict[erica[i]] += 1

        bobPoints += pointsDict[bob[i]]
        bobDict[bob[i]] += 1


    if ericaPoints > bobPoints:
        return "Erica"
    elif bobPoints > ericaPoints:
        return "Bob"

    if ericaDict['H'] > bobDict['H']:
        return "Erica"
    elif bobDict['H'] > ericaDict['H']:
        return "Bob"

    if ericaDict['M'] > bobDict['M']:
        return "Erica"
    elif bobDict['M'] > ericaDict['M']:
        return "Bob"

    return "Tie"


erica = "EEMEE"
bob = "EESSH"

print(winner(erica, bob))