# Coded in Python 2.7 by Le1tz3y


def find_message(text):
    
    import string
    alist = []
    
    for ch in text:
        if ch in string.ascii_uppercase:
            alist.append(ch)
        else:
            pass
        
    return string.join(alist, "")