
def same_vowel_group(w):
    vowels = ['a', 'e', 'i', 'u', 'o']                                ## Creating vowels

    hashtable = {}                                                    ## making a hashtable to hold evey word inside of them will be list of vowels
    for i, word in enumerate(w):
        if(word not in hashtable.keys()):                             ## non repeating words
            hashtable[word] = hashtable.setdefault(word, [])
            for char in word:
                if(char in vowels and char not in hashtable[word]):
                    hashtable[word].append(char)

    selectedWords = []                                                ## the output we want
    block = False
    for i, word in enumerate(hashtable):
        for j, otherword in enumerate(hashtable):
            block = False
            if(j == i):                                               ## we dont want the same index to match
                block = True
                continue
            else:
                if(len(hashtable[word]) == len(hashtable[otherword])):
                    for vowel in hashtable[word]:
                        if(vowel not in hashtable[otherword]):
                            block = True
                            break
            if(block == False and len(hashtable[word]) == len(hashtable[otherword])):
                selectedWords.append(word)                           ## choosing the selected indexes
                break

    if(len(selectedWords) == 0):
        selectedWords.append(w[0])

    print(selectedWords)
    return sorted(selectedWords, reverse = True)
 
w = ['bot', 'bottom', 'hoops']                                       ## test list
            
print(same_vowel_group(w))                                           ## output



