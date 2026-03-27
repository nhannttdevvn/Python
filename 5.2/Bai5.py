def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_gen = (x for x in range(1, 21) if is_prime(x))
try:
    while True:
        print(next(prime_gen))
except StopIteration:
    print("Đã hết số nguyên tố trong phạm vi.")

# Output:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19