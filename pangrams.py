'''A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. 
Ignore numbers and punctuation.'''

# initialize empty list
# compare sentence, put in new string if alphanumeric chars (string = x)
# sort x and change it to lowercase
# compare it to "abcdefghijklmnopqrstuvwxyz"
# if both strings are equal = return true
# return false otherwise


alpha = "abcdefghijklmnopqrstuvwxyz"
sentence = "The quick brown fox jumps over the lazy dog"
random_set = set()
for c in sentence:
    if c.isalpha():
        random_set.add(c.casefold())

print(random_set == set(alpha))


        
