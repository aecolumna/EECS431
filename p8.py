from heapq import _heappop_max, _heapify_max, _siftup_max, _siftup, _heapreplace_max, _siftdown_max, heappush, heappop,heapreplace

def _heappushMax(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown_max(heap, 0, len(heap)-1)

def getMedian(smallMaxHeap, bigMinHeap):
    if not smallMaxHeap and not bigMinHeap:
        print("None")
    elif len(smallMaxHeap) == len(bigMinHeap):
        print(int(smallMaxHeap[0] + bigMinHeap[0])/2)
        return int(smallMaxHeap[0] + bigMinHeap[0])/2
    elif len(smallMaxHeap) > len(bigMinHeap):
        print(smallMaxHeap[0])
        return smallMaxHeap[0]
    else:
        print(bigMinHeap[0])
        return bigMinHeap[0]


import random
from statistics import median

def remove(smallMaxHeap, bigMinHeap, x):
    print("ran remove")

    if x <= smallMaxHeap[0]:
        try:
            index = smallMaxHeap.index(x)
        except:
            print("Wrong!")
            return

        if index == (len(smallMaxHeap) - 1):
            smallMaxHeap.pop()
        else:
            smallMaxHeap[index] = smallMaxHeap.pop()
            _siftup_max(smallMaxHeap, index)

    elif x >= smallMaxHeap[0]:
        try:
            index = bigMinHeap.index(x)
        except:
            print("Wrong!")
            return

        if index == (len(bigMinHeap) - 1):
            bigMinHeap.pop()
        else:
            bigMinHeap[index] = bigMinHeap.pop()
            _siftup(bigMinHeap, index)

    # rebalance everything
    if len(smallMaxHeap) > (len(bigMinHeap) + 1):
        item = _heappop_max(smallMaxHeap)
        heappush(bigMinHeap, item)
    elif len(bigMinHeap) > (len(smallMaxHeap) + 1):
        item = heappop(bigMinHeap)
        _heappushMax(smallMaxHeap, item)


bigMinHeap = []
smallMaxHeap = []
testArr = []

lenMin = len(bigMinHeap)
lenMax = len(smallMaxHeap)  # minHeap always make it negative!!

randomArr = [random.randint(1,100) for i in range(100)]
#randomArr = [31, 69, 4, 85, 68, 45, 93, 8, 22, 3, 49, 56, 36, 17, 94, 22, 80, 14, 37, 8, 69, 59, 56, 45, 80, 81, 14, 79, 43, 75, 22, 13, 56, 92, 62, 18, 31, 94, 5, 46, 15, 90, 37, 9, 74, 90, 61, 17, 61, 85, 17, 37, 20, 88, 1, 76, 22, 75, 95, 72, 67, 10, 54, 89, 28, 13, 5, 67, 1, 20, 65, 15, 99, 34, 93, 60, 96, 42, 64, 62, 70, 22, 34, 9, 15, 1, 71, 39, 69, 13, 70, 96, 33, 50, 28, 64, 23, 98, 81, 74]
counter = 0

for i in randomArr:
    if testArr:

        getMedian(smallMaxHeap,bigMinHeap)
        counter+=1


    print(smallMaxHeap[::-1], " :: ", bigMinHeap)

    if smallMaxHeap and bigMinHeap:
        myMedian = float(getMedian(smallMaxHeap, bigMinHeap))
        officialMedian = median(testArr)
        print("i = ", i, " ", end=" ")
        print(" mine: ", myMedian, " official: ", officialMedian)
        assert( myMedian == median(testArr))


    testArr.append(i)
    # empty case
    if len(smallMaxHeap) == 0 and len(bigMinHeap) == 0:
        _heappushMax(smallMaxHeap, i)
        continue

    leftVal = smallMaxHeap[0]

    # equal size case
    if len(smallMaxHeap) == len(bigMinHeap):
        if i <= leftVal:
            _heappushMax(smallMaxHeap, i)
        else:
            heappush(bigMinHeap, i)
        continue

    # left one is bigger
    if len(smallMaxHeap) > len(bigMinHeap):
        if i >= leftVal:
            heappush(bigMinHeap, i)
        elif i >= smallMaxHeap[0] and i <= bigMinHeap[0]:
            heappush(bigMinHeap, i)
        elif i <= leftVal:
            hold = _heapreplace_max(smallMaxHeap, i)
            heappush(bigMinHeap, hold)


        continue

    # right one is bigger
    if len(smallMaxHeap) < len(bigMinHeap):
        if i <= bigMinHeap[0]:
            _heappushMax(smallMaxHeap, i)

        elif i >= bigMinHeap[0]:
            hold = heapreplace(bigMinHeap, i)
            _heappushMax(smallMaxHeap, hold)



        continue