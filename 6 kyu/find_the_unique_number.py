def find_uniq(arr):
    for i in range(len(arr)-1):
        if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
            print(arr[i])
            return arr[i]
        
    return arr[len(arr)-1]
