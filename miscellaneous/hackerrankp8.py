from heapq import _heappop_max, _heapify_max, _siftup_max, _siftup, _heapreplace_max, _siftdown_max, heappush, heappop,heapreplace

def _heappushMax(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown_max(heap, 0, len(heap)-1)

def getMedian(smallMaxHeap, bigMinHeap):
    if not smallMaxHeap and not bigMinHeap:
        print("Wrong!")
    elif len(smallMaxHeap) == len(bigMinHeap):
        n = (smallMaxHeap[0] + bigMinHeap[0]) / 2
        if isinstance(n, float) and n.is_integer():
            n = int(n)

        print(n)

    elif len(smallMaxHeap) > len(bigMinHeap):
        print(smallMaxHeap[0])

    else:
        print(bigMinHeap[0])


def remove(smallMaxHeap, bigMinHeap, x):

    if not smallMaxHeap and not bigMinHeap:
        print("Wrong!")
        return False
    if x <= smallMaxHeap[0]:
        try:
            index = smallMaxHeap.index(x)
        except:
            print("Wrong!")
            return False

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
            return False

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

    return True





bigMinHeap = []
smallMaxHeap = []

lenMin = len(bigMinHeap)
lenMax = len(smallMaxHeap)  # minHeap always make it negative!!

loops = int(input())







for _ in range(loops):
    a, b = input().split()
    strOperation = str(a)
    i = int(b)


    if strOperation == 'r':
        success = remove(smallMaxHeap, bigMinHeap, i)
        if success:
            getMedian(smallMaxHeap, bigMinHeap)
        continue



    # empty case
    if len(smallMaxHeap) == 0 and len(bigMinHeap) == 0:
        _heappushMax(smallMaxHeap, i)
        getMedian(smallMaxHeap, bigMinHeap)
        continue

    leftVal = smallMaxHeap[0]

    # equal size case
    if len(smallMaxHeap) == len(bigMinHeap):
        if i <= leftVal:
            _heappushMax(smallMaxHeap, i)
        else:
            heappush(bigMinHeap, i)
        getMedian(smallMaxHeap, bigMinHeap)
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
        getMedian(smallMaxHeap, bigMinHeap)
        continue

    # right one is bigger
    if len(smallMaxHeap) < len(bigMinHeap):
        if i <= bigMinHeap[0]:
            _heappushMax(smallMaxHeap, i)

        elif i >= bigMinHeap[0]:
            hold = heapreplace(bigMinHeap, i)
            _heappushMax(smallMaxHeap, hold)
        getMedian(smallMaxHeap, bigMinHeap)
        continue