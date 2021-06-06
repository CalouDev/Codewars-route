def first_non_consecutive(arr):
    result = True
    for i in range(1, len(arr)):
        if arr[i] - 1 == arr[i-1]:
            continue 
        else: 
            return arr[i]
            
    return None
