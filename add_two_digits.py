"""You are given a two-digit integer n. Return the sum of its digits.

For n = 29, the output should be
    solution(n) = 11. """

# =================== Approach ======================= #
#
# I'm going to convert n into a string
# so I can iterate through it with string manipulation
# 
# I'm going to initialize an empty sum,
# when I iterate through the string,
# it'll add the int number to the sum
#
# Return the sum of two of the numbers
#
# ==================== Solution ====================== #

def solution(n):

    n_str = str(n)
    sum = 0
    for c in n_str:
        sum += int(c)
        
    return sum
    

# ==================== Test Cases ==================== #

print(solution(29))

# output: 11

print(solution(1203405))

# output: 15

print(solution(52))

# Output: 7