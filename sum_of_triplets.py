# =================== Question ======================= #

""" Given an array of integers arr,
write a function to compute the sum of triplets

formed by taking three consecutive elements from the array. 
The function should return a new array where each element represents
the sum of the triplet.

For instance, if the input array is [1, 2, 3, 4, 5], 
the output should be [6, 9, 12] 


where 6 corresponds to 1 + 2 + 3, 9 corresponds to 2 + 3 + 4, and 12 corresponds to 3 + 4 + 5."""

# =================== Approach ======================= #
#
# I'm going to initialize an empty list (list for Three), 
# and an empty Sum variable
#
# 
# I'm going to iterate through the arr to implement sort of a sliding window
# 
# if i is less than or equal to the index of the last element, 
# sum will = the first three numbers in the arr.
# 
# Sum will then be added to the list for three list,
# 
# I will pop the first number of arr, so that the next three will be [0], [1], [2]
# and this is how the window will slide.

# ==================== Solution ====================== #

def  sum_of_triplets(arr):

    listForThree = []
    sum = 0

    for i in range(len(arr)):
        if i <= len(arr) - 1:
            sum = arr[0] + arr[1] + arr[2]
            listForThree.append(sum)
        arr.pop(0)
    return listForThree

# ==================== Test Cases ==================== #

print(sum_of_triplets([1,2,3,4,5]))

# output: [6, 9, 12]

print(sum_of_triplets([4,6,3,8,10]))




