# =================== Question ======================= #

"""Create a function that takes an array of integers nums as input and
 returns a new array diff where each element

# diff[i] represents the absolute difference between nums[i] and nums[i+1].
# Ensure that the array diff has one less element than the input array nums.
"""
# =================== Approach ======================= #
#
# I'm going to initialize an empty list
# 
# I'm going to iterate through nums and save a variable: Difference
#
# Difference will change every loop to the result of
# the current number - the number to the right.
#
# I'll append difference to diff and return it!
#
# ==================== Solution ====================== #

def neighboring_differences(nums):
    diff = []

    for i in range(len(nums)-1): 
                difference = abs(nums[i] - nums[i + 1])
                diff.append(difference)
            
    return(diff)

# ==================== Test Cases ==================== #

print(neighboring_differences([1,2,3,4,5]))

# output: [1, 1, 1, 1]

print(neighboring_differences([1,3,5,7,9]))

# output: [2, 2, 2, 2]

print(neighboring_differences([50,75,125,150,200]))


