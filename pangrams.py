"""A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog"
is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram.
Return True if it is, False if not. 

Ignore numbers and punctuation."""

# =================== Approach ======================= #
#
# I'm going to initialize an empty set (this is because sets are unordered)
# I wanted to avoid using the sorted function.
# 
# I'm gonna initalize alpha as the alphabet (thought it was fitting)
# 
# I'll iterate through the sentence, and if c is an alphabet character,
# I want to add it to my set. (Casefold means it'll be added as an lowercase.)
#
# ill return the comparison result of random_set, to set(alpha).
# Since it'll be unordered, if it's the same, it'll return true in the same order!
#
# ==================== Solution ====================== #
def solution(sentence):
    alpha = "abcdefghijklmnopqrstuvwxyz"

    random_set = set()
    for c in sentence:
        if c.isalpha():
            random_set.add(c.casefold())

    return(random_set == set(alpha))

# ==================== Test Cases ==================== #

print(solution("The quick brown fox jumps over the lazy dog"))

# output: True

print(solution("Sphinx of black quartz, judge my vow."))

        
