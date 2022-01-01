# Question No.1

string = "RANVIJAY"
lis = list(string)
print("After convert the string into list : ",lis)



# Question No.2

def convert_to_string(lis):
    
    s=""
    for x in lis:
       s = s + x;
    return s;

lis = ['R', 'A', 'N','V','I','J','A',"Y"]
string = convert_to_string(lis)
print("After Convert to string : ",string)



# Question No.3

import numpy as np

n = int(input("Enter a number : "))
number = np.random.randint(1,n+1,5)
num = list(number)
print("list of n random numbers : ",num)




# Question No.4

list1 = [1,5,2,4,3]

# To sort the list 
list1.sort(reverse = True)

print("list of order in descending order : ",list1)




# Question No. 5

random_list = [1,1,2,3,2,4,4,1,2]
frequency = {}

# iterating over the list
for item in random_list:
   # checking the element in dictionary
   if item in frequency:
      # incrementing the counter
      frequency[item] += 1
   else:
      # initializing the count
      frequency[item] = 1


print("The frequency of each numbers : ",frequency)




#     Question No. 6 

def unique_element(list1):
    list2 = []
    
    for a in list1:
        if a not in list2:
            list2.append(a)
    return list2
    
    
list1 = [1,1,3,2,3,2,3,2,2]
list3 = unique_element(list1)
list3.sort()
print("The unique element : ",list3)




# Question no. 7

def repeating_element(nums):
    num_set = set()
    no_repeate = -1

    for i in range(len(nums)):

        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])

    return no_repeate

print("The first repeating element : ",find_first_duplicate([1,2,3,4,5,1,2]))





# Question No. 8


dictionary = {} 
n = int(input("Enter a number : "))
for x in range(0,n+1):
    dictionary[x]=(x**2,x**3)
    
print("list containing the square and cube of the number : ")
print(dictionary)




# Question no. 9

def merge_list(list1, list2):
    new_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return new_list

list1 = [1,2,3,4]
list2 = ['a','b','c','d']

print("The Desire list : ",merge_list(list1, list2))




# Question No. 10

sqr = []

n = int(input("Enter a number : "))
for var in range(0, n+1):
    num = var**2
    sqr.append(num)
print("The square of 0 to n : ",sqr)




# Question No.11

decs = {}

n = int(input("Enter a number : "))
for var in range(0, n+1):
    decs[var] = var**2
    
print("The square of 0 to n : ",decs)


#  Question No. 13

from typing import List
def uppercaseWords(wordList: List[str]) -> List[str]:  
    """
    uppercaseWords(['aa', 'bb', 'cd', 'e'])
    ['AA', 'BB', 'CD', 'E']
    """
    newList = map(getUpper, wordList)
    return list(newList)
    
    
#    Question No. 14

import functools

list1 = [1,2,3,4,5]
print("The product of number inside the list : ",end="")
print(functools.reduce(lambda a,b:a*b,list1))