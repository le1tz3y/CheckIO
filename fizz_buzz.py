# Coded in Python 2.7 by Le1tz3y

def checkio(number):
    
    if number % 15 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)