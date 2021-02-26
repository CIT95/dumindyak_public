# How many hours of activity per week. 
# Value in minutes. 
myDict = {}

def getUserInfo():
    activity = '' #local variable
    time = '' #local variable

    print("\nWhat activity do you want to record?")
    activity = input()

    print("\nHow much time did you spend doing the activity?")
    time = int(input())

    return activity, time

print("Welcome to activity tracker.\n")

while True:
    act, tme = getUserInfo()
    #print(act, tme)
    
    ''' 
    if k in myDict:
        myDict[k].append(v)
    else:
        myDict[k] = [v]

    do you want to enter another activity? Y/N
    '''
    
    #3. check whether a given key already exists in a dd
    if act in myDict:
        myDict[act] = myDict[act] + tme
    else:
        #1. add a key to a dd 
        myDict[act] = tme

    print(myDict)

    print("\nDo you want to add another activity?")
    addAnother = input()

    if (addAnother in ['N', 'n']):
        break

print("\n-------------------------------------")
print("              Summary                ")
print("-------------------------------------")

print("\nHere's what you enterd:")

#4. iterate over dd using for loops
for x in myDict.items():
    print(x[0] + ": " + str(x[1]))

'''
print(myDict)

sort_myDict = sorted(myDict.items(), key=lambda x: x[1])

for i in sort_myDict:
	print(i[0], i[1])
'''

#2. sort (ascending or descending) 
print("\nHere is you what you entered in ascending order:")
sort_myDict = sorted(myDict.items(), key=lambda x: x[1])

for i in sort_myDict:
	print(i[0], i[1])

'''
filter(lambda x:x[1]>0, d1.items())
filtered_myDict = filter(lambda x: x[1] < 30, myDict.items())

for i in filtetred_myDict:
	print(i[0], i[1])
'''

#5. filter a dd based on values
print("\nHere are your activities you spent less than 30 mins on:")
filter_myDict = filter(lambda x: x[1] < 30, myDict.items())

for i in filter_myDict:
	print(i[0], i[1])

#6. take your dd and create a list of dd
print("\nHere are some final stats:")
time_list = myDict.values()

#7. iterate over the list of dd and output summary data (total, average, min, max etc)
print("Total minutes spent on all activities: " + str(sum(time_list)))
print("Max minutes spent on an activity: " + str(max(time_list)))
print("Min minutes spent on an activity: " + str(min(time_list)))
print("Average minutes spent on an activity: " + str(sum(time_list)/len(time_list)))

print("\nDone!")
