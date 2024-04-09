# Multiply the elements of a tuple in Python

import math

# ✅ multiply the elements of a tuple by a scalar

my_tuple = (5, 3)

by_five = tuple(5 * elem for elem in my_tuple)

print(by_five)  # 👉️ (25, 15)


# -----------------------------------------------

# ✅ multiply the elements of a tuple

my_tuple = (5, 5, 5)

result = math.prod(my_tuple)

print(result)  # 👉️ 125

# -----------------------------------------------

# ✅ multiply the elements of each tuple in a list

list_of_tuples = [(1, 2), (3, 4), (5, 6)]

result = [math.prod(tup) for tup in list_of_tuples]

# 👇️ [2, 12, 30]
print(result)