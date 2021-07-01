# Python program to check whether two strings are
# anagrams of each other
 
# function to check whether two strings are anagram
# of each other

# this function will take the array of string

def anagrams(texts: list):
    res = []
    angrm = texts[0]
    true = True
    i = 0
    while true:
        for j in texts:
            if sorted(j) == sorted(angrm) and j != angrm:
                res.append(angrm)
                texts.remove(angrm)
                i = i - 1
                break

        i = i + 1
        angrm = texts[i]

        if i == len(texts) - 1:
            true = False

    return res

ans = anagrams(['code', 'listen', 'forgeeksgeeks',  'are', 'deco', 'geeksforgeeks', 'rae', 'codes', 'sodec', 'silent'])
print(ans)
print(list(range(6, 21)))