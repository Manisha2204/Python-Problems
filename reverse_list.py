def reverse_list(n):
    reverse = []

    for i in range(len(n)):
       
       reverse.append(n[(len(n)-1)-i])
       
    return reverse

numbers = list(map(int,input().split()))
print(reverse_list(numbers))
