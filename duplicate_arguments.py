"""Complete the solution so that it returns true if it contains any duplicate argument values.
 Any number of arguments may be passed into the function.

The array values passed in will only be strings or numbers.
 The only valid return values are true and false."""

# =================== Approach ======================= #
#
# I'm to initialize an empty set or a hashset,
# This is because a hashset will not allow duplicates
# 
# I'm going to iterate through the numbers given through the argument,
# if the number is already in the set, return True (Because it'll be a dupe)
# if no duplicates are found, it'll return false
#
#
# ==================== Solution ====================== #
def solution(*args):

    emp_set = set()

    for num in args:
        if num  in emp_set:
            return True
        emp_set.add(num)
    return False

# ==================== Test Cases ==================== #

print(solution(1, 2, 3, 2))

# Output: True

print(solution(1, 2, 3, 4))

# Output: False

print(solution(1, 1, 1, 1))

# Output: True

print(solution(-1, 2, 3, 1))

# Output: True

# ==================================================== #