$ python
Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win
Type "help", "copyright", "credits" or "license" for more information.
>>> username ="chaiandcode"
>>> len(username)
>>> username[0]="A"
  File "<stdin>", line 1, in <module>
'e'
'ha'
e__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__, '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', 'hook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier'rans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rparrsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate, 'zfill']
>>> 12**8
429981696
>>> mylist=[1,2,3]
1
3
>>> myD[1]
'Ad'
>>> my[4]
Traceback (most recent call last):
NameError: name 'my' is not defined. Did you mean: 'myD'?
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object is not callable
>>> myTup[0]
1
>>> mylist(1)=0
>>> mylist[1]
>>> mylist[1]=0
>>> a=3
>>> a = 3.14
AttributeError: module 'sys' has no attribute 'ref_count'
>>> a
>>> mylist_2
>>> mylist_1
[33, 2, 3]
>>> l2 = l1
>>> l1
[44, 2, 3]
>>> l2 = l1[:]
[1, 2, 3]
[55, 2, 1]
>>> l1 = copy.copy(l2)
[1, 2, 3]
>>> m==n
>>> m is n
>>> n = [1,2,3]
False
True
>>> chai[0]
>>> chai[0:6]
>>> chai[-1:-2]
>>> chai[-1:-5]
>>> num_list="0123456789"
'Masla C'
'012345'
'012345678'
>>> num_list[-4:-1]
>>> num_list[3:]
'012'
>>> chai
MASLA CHAI
>>> print(chai.replace("Masla" , "Ginger")
Ginger Chai
>>> print(chai.split(", ")
['lemon,Ginger', 'Masla', 'Mint']
7
>>> print ( chai.count("chai"))
>>> chai_type="Masla Chai"
>>> quantity = 2
>>> order = "I order {} cups of {} chai"
>>> print(order.format(quantity, chai_type))
>>> print("".join(chai))
lemonmaslaginger
>>> print(" ".join(chai))
lemon masla ginger
['lemon', 'masla', 'ginger']
>>> chai = " ".join(chai)
>>> chai
'lemon masla ginger'
>>> len(chai)
18
>>> for letter in chai
  File "<stdin>", line 1
    for letter in chai
                      ^
SyntaxError: expected ':'
>>> for letter in chai :
... print(letter)
  File "<stdin>", line 2
    print(letter)
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for letter in chai :
...
lemon masla ginger
lemon masla ginger
lemon masla ginger
lemon masla ginger
lemon masla ginger
lemon masla ginger
lemon masla ginger
lemon masla ginger
lemon masla ginger
lemon masla ginger
lemon masla ginger
lemon masla ginger
lemon masla ginger
lemon masla ginger
lemon masla ginger
lemon masla ginger
lemon masla ginger
>>> print letter in chai:
  File "<stdin>", line 1
    print letter in chai:
    ^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> chai = "Masla ,Ginger,Lemon"
>>> chai = "Masla ,Ginger ,Lemon"
>>> chai = chai.split(" ,")
>>> chai
['Masla', 'Ginger', 'Lemon']
>>> chai = ("").join(chai)
>>> chai
'MaslaGingerLemon'
>>> chai = (" ").join(chai)
>>> chai
'M a s l a G i n g e r L e m o n'
>>> for letter in chai:
...   print(letter)
...
M

a

s

l

a

G
i

n

e

e


n
>>> chai = "He said , "\ I am doing well\""
  File "<stdin>", line 1
    chai = "He said , "\ I am doing well\""
                        ^
SyntaxError: unexpected character after line continuation character
>>> chai = "He said , \" I am doing well\""
>>> chai
'He said , " I am doing well"'
>>> chai = chai.replace(" I am doing well" , " I am struggling")
>>> chai
'He said , " I am struggling"'
>>> chai = "c:/chai/pwd"
>>> chai
'c:/chai/pwd'
>>> chai = r"chai"
>>> chai
'chai'
>>> num.append(6)
>>> print(num)
[1, 2, 3, 4, 5, 6]
>>> print(num)
>>> num.insert(3,1)
>>> print(num)
[1, 2, 3, 1, 4, 5]
[1, 2, 1, 4, 5]
[1, 3, 2, 1, 1, 4, 5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'replace'
>>> num.remove(3,1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
>>> print(num)
>>> for i in num:
...
[2, 1, 4, 5]
>>> square:List[int] = [x**2 for x in range(0,100)]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
>>> from typing import List
>>> square:List[int] = [x**2 for x in range(0,100)]
>>> print(square)
36, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801]
>>> square:List[int] = [x**2 for x in range(0,10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> num = [1,2,3,4,5]
>>> list[1:2] = [99,01]
                    ^
>>> list[1:2] = [99,100]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
>>> list[1:3] = [99,100]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
>>> list[1:3]
list[slice(1, 3, None)]
>>> num[1:3] = [99,100]
>>> num[1:3]=[]
[1, 4, 5]
>>> num[1:3] = [2,3,6]
>>> num
[1, 2, 3, 6]
>>> num = num.sorted(num)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
>>> num = num.sort(num)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sort() takes no positional arguments
>>> num = sort(num)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
>>> num = sorted(num)
>>> num
[1, 2, 3, 6]