gen = (x for x in range (16) if x % 3 == 0)

first = next(gen)
print(first)  # Output: 0
second = next(gen)
print(second)  # Output: 3