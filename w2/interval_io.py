
# get starting number
print('Hello, please enter a starting value:')
startingNum = input()

# get ending number
print('Please enter an ending value:')
endingNum = input()

# printing the starting and ending number
print('Your starting value is ' + str(startingNum) + ' and your ending value is ' + str(endingNum))

# checking if the satrting num is less than ending num
if int(startingNum) > int(endingNum):
    print('Your starting value must be less than your ending value. Please try again.')
else:
    for x in range( int(startingNum) , int(endingNum) + 1 ):
        print(x) 

