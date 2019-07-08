def distance_to_nearest_vowel(txt):
    vov = ['a', 'e', 'i', 'o', 'u']

    distanceList = []
    IsFirstItemNotVowel = False
    
    for i, char in enumerate(txt):
        if(char in vov):
            distanceList.append(0)
            for j in range(i-1,-1,-1):
                if(IsFirstItemNotVowel):
                    distanceList[j] = i-j
                else:
                    if(distanceList[j] > i-j):
                        distanceList[j] = i-j
        else:
            if(len(distanceList) == 0):
                IsFirstItemNotVowel = True
                distanceList.append(1)
            else:
                distanceList.append(distanceList[-1] + 1)

    return distanceList

# print(distance_to_nearest_vowel("aaaaa"))
# print(distance_to_nearest_vowel("babbb"))
# print(distance_to_nearest_vowel("abcdabcd"))
# print(distance_to_nearest_vowel("shopper"))
print(distance_to_nearest_vowel("bba"))