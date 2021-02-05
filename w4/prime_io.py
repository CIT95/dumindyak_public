# get starting number
print('Hello, please enter a starting value:')
startingNum = input()

# get ending number
print('Please enter an ending value:')
endingNum = input()

# printing the starting and ending number
print('Your starting value is ' + str(startingNum) + ' and your ending value is ' + str(endingNum))

# taken from wikipedia - https://en.wikipedia.org/wiki/Primality_test#Python_Code
def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# checking if the satrting num is less than ending num
try:
    if int(startingNum) > int(endingNum):
        raise Exception

except Exception as e:
    print("Your starting value must be less than your ending value. Please try again later.")
else:
    for x in range( int(startingNum) , int(endingNum) + 1 ):
        """         
        if (x == 2) or (x == 3) or (x == 5) or (x == 7):
            print(x)
        elif (x%2 != 0) and (x%3 != 0) and (x%5 != 0) and (x%7 !=0) and (x != 1):
            print(x)
        """
        if is_prime(x):
            print(x)
finally:
    print("Thank you for your time.")         