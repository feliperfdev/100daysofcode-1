def fibonacci(num):
    try:
        assert(type(num) is int and num > 0)
        if num == 1 or num == 2:
            return 1
        else:
            f = fibonacci(num-1) + fibonacci(num-2)
        return f
    except (AssertionError, TypeError):
        print('Informe um valor inteiro e maior que zero!')


print(fibonacci(10))
print(fibonacci(4))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))