import functools
import operator
import itertools
lis = [1,2,3,4,5]

print("Product is : ",end = "")
print(functools.reduce(lambda a, b : a*b, lis))

print("maximum number is : ",end = "")
print(functools.reduce(lambda a,b : a if a>b else b, lis))

print("Sum of the list : ",end="")
print(functools.reduce(lambda a,b : a+b,lis))

list1 = ["Very","clever","Guy"]
print(functools.reduce(operator.add,list1))

print("Sum of list : ",end="")
print(list(itertools.accumulate(lis,lambda x,y : x+y)))
