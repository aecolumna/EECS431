def merge(arr, arr2):
    arr3 = []

    i = 0  # index counter for arr1
    j = 0  # index counter for arr2
    k = 0  # " " for arr3

    len3 = len(arr1) + len(arr2)

    while (k < len3):

        if i >= len(arr1):
            arr3.append(arr2[j])
            j += 1

        elif j >= len(arr2):
            arr3.append(arr1[i])
            i += 1

        # case 1
        elif arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        # case 2
        elif arr2[j] < arr1[i]:
            arr3.append(arr2[j])
            j += 1

        k += 1
    return arr3


def merge_sort(a, n):
    if n < 2:
        return

    m = n // 2
    merge_sort(a, m)
    merge_sort(a + m, n - m)
    merge(a, n, m)


arr = [92, 86, 98, 91, 67, 12, 71, 36, 39, 7]

merge_sort(0, len(arr), arr)
print(arr)