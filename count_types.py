def count_types(n):
    c_positive = 0
    c_negative = 0
    c_zero = 0

    for i in n:
        if i>0:
            c_positive+=1
        elif i<0:
            c_negative+=1
        else:
            c_zero+=1
    return c_positive,c_negative,c_zero


numbers = list(map(int,input().split()))
print(count_types(numbers))
