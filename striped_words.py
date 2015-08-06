# Coded in Python 2.7 by Le1tz3y


VOWELS = "AEIOUYaeiouy"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz"
​
def checkio(text):
    
    import re, string
    
    init_word_list = re.findall('[A-z0-9]+', text)
    
    word_list = []
    
    for k in init_word_list:
        l = k.encode("ascii", "ignore")
        if str.isalpha(l):
            word_list.append(k)
        else:
            pass
    
    print word_list
    
    sum = 0
    
    for i in word_list:
        iter = 0
        for j in i:
            iter = iter + 1
            if iter == 1:
                if j in VOWELS:
                    test = "v"
                else:
                    test = "c"
            elif iter == len(i):
                if (j in CONSONANTS and test == "v"):
                    sum = sum + 1
                elif (j in VOWELS and test == "c" ):
                    sum = sum + 1
                else:
                    break
            else:
                if (test == "v" and j in CONSONANTS):
                    test = "c"
                elif (test == "c" and j in VOWELS):
                    test = "v"
                else:
                    break
                    
    return sum
​