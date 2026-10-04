def largest_even_number(num):

    max_num = None
    for i in num:
        if i%2==0:
            if max_num is None or i > max_num:
             max_num=i
    
    return max_num    

numbers = list(map(int,input().split()))
print(largest_even_number(numbers))