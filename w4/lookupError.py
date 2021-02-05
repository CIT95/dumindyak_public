
print("Hello there!! give me any number you want to divide:")
firstNum = input()

print("Give me a number you want to divide by:")
secondNum = input()


try:
    result = int(firstNum)/int(secondNum)
except ZeroDivisionError as e:
    print("Sorry! You cannot divide by 0")
except Exception as e:
    print(e)
else:
    print(result)
finally:
    print("Done!!")