# define function
def count_even_numbers(n):
    # intialise a counter
    c = 0
    # run loop
    for i in n:
        # check if i is even
        if i%2==0:
            c+=1
    return c


# take input of list from user
numbers = list(map(int,input().split()))
# call function
print(count_even_numbers(numbers))
