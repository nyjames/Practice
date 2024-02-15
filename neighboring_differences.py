# Neighboring Differences:
# Create a function that takes an array of integers nums
# as input and returns a new array diff where each element
# diff[i] represents the absolute difference between nums[i] and nums[i+1].
# Ensure that the array diff has one less element than the input array nums.
# [1,2,3,4,5]

def neighboring_differences(nums):
    diff = []

    for i in range(len(nums)-1): 
                difference = abs(nums[i] - nums[i + 1])
                diff.append(difference)
            
    print(diff)

print(neighboring_differences([1,2,3,4,5]))

# output: 1, 1, 1, 1



