def find_index(num,x):

    for i in range(len(num)):
        if num[i]==x:
            return i
    return -1


numbers = list(map(int,input().split()))
target = int(input())
print(find_index(numbers,target))