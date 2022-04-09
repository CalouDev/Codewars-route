def data_reverse(data):
    result = []
    
    for i in range(len(data), 0, -8):
        result.append(data[i-8:i])
        
    return [j for n in result for j in n]
