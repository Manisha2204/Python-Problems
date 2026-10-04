
# define function
def count_occurences(number,target):
# intialise a c=0
    c = 0
# take elements from the list
    for i in number:
# if i==target, increase c
        if i==target:
            c+=1
    return c

# take input of list 
numbers = list(map(int,input().split()))
#select a target from the list 
target = int(input())
# call function 
print(count_occurences(numbers,target))
