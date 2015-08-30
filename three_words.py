# Coded in Python 2.7 by Le1tz3y

def checkio(words):
    alist = words.split(' ')
    
    count = 0
    
    for i in alist:
        if i.isalpha():
            count += 1
            if count == 3:
                return True
            else:
                pass
        else:
            count = 0
    
    return False