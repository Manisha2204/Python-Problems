def count_above_average(num):

    total = 0
    for i in num:
        total+=i
    avg = total/len(num)
    c=0
    for i in num:
        if i>avg:
            c+=1
    return c


numbers = list(map(int,input().split()))
print(count_above_average(numbers))
