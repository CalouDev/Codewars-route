def digital_root(n):
    while n > 9:
        new_n = 0
        for i in str(n):
            new_n += int(i)
        n = new_n
    return n
