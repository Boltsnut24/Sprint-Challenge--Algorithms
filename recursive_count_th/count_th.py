'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #base case, original string is now smaller than 2 chars
    if(len(word) < 2):
        return 0
    
    #check first two chars of string for equality to "th"
    #if true, increment by 1 and remove them from string
    #if false, don't increment and remove only first char from string
    if (word[0] == "t" and word[1] == "h"):
        return count_th(word[2:])+1
    else:
        return count_th(word[1:])


