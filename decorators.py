#Example 7: Decorators
def decor(func):
    def innerfunc():
        a = func()
        return a*2
    return innerfunc()

@decor
def number():
    return 5

print(number)

#Ex8: More Decorators
def dercorfunc(func8):
    def inner(n):
        result = func8(n)
        result += " How are you?"
        return result
    return inner

@dercorfunc
def hello(name):
    return "Hello " + name

print(hello("Dat"))