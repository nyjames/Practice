"""Complete the solution so that it returns true if it contains any duplicate argument values.
 Any number of arguments may be passed into the function.

The array values passed in will only be strings or numbers.
 The only valid return values are true and false."""

# reminds me of a contains duplicate problem
# contains duplicate was completed with a set (set's are unordered and no dupes are allowed)

# initialize empty set
# for each number in arr, 
# if number is in set,
# return true, else false

def solution(*args):

    emp_set = set()

    for num in args:
        if num  in emp_set:
            return True
        emp_set.add(num)
    return False

print(solution(1, 2, 3, 2))