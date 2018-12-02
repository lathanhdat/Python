#First Example
def cube(n):
    return n**3
print(cube(2))

f = lambda n:n**3
print(f(2))

#Second Example
a = lambda x : 'YES' if x%2==0 else 'NO'
print(a(10))
print(a(9))

#Third Example
def add(a,b):
    return a+b
print(add(5,10))

lambda1 = lambda a,b:a+b
print(lambda1(5,10))

#Example 4: Filter function
lst = [4,5,2,6,7]
result = list(filter(lambda x:x%2 == 0,lst))
print(result)

#Example 5: Map function
lst1 = [4,6,7,63,3,72]
result = list(map(lambda n : n*2,lst))
print(result)


#Example 6: Reducefunction
from functools import reduce
lst = [5,10,15,20]
result= reduce(lambda x,y:x+y,lst) #50 = 5+10+15+20
print(result)