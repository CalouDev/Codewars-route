def odd_or_even(arr):
    new_arr = 0
    for i in range(len(arr)):
        new_arr += arr[i]
    return "even" if new_arr % 2 == 0 else "odd"
