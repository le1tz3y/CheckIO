# Coded in Python 2.7 by Le1tz3y


def index_power(array, n):
​
    try:
        return array[n] ** n
    except IndexError:
        return -1