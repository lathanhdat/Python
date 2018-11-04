def display(name):
    def message():
        return 'Hello '
    return (message() + name)

print (display("Dat"))


def display1(lst):
    for i in lst:
        print (i)
display1([1,2,3,4])

def factorial(n):
        if n == 0:
                return 1
        else:
                return (n * factorial(n -1))
print(factorial(5))