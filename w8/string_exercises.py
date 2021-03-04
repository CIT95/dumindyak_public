print("------------Q1-------------\n")
# Exe: 1 w3resource - Write a Python program to calculate the length of a string.
# I was able to solve it without any problems.

def getLenth(spam):
    
    length = len(spam)

    return length

spam = "My name is Dumi"

print(getLenth("Hello World!"))
print(getLenth(spam))



print("\n------------Q2-------------\n")
#  Exe: 2 w3resource - Write a Python program to count the number of characters (character frequency) in a string.
# I was able to solve it without any problems. We have done a same exercise in previous week.

sampleString = 'google.com'
count = {}

for character in sampleString.lower(): # Here it will convert all letters to lower case letters. 
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

""" # Either I can use frequency function to get the answer here. 
sampleString = 'google.com'
frequency = {}

for character in sampleString.lower(): # Here it will convert all letters to lower case letters. 
    frequency.setdefault(character, 0)
    frequency[character] = frequency[character] + 1

print(frequency) """

print("\n------------Q3-------------\n")
# Exe: 6 Pynative -Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string
# I was able to solve it without any problems.

def getSingStr(x, y):
    newNum_x = y[:2] + x[2:]
    newNum_y = x[:2] + y[2:]

    return newNum_x +  ' '  + newNum_y

print(getSingStr('abc', 'xyz'))
                   

print("\n------------Q4-------------\n")
# Exe: 13 w3resource - -Write a Python script that takes input from the user and displays that input back in upper and lower cases.
# I was able to solve it without any problems.

print("What is your name?")
name = input()
print("My name is" + ' ' + name.upper())
print("My name is" + ' ' + name.lower())

print("\n------------Q5-------------\n")
# Exe: 8 Pynative -  Find all occurrences of “USA” in a given string ignoring the case.
# I tried to solve it by myself, it was correcet but in this exercise we have to get both upper and lower. So I had to google it to see how to use lower function in this problem. 

str1 = "Welcome to USA. usa awesome, isn't it?"

count = str1.lower().count('usa')

print("The USA count is:", count)


print("\n------------Q6-------------\n")
# Exe: 40 w3resource - Write a Python program to reverse words in a string.
# I had to check about the reverse function in google.

def myFunction(a):
    words = a.split() # Used split here to split the words
    reverse = ' '.join(words[::-1]) # after checking the word sone by one used join func. to join the reversed sentence. 
    return reverse

spam = myFunction("This is our learn together weekly assignment")

print(spam)

print("\n------------Q7-------------\n")
# Exe: 14 Pynative - Remove empty strings from a list of strings
# Searched about the filter function to check how it works in python. 

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

filteredStr = filter(None, str_list)

print(list(filteredStr))

print("\n------------Q8-------------\n")
# Exe: 16 Pynative - Removal all the characters other than integers from a string
# Serched in google about isdigit function.

result = ''
str1 = 'I am 25 years and 10 months old'
str2 = str1.split()

for i in str2:
    if i.isdigit():
        result = result + i # adding numbers to result variable one by one. 

print(result)
        
print("\n------------Q9-------------\n")
# Exe: 15 Pynative - Remove special symbols/Punctuation from a given string.
# I solved this problem without any issues. 

test_string = "/*Jon is @developer & musician"
chars = ['/', '@', '&', "*"]
for i in chars :
    test_string = test_string.replace(i, '')
 
# printing resultant string 
print (str(test_string))

print("\n------------Q10-------------\n")
# Exe: 12 Pynative - Find the last position of a substring “Emma” in a given string.
# I solved this problem without any issues. 

str1 = "Emma is a data scientist who knows Python. Emma works at google."
subStr = str1.rfind("Emma")
print("Last occurrence of Emma starts at index:", subStr)