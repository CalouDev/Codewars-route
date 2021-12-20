def corner_fill(square):
    result = []
    for y in range(len(square)):
        for x in range(len(square)):
            if y == 0:
                result.append(square[y][x])
                result.append(square[])
            elif y == 1:
                result.append(square[y][x-1])
            else:
                result.append(square[y][x])
