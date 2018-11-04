import sys
lst = sys.argv
for i in lst:
    print(i)
print ("Type cast argv [1] * argv [2] ",int(lst[1])*int(lst[2]))