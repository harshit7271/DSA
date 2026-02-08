number = [12, 15, 45, 89, 34]

largest = number[0]
for i in number[1:]:
    if i > largest:
        largest = i

print(largest)
