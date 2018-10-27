from optimization import Food, buildMenu

def maxVal(toConsider, avail):
    if toConsider == [] or avail == 0:
        result = (0, ())

    elif toConsider[0].getCost() > avail:
        # explore right branch only
        result = maxVal(toConsider[1:], avail)
        # avail doesn't change since were not adding item
        # decrease size of to Consider by 1

    else:
        nextItem = toConsider[0]

        #explore left branch
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())

        withVal += nextItem.getValue()

        #explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)

        #choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + nextItem)
        else:
            result = (withoutVal, withoutToTake)




