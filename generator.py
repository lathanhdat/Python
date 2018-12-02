def genefunc(x,y):
    while x<y:
        yield x
        x += 1
result = genefunc(20,25)

for i in result:
    print(i)