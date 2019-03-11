def is_prime(n, i=2):
    # Base cases
    if n <= 2:
        return True if (n == 2) else False
    if n % i == 0:
        return False
    if i * i > n:
        return True

    # Check for next divisor
    return is_prime(n, i + 1)


print('is_prime(3):', is_prime(3))
print('is_prime(7):', is_prime(7))
print('is_prime(9):', is_prime(9))
print('is_prime(31):', is_prime(31))
