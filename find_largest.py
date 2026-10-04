# define function
def find_largest(n):
    largest = n[0]
    # take elements from the list
    for i in n:
        # updae largest if i is greater
        if i>largest:
            largest = i
    return largest

# take list input 
numbers = list(map(int,input().split()))
# call function
print(find_largest(numbers))
