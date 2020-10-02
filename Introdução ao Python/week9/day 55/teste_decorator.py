def setUpper(function):
    def functionDecorator():
        return function().upper()
    return functionDecorator

def setLower(function):
    def functionDecorator():
        return function().lower()
    return functionDecorator

def semDecorator():
    return 'Hello, World!'

@setUpper
def comDecoratorUpper():
    return 'Hello, World!'

@setLower
def comDecoratorLower():
    return 'Hello, World!'

print(semDecorator()) # Hello, World!
print(comDecoratorUpper()) # HELLO, WORLD!
print(comDecoratorLower()) # hello, world!