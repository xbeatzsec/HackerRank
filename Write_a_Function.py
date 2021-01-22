def is_leap(year):
    c = year / 4
    v = c.is_integer()
    if v == True:
        f = year / 100
        z = f.is_integer()
        if z == True:
            i = year / 400
            iu = i.is_integer()
            if iu == False:
                return iu
        return v
    else:
        return v
    y = year / 100
    w = y.is_integer()
    if w == False:
        return w
    else:
        return w




