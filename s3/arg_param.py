def addValue(x, y=0):
    return x + y
# in this function, the box X is the age. Y is 15.
# above, Y=0 is a "default parameter".
# X and Y are "parameters".

# but in here x is defined as "number". Y is still same.   
def getInput():
    print("Hello there, what is your age now?")
    num = input()
    print("Do you want know what is your age in 15 years? (Y/N)")
    ans = input()
    return num, ans

number, answer = getInput()

if (answer == 'Y') or (answer == 'y'):
    y = 15
    z = addValue(int(number), y) # Z (return value) is whatever the age is after adding 15. 
    # Here, number(age) and 15 are "arguments". 

    print("Your age in 15 years is: " + str(z))

else:
    z = addValue(int(number)) # this Z is giving his/her age back. 
    
    print("Your age is: " + str(z))
    




#print(z)
#number= input()

