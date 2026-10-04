def count_duplicates(num):

    duplicates = set()
    seen = set()

    for i in num:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)
    return len(duplicates)

numbers = list(map(int,input().split()))
print(count_duplicates(numbers))