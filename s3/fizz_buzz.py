def fizz_buzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return 'FizzBuzz'
    elif (num % 3 == 0):
        return 'Fizz'
    elif (num % 5 == 0):
        return 'Buzz'
    else: 
        return num

# write  code that will take user input
print("Hi, write any number here.")
number = input()

ret = fizz_buzz(int(number))
print(ret)


   
