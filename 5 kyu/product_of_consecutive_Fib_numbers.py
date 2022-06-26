def productFib(prob):
    result, n1, n2 = 0, 0, 1

    while result <= prob:
        if n1 * n2 == prob:
            return [n1, n2, True]
        elif n1 * n2 <= prob:
            result = n1 + n2
            n1 = n2
            n2 = result
        else:
            return [n1, n2, False]
