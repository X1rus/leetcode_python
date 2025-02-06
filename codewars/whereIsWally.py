'''

Write a function that returns the index of the first occurrence of the word "Wally".

"Wally" must not be part of another word, but it can be directly followed by a punctuation mark.

If no such "Wally" exists, return -1.

Examples:
"Wally" --> 0
"Where's Wally" --> 8
"Where's Waldo" --> -1
"DWally Wallyd .Wally" --> -1
"Hi Wally." --> 3
"It's Wally's." --> 5
"Wally Wally" --> 0
"'Wally Wally" --> 7

'''


def wheres_wally(s):
    words = s.split()

    index = 0
    for word in words:
        clean_word = word.rstrip(".,!?")
        if clean_word == "Wally":
            return s.index(word, index)
        index += len(word) + 1

    return -1



print(wheres_wally("It's Wally's."))
print(wheres_wally("'Wally Wally"))