def most_frequent(num):
    duplicates = {}
    for i in num:
        if i in duplicates:
            duplicates[i]+=1
        else:
            duplicates[i]=1
        
    most_frequent = None
    max_count = 0

    for number,count in duplicates.items():
        if count > max_count:
            max_count = count
            most_frequent = number

    return most_frequent
 
numbers = list(map(int,input().split()))
print(most_frequent(numbers))