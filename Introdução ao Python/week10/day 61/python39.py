# Um dos recursos disponíveis na versão 3.9 do Python lançada hoje (05/10):

some_var = list[dict[str, int]]

print(some_var)

# ====================================================

# Type Hinting

def print_numbers(numbers: list[int]) -> None:
    for number in numbers:
        print(number)

print_numbers([1, 2, 3, 4])

# ====================================================

# .removeprefix() e .removesuffix() -> novos métodos string

string = "Hello World!"
string = string.removeprefix("Hello ")
print(string)

string = "Hello World!"
string = string.removesuffix(" World!")
print(string)

# ====================================================

# Concatenação de dicionários com |

dictionary1 = {'x': 1, 'y': 2, 'z': 3}
dictionary2 = {'a': 4, 'b': 5, 'c': 6}

concatenado = dictionary1 | dictionary2
print(concatenado)

# ====================================================

# Update de dicionários com |=

dict1 = {'x': 1, 'y': 2, 'z': 3}
dict2 = {'a': 4, 'b': 5, 'c': 6}

dict1 |= dict2
print(dict1)

