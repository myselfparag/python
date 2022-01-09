#Python notes for professional - 33 and 34 page





#python data types:- DATA TYPES ARE NOTHING BUT  VARIBLES YOU USE TO RESERVE SOME SPACE IN MEMORY. 
#STRING DATA TYPES:  Python allows for either pairs of single or double quotes to show that it'a a string. Strings are immutable sequence data type,
a = (input("type any word, it will be treated as string as it is in double quotes"))
print(a[:])
print(a[0:2])
print(a[-1:-3:-2])
#while indexing we can do ---> a[1:5:-1] as it is illogical because we cannot reach to 5 by adding -1 in 1.
print(a[1:5:-1]) #not logical nothing will get printed 

#1-->Set Data Types:- Sets are unordered collections of unique objects, there are two types of set : (A)SETS (B)FROZEN SETS
#(A) --> They are mutable and new elements can be added once sets are defined. These are like mathmatical sets in which the output shows set without repeating elements
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # duplicates will be removed
#(B)Frozen Sets - They are immutable and new elements cannot added after its defined.
#The frozenset() is an inbuilt function in Python which takes an iterable object as input and makes them immutable. Simply it freezes the iterable objects and makes them unchangeable. 
#In Python, frozenset is the same as set except the frozensets are immutable which means that elements from the frozenset cannot be added or removed once created. This function takes input as any iterable object and converts them into an immutable object. The order of elements is not guaranteed to be preserved.
cities = frozenset(["Frankfurt", "Basel","Freiburg"])
print(cities)

#2 -->Numbers have four types in Python. Int, float, complex, and long.
int_num = 10 #int value
float_num = 10.2 #float value
complex_num = 3.14j #complex value
long_num = 1234567e #long value

#3 -->List Data:- List are used to store multiple items in a single variable, these are made by square blocks.list can have any type of data.
thislist = ["apple", "banana", "cherry",2]
print(thislist)
#4 -->Dictionary Data:- Dictionaries are used to store data values in key:value pairs.A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
thisdict = {"Name":"red","age":18}
print(thisdict.values()) #will output list of values in dic. ['red',10]
print(thisdict.keys()) #will output list of keys. ['name','age']
#3 --> Tuple Data Type
#Lists are enclosed in brackets [ ] and their elements and size can be changed, while tuples are enclosed in parentheses ( ) and cannot be updated. Tuples are immutable.
tuple = (123,'hello')
tuple1 = ('world')
print(tuple) #will output whole tuple. (123,'hello')
print(tuple[0]) #will output first value. (123)
print(tuple + tuple1) #will output (123,'hello','world')
tuple[1]='update' #this will give you error.
 
