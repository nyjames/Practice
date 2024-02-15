""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. """

# =================== Approach ======================= #
#
# You can try a two-pointer technique, and a hashmap technique,
# let's try hashmap!
#
# Start by initializing your hashmap
# 
# iterate through your nums (enumerated), so you can get both, number and index
# The diff var will determine which num we're looking for!
# 
# n - target will give us what we're looking for
# 
# if diff is in the hashMap, return the diff and the index we found it at!
# 
# if not, add those digits to the hashMap and try again, this works because
# if there is a correct answer, you will absolutely find it with this code.

# ==================== Solution ====================== #

def twoSum(self, nums, target):

   hashMap = {}

   for i, n in enumerate(nums):
      
      diff = target - n

      if diff in hashMap:

        return(hashMap[diff], i)
      
      hashMap[n] = i

# ==================== Test Cases ==================== #

print(twoSum(None,[2, 7, 11, 15], 9))

# output: [0, 1]

print(twoSum(None,[3,2,4], 6))

# output: [1,2]