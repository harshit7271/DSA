data = [4, 6, 2, 3, 1, 7, 5]

# slicing method
"""
reversed_data = data[::-1]
print(reversed_data)
"""
n = len(data)
reversed_data = []

for i in range(n-1, -1, -1):
    reversed_data.append(data[i])
print(f'{reversed_data} is the reversed list')


"""

n = len(data) - 1
reversed_data2 = []
while n >= 0:
    reversed_data2.append(data[n])
    n -= 1
print(reversed_data2)

"""
