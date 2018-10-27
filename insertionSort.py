
def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        val = arr[i]
        while j > 0 and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = val

arr = [92, 86, 98, 91, 67, 12, 71, 36, 39, 7]

insertionSort(arr)
print(arr)