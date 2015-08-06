# Coded in Python 2.7 by Le1tz3y


def count_neighbours(grid, row, col):
    
    sc_row = grid[row]
    n_urow = grid[row - 1]
    try:
        n_lrow = grid[row + 1]
        test = "pass"
    except:
        n_lrow = grid[row]
        test = "exception"
    sc = sc_row[col]
    n_lc = 0
    n_rc = 0
    n_ulc = 0
    n_umc = 0
    n_urc = 0
    n_llc = 0
    n_lmc = 0
    n_lrc = 0
    
​
    try:
        n_lc = sc_row[col - 1]
    except:
        pass
    try:
        n_rc = sc_row[col + 1]
    except:
        pass
    try:
        if col == 0:
            n_ulc = 0
        else:
            n_ulc = n_urow[col - 1]
    except:
        pass
    try:
        n_umc = n_urow[col]
    except:
        pass
    try:
        n_urc = n_urow[col + 1]
    except:
        pass
    try:
        if col == 0:
            n_llc = 0
        else:
            n_llc = n_lrow[col - 1]
    except:
        pass
    try:
        n_lmc = n_lrow[col]
    except:
        pass
    try:
        n_lrc = n_lrow[col + 1]
    except:
        pass
        
    row_m1 = row - 1
    if row_m1 < 0:
        n_ulc = 0
        n_umc = 0
        n_urc = 0
    else:
        pass
    
    if test == "exception":
        n_llc = 0
        n_lmc = 0
        n_lrc = 0
    else:
        pass
    
    sum = n_lc + n_rc + n_ulc + n_umc + n_urc + n_llc + n_lmc + n_lrc
​
    print sum
​
    return sum