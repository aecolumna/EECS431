


def all_subsets(given_array):
    subset = [None] * len(given_array)


    def helper(subset, i):
        if i == len(given_array):
            print(subset)
            return


        subset[i] = None
        helper(subset, i + 1)
        subset[i] = given_array[i]
        helper(subset, i + 1)

    helper(subset, 0)





all_subsets([1,2,3,4])