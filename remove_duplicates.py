def remove_duplicates(n):
    my_list = []
    for i in n:
        # if i in my_list:
        #     continue
        # else:
        #     my_list.append(i)
        if i not in my_list:
            my_list.append(i)
    return my_list
        

numbers = list(map(int,input().split()))
print(remove_duplicates(numbers))
