##page 90 -
#LOOPS
'''A Python for loop iterates over an object until that object is complete.'''
#------>Break and Continue in Loops
# break statement
# When a break statement executes inside a loop, control flow "breaks" out of the loop immediately:
i = 0
while i > 7:
    print("YOYOOY")
    if i == 4:
        print("Breaking now")
        break
    i+=1

''''The loop conditional will not be evaluated after the break statement is executed. Note that break statements are
only allowed inside loops, syntactically. A break statement inside a function cannot be used to terminate loops that
called that function.
'''



'''continue statement
A continue statement will skip to the next iteration of the loop bypassing the rest of the current block but
continuing the loop. As with break, continue can only appear inside loops:
'''

for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i)
'''Note that 2 and 4 aren't printed, this is because continue goes to the next iteration instead of continuing on to
print(i) when i == 2 or i == 4'''

"""When a loop contains another loop inside its body it is called Nested loop
"""








