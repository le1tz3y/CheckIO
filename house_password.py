# Coded in Python 2.7 by Le1tz3y


def checkio(data):
    
    passlist = []
    uclist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
              'Y', 'Z']
    lclist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
              'y', 'z']
    test0 = 0
    test = 0
    test2 = 0
    
    # Build a list of letters and numbers
    for i in data:
        try:
            num = int(i)
            passlist.append(num)
            test0 = test0 + 1
        except ValueError:
            passlist.append(i)
            
    # Check for 10 or more items in password
    if len(passlist) >= 10 and test0 >= 1:
        for j in passlist:
            test = test + 1
            if j in uclist:
                for k in passlist:
                    test2 = test2 + 1
                    if k in lclist:
                        return True
                    else:
                        if test2 == len(passlist):
                            return False
                        else:
                            test2 = test2 + 0
            else:
                if test == len(passlist):
                    return False
                else:
                    test = test + 0
    else:
        return False
​