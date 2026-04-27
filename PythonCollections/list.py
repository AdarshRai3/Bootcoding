#A built in Ds that stores an ordered , mutable collections of items.
#Lists can hold items of any items, including other lists

#Ordered : Items have a defined order and can be accesses by their index
#Mutable : You can change , add , or remove after the list has been created 
#Hetrogenous : A single list can contain elements of different datatypes
#Iterable: Lists can be looped over using list compheresions , loops or lambda functions 
 
my_list = [1,2,3,4,5]
mixed_list = [1, " hi ", 3.14 , True]

nested = [[1,2],[3,4]]

#Empty list 
empty_list = []

#List of strings
colors = ["Red","Blue","Green"]

#List of mixed types
info = ["Alice", 30 , 4.8 , False]

#List inside a list(nested)
matrix = [[1,2],[3,4],[5,7]]

'''
1 2
3 4
5 6
'''
lie = list() #Creating list using constructor-> []

lif = list("Ada")
print(lif)
# ->['A','d','a']

s = {10,20,30}
lst = list(s)
print(lst)

lst0 = list(range(10))

# list() is used when we want to create list of other iterables(set,range,string)

original_list = [1,2,3,4,5]
copied_list = list(original_list)
print(copied_list)
#Another function of the list() to copy one list from another

# list(123) this will give us an error since 123->int and we know int is not interable so we cannot use list

#Indexing and Slicing
fruites = ["apple","organes","mango"]
fruites[1] #Oranges
fruites[-1] #mango
fruites[-3] #apple
fruites[3] #Index out of range

#Numbers
numbers = [10,20,30,40,50]

#list[start:end:step]
#Impo
print(numbers[:3]) #[10,20,30,40]
print(numbers[1:]) #[20,30,40,50]
print(numbers[1::2]) #[20,40]
print(numbers[1:100])#No error : Slicing will not throw out of range error if you exceed the list
print(numbers[len(numbers)-1]) #50
print(numbers[::-1]) #Will print the list in reverse order [40,30,20,10]
print(numbers[-3:])

#Modifying the list
fruites = ["apple","banana","cherry"]
fruites[1] = "blueberry"
print(fruites) #["apple","blueberry","cherry"]
#We can also modify using slice
fruites[1:3] = ["pear", "kiwi"]

fruites.append("mango")
print(fruites)#["apple","blueberry","cherry","mango"]

fruites.insert(3,"banana")
print(fruites) #["apple","blueberry","cherry","banana","mango"]

fruites_2 =["grapes","kiwi"]
fruites.extend(fruites_2) #["apple","blueberry","cherry","banana","mango","grapes","kiwi"] 
#append would add the entire list as a single list inside the list as a single element

fruites.remove("banana") 
#when we want to remove elements by value
#remove doesn't return anything : None
print(fruites)
#["apple","blueberry","cherry","banana","mango","grapes","kiwi"] 

fruites.pop(4) 
#when we want to remove element by index
#pop() will remove last element or [-1]element
#pop will return the element that it remove from the list

del fruites[1]
#will remove element as index=1
#del is keyword not function that helps to remove element and it does not return anything

del fruites[1:3] 
#We can also remove elements in the slice


fruites.clear()
#Remove all the elements

#Shallow copy and deep copy 
a = [1,2,3]
b = a
b.append(4)
print(a)
#[1,2,3,4]

b = a[:] #shallow copy
b[0] = 99
print(a) #[1,2,3,4]
print(b) #[99,2,3,4]
#shallow copy for a flat list
#Change in copy will not see any change in original

c =[[1,2] ,[3,4]]
d = c[:]
d[0][0] = 99
print(c) #[[99,2],[3,4]]
print(d) #[[99,2],[3,4]]
#shallow copy for a nested list
#copy will have reference of original 
#Change in copy will show change in original

#Solution of this problem is deepcopy
import copy
e = copy.deepcopy(c)
e[0][0] = 100
print(c)#[[99,2],[3,4]]
print(d)#[[100,2],[3,4]]

#operation in list
#list concationation
a = [1,2,3]
b = [4,5]
result = a + b 
ans = a + b + 6 #This will give type error
ans = a + b + [6] # This will work 
print(result)
#But unlike extends we can change the original list but using concatination we can create the entire new list

#multiply
a = [0,1]

print(a*2)
#[0,1,0,1] This will repeat the list characters


#Now we want to check if something exist in the list or not for that you can use "in"

fruits = ["apple","mango","banana","kiwi"]

print("appple" in fruits) #True
print("apple" not in fruits) #False
#But this does linear search 

nested = [[0]*3]*3 
'''
0 0 0
0 0 0
0 0 0
'''
#This do shallow copy which will create problems , shallow copy refereces in nested list
nested[0][0] = 1
'''
1 0 0
1 0 0 
1 0 0
'''

print(len([1,2,3,[4,5]])) #length : 4

numbers = [1,2,3,8,9]
print(min(numbers)) #1
print(max(numbers)) #9
print(sum(numbers)) #23

names = ['Alice' , 'Bod' , 'Charlie']
print(max(names)) #Charlie
print(min(names)) #Alice
#Compare letter by letter on ascii level and A - 65 and a - 98
print(ord('A'))

#Advance Method of list

nums = [1,2,3]
nums.reverse() #[3,2,1]-> in place
list(reversed(nums)) #[3,2,1]-> new list

words = ["anans","bananas","cherry" ]
sorted_word = sorted(words, key = len , reverse = True)
print(sorted_word) #sorted will create a new list

nums = [-10,5,-3,2,-1]
nums.sort(key=abs,reverse = True) #In-place

names = ['Alice','ALice','Charlie']
names.sort(key=str.lower, reverse=True)

fruits = ['apple','banana','apple','orange','banana','apple']

print(fruits[1:3].count('apple'))
print(fruits.index('apple',-3))


#Iternation in list
for fruit in fruits:
    print(fruit)
    
for i in range(len(fruits)):
    print(fruits[i])
    
c = 0
for fruit in fruits:
    if fruit == "apple":
        c+=1

print(c)

f_index = 0
for i in range(len(fruits)):
    if fruits[i] == 'apple':
        f_index = i
        break
    
print(f_index)

reversed_list = []

for fruit in fruits[::-1]:
    reversed_list.append(fruit)
    
for i in range(len(fruits)-1,-1,-1):
    reversed_list.append(fruits[i])
    
print(reversed_list)

nums = [4,5,6,67,7,1]
min_num = 0
for i in nums:
    if min_num > i:
        min_num = i
print(min_num)

#Nested list
