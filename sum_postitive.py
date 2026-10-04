# define a function
def sum_postitive(n):
    sum = 0
    # take elements of the list 
    for i in n:
        # find if its positive or not 
        if i>0:
            sum+=i
    return sum

#  take list input
numbers = list(map(int,input().split()))
# call function
print(sum_postitive(numbers))
