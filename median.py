# Coded in Python 2.7 by Le1tz3y

def checkio(data):
​
    data.sort()
    count = len(data)
​
    if count % 2 == 0:
        low = data[(count/2)-1]
        high = data[count/2]
        lowf = float(low)
        highf = float(high)
        median = (lowf + highf) / 2
        return median
    else:
        median = data[count/2]
        return median