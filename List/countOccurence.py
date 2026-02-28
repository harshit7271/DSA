# Counting occurences of an element
item = ["apple", "banana", "apple", "orange", "banana", "apple"]
target = "apple"

count = 0
for i in item:
    if i == target:
        count += 1

print(count)


# we can also use the built- in function count()
"""items.count(target)"""
