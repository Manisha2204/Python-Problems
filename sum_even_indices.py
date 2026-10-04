def sum_even_indicies(num):

    total=0
    for i in range(len(num)):
        if i%2==0:
            total+=num[i]
    return total



numbers = list(map(int,input().split()))
print(sum_even_indicies(numbers))
