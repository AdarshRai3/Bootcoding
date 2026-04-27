from types import List

#Collection
#If we have large data set storing things in variable is not the right way, for that we need collections
day_1_temp = 41 
day_2_temp = 42
day_3_temp = 45
day_4_temp = 43
day_5_temp = 41

avg_temp_var = (day_1_temp + day_2_temp + day_3_temp + day_4_temp + day_5_temp)/5
print(avg_temp_var)

temp:List = [41,42,45,43,41]

avg_temp_list = sum(temp)/len(temp)

print(avg_temp_list)



# Type of Collections/DataStructure
# Sequences - string, list , set
# Mapping - dictionary
# sets - set , forzenset

#string - Ordered , immutable sequence of character
#-"Hello world"

#list - Ordered , mutable collection that can have misted datatypes
#-[1,"Ad",3.14,True]

#tuple - Ordered , immutable collections similar to list
#-(1,"Ad",3.14,True)

#dictionary - Unordered(pre-3.7)/insertion-order(3.7+) key-value pair
# -{'name':'Ad', 'age':25}

#set - Unordered mutable collections of unique element
#-{1,2,3,4}

#frozenset - Immutable version of a set
#-{1,2,3,4}