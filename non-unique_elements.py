# Coded in Python 2.7 by Le1tz3y

def checkio(data):
    
    list = []
    
    for i in data:
        uniqtest = data.count(i)
        ind = data.index(i)
        if uniqtest > 1:
            list.append(i)
        else:
            continue
            
    return list
​