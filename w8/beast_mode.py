""" question_prompt = []

print("What do we use to get a length in a function?")
print("Here are the answers, pick one")

a = {1:"add",2:"len",3:"split"}
for i,j in a.items():
    print(i,j)

answer = input()
 """
# Here is a simple game to level up your python skills. I have created 5 mulitple choice questions with the answers. You just have to give a correct answer for each question.
# HAVE FUN!!!

print("\n----------Let's start the simple quiz!!----------\n")
questions = {
   'Q1': {
       'question': "To get the length of a string, use the ...... function",
       'answers': {1:"add",2:"len",3:"split",4:"index"},
       'correct': 2
   },
      'Q2': {
       'question': "What method should we use to find the first occurrence of a specified value?",
       'answers': {1:"index",2:"len",3:"count",4:"find"},
       'correct': 1
   },
      'Q3': {
       'question': "The ...... method returns the number of times a specified value appears in the string.",
       'answers': {1:"find",2:"lower",3:"count",4:"len"},
       'correct': 3
   },
      'Q4': {
       'question': "What do we use to replaces a specified phrase with another specified phrase?",
       'answers': {1:"add",2:"len",3:"split",4:"replace"},
       'correct': 4
   },
      'Q5': {
       'question': "The ...... method removes any spaces at the beginning and spaces at the end characters.",
       'answers': {1:"strip",2:"len",3:"replace",4:"join"},
       'correct': 1
   }
}

correctCount = 0

for qlabel in questions.keys(): #['Q1', ]
    question = questions[qlabel] #save the 2nd tier dict to a variable
    
    #then get all info from the dict to variables
    qtext = question['question']
    answers = question['answers']
    correct = question['correct']

    print("\n" + qlabel + ") " + qtext + "\n")
    for ans in answers.items():
        choice = str(ans[0])
        text = ans[1]
        print(choice + ". " + text)
 
    print("\nPlease answer by typing the corresponding number of your choice:")
    userChoice = int(input())

    if userChoice == correct:
        print("Your answer is correct!")
        correctCount =  correctCount + 1
    else:
        print("Sorry, the correct answer is: " + answers[correct])

print("\n\nYour final score is " + str(correctCount) + "/5. Thank you for playing!")


'''
  {
       'question': "What do we use to get a length in a function?",
       'answers': {1:"add",2:"len",3:"split"},
       'correct': 1
   }
'''

#print(d['Q1']['question'])
