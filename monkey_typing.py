# Coded in Python 2.7 by Le1tz3y


def count_words(text, words):
    
    import re
    count = 0
    
    for i in words: 
        num = len(re.findall(i, text, re.I))
        if num > 0: 
            count = count + 1
        else: 
            pass
                    
    return count