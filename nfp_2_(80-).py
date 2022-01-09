#Notes of page 80- 
'''CONDITIONALS:- If,Elif,Else are conditionals  here which help in providing conditions in a programe'''
#Ternary operators are also known as conditional expressions are operators that evaluate something based on a condition being true or false.
'''In Python you can define a series of conditionals using if for the first one, elif for the rest, up until the final
(optional) else for anything not caught by the other conditionals.'''
number = 5
if number > 2:
 print("Number is bigger than 2.")
elif number < 2: # Optional clause (you can have multiple elifs)
 print("Number is smaller than 2.")
else: # Optional clause (you can only have one else)
 print("Number is 2.")
 #Truth Values
'''The following values are considered falsey, in that they evaluate to False when applied to a boolean operator
1.None
2.False
3.0, or any numerical value equivalent to zero, for example 0L, 0.0, 0j
4.Empty sequences: '', "", (), []
5.Empty mappings: {}
6.User-defined types where the __bool__ or __len__ methods return 0 or False
'''

#Boolean Logic Expressions
'''Boolean logic expressions, in addition to evaluating to True or False, return the value that was interpreted as True
or False. It is Pythonic way to represent logic that might otherwise require an if-else test.'''
'''And operator
The and operator evaluates all expressions and returns the last expression if all expressions evaluate to True.
Otherwise it returns the first value that evaluates to False:
'''
print(1 and 2 ) #this will return only 2 as an output 
'''Or operator
The or operator evaluates the expressions left to right and returns the first value that evaluates to True or the last
value (if none are True).
>>> 1 or 2
1
>>> None or 1
1
>>> 0 or []
[]'''

#WAP IN WHICH HAVE TO INPUT AGE OF USER AND TELL HIS OR HER VOTING STATUS
age = int(input(" AGE  "))
if age < 18:
  print("You cannot vote ")
else:
  print("yes you can vote")

#WAP TO CHECK INPUT NUMBER IS ODD OR EVEN 
in_number=int(input("enter your number"))
if in_number % 2 == 0:
    print(in_number,"Is even")
else:
    print(in_number,"Is odd")

'''#Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
             Unit                                                     Price  
First 100 units                                               no charge
Next 100 units                                              Rs 5 per unit
After 200 units                                             Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)</strong>'''

Unit = int(input("Enter the number of units"))
if Unit <= 100:
    print("Zero")
elif Unit > 100 and Unit <= 200:
    print("Your bill is ",Unit*5)
else:
    print("Your bill is ",Unit*10)
    

#Write a program to display the last digit of a number
numb = int(input("Enter your number "))
print("Last digit of number ", numb%10)
