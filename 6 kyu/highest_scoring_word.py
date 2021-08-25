def high(x):
    chr = "abcdefghijklmnopqrstuvwxyz"
    n = 0
    result = 0
    for word in x.split(' '):
        for i in range(len(word)):
            result += chr.find(word[i]) + 1
            
        if result > n:
            n = result
            w = word
            
        result = 0
            
    return w
