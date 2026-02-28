numbers = [1, 2, 2, 3, 4, 4, 5]

# first approach
# this remove the duplicates but will not maintain the oorder of the elements
"""
set_num = list(set(numbers))
print(set_num)
"""""

# second approach
unique_elements = []
for i in numbers:
    if i not in unique_elements:
        unique_elements.append(i)
print(unique_elements)
