# Sum of Triplets:
# Given an array of integers arr, write a function to compute the sum of triplets formed by taking
#  three consecutive elements from the array. The function should return a new array where each element represents
# the sum of the triplet. For instance, if the input array is [1, 2, 3, 4, 5], the output should be [6, 9, 12] 
# where 6 corresponds to 1 + 2 + 3, 9 corresponds to 2 + 3 + 4, and 12 corresponds to 3 + 4 + 5.

def  sum_of_triplets(arr):

    listForThree = []
    sum = 0

    for i in range(len(arr)):
        if i <= len(arr) - 1:
            sum = arr[0] + arr[1] + arr[2]
            listForThree.append(sum)
        arr.pop(0)
    return listForThree

print(sum_of_triplets([1,2,3,4,5]))




