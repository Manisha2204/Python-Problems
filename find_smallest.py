def find_smallest(n):
    smallest = n[0]
    for i in n:
        if i<smallest:
            smallest = i
    return smallest

numbers = list(map(int,input().split()))
print(find_smallest(numbers))
