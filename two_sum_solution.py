def twoSum(self, nums, target):

        hashMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return([diff], i)
        hashMap.update(n)

nums = [2, 7, 11, 15]
target = 9

print(twoSum(None, nums, target))