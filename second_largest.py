def second_largest(n):
    largest = float('-inf')
    sec_largest = float('-inf')
    for i in n:
        if i>largest:
            sec_largest = largest
            largest = i
        
        elif i>sec_largest:
            if i!=largest:
                sec_largest=i
            
    return sec_largest
         

numbers = list(map(int,input().split()))
print(second_largest(numbers))
