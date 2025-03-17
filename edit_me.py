def monotonic(lst):
    inc = dec = True
    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i+1]:
            inc = False
        elif lst[i] < lst[i+1]:
            dec = False
    return inc or dec

assert monotonic([1,3,4,100]) == True
assert monotonic([1,2,1,2]) == False
assert monotonic([100, 56, 3, 2, 2, 1]) == True