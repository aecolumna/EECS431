from copy import deepcopy

nums = [1, 2,3,4]


# index=0, arr=[] by default
def f(index, arr):
    if index >= len(nums):
        print(arr)
        return


    a2 = deepcopy(arr)
    a2.append(nums[index])
    f(index + 1, a2)

    f(index + 1, arr)



myarr = []
f(0, myarr)
