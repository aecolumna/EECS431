def binarySearchDistance(arr, x):
    l = 0
    r = len(arr) - 1

    if x > arr[r]:
        return x - arr[r]

    if x < arr[l]:
        return arr[l] - x

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return 0

        elif arr[mid] < x:
            l = mid + 1

        else:
            r = mid - 1

    n1 = arr[l] - x
    n2 = x - arr[r]
    return min(n1, n2)

arr = [6, 25, 30, 41, 61, 90, 91, 93, 97]

print(7, binarySearchDistance(arr, 7))