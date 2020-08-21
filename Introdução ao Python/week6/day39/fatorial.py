def fatorialRecursivo (n):
    if n != 0:
        f = n * fatorialRecursivo(n-1)
        return f
    else:
        return 1

print(fatorialRecursivo(5))
print(fatorialRecursivo(0))