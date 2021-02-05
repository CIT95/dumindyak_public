def fizz_buzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return 'FizzBuzz'
    elif (num % 3 == 0):
        return 'Fizz'
    elif (num % 5 == 0):
        return 'Buzz'
    else: 
        return num


try:
    # write  code that will take user input
    print("Hi, write any number here.")
    number = int(input())

    if (number < 0):
        raise Exception

    ret = fizz_buzz(number)
except ValueError as e:
    print(e)
except Exception as e:
    print("Please do not enter a negative number.")
else: 
    print(ret)
finally:
    print("Bye!!")