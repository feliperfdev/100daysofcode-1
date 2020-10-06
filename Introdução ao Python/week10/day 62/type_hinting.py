# Sem type hinting:

def add_int(val):
    return val+val

print(add_int('e')) # -> ee

# Com type hinting:

def add_int_hinting(val: int):
    return val + val

print(add_int_hinting('e'))

# ==========================================================================================

# Sem type hinting: 
def print_num(num):
    for n in num:
        print(num, end=' ')

print_num([1, 2, 3, 4]);                                                            print()

# Com type hinting
def print_numbers(numbers: list[int]) -> None:
    for number in numbers:
        print(number, end=' ')

print_numbers([1, 2, 3, 4]);                                                        print()

def print_numbersTuple(numbers: tuple[int]) -> None:
    for number in numbers:
        print(number, end=' ')

print_numbersTuple((1, 2, 3, 4))