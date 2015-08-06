# Coded in Python 2.7 by Le1tz3y


def checkio(array):
    
    index = -1
    sum = 0
    
    for i in array:
        index = index + 1
        if index % 2 == 0:
            sum = sum + i
        else:
            pass
            
    try: 
        return sum * array[len(array) - 1]
    except IndexError: 
        return 0