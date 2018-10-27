def helper(given_array,subset=9, i=0):
    if subset == 9:
        subset = [None] * len(given_array)

    if i == len(given_array):
        lst = [i for i in subset if i]
        yield lst

    else:
        subset[i] = None
        helper(given_array,subset, i + 1)
        subset[i] = given_array[i]
        helper(given_array, subset, i + 1)



list(helper([1,2,3,4]))
