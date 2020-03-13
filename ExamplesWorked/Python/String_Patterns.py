wordLen = int(input())
maxVowels = int(input())



def calculateWays(wordLen, maxVowels):
    if wordLen == 1 and maxVowels == 0:
        print("there is only 21")
    elif wordLen == 1 and maxVowels == 1:
        a = 26
    elif wordLen > 1 and maxVowels == 0:
        a = 21**wordLen
    elif wordLen > 1 and maxVowels > 0:
        x = 21**wordLen
        y = (21**(wordLen-maxVowels))*(maxVowels*5)
        z = (21**(wordLen-maxVowels))+(maxVowels*10*5)+34
        print(x,y,z)
        a = x+y+z
        print("there are only",a)
    return a

calculateWays(wordLen, maxVowels)