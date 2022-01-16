from tkinter import *
from typing import Counter
import random
from createPassword import createPassword
import subprocess

import os
# Set environment variable
#os.environ['TK_SILENCE_DEPRECATION'] = 1

root = Tk()
root.geometry("1500x800")
root["bg"] = "black"

userAnswers = []
questions = []
questionCounter = [0]
hintCounter = [0]
passwordLength = 0
score = [15]

# Get 3 String answer Questions and 3 Integer answer question from the Question Bank
directory = os.getcwd()
# Get String Questions from Question Bank
fileName = directory + '/QuestionBankStr.txt'
myFile = open(fileName, "r")
strQuestionsList = myFile.readlines()
for i in range(len(strQuestionsList)):
    strQuestionsList[i] = strQuestionsList[i].rstrip('\n')
    print(strQuestionsList[i])
myFile.close()

print("***************")

# Get Integer Questions from Question Bank
fileName = directory + '/QuestionBankInt.txt'
myFile = open(fileName, "r")
intQuestionsList = myFile.readlines()
for i in range(len(intQuestionsList)):
    intQuestionsList[i] = intQuestionsList[i].rstrip('\n')
    print(intQuestionsList[i])
myFile.close()



# Welcome Page
def deleteWelcomePage():
    welcomeLabel.pack_forget()
    welcomeButton.pack_forget()
    #welcomeButton.place_forget()
    leftLabel.pack_forget()
    leftLabel.place_forget()
 
    displayDescriptionPage()

def displayWelcomePage(): 
    global welcomeButton
    global welcomeLabel
    global leftLabel

    welcomeLabel = Label(root, text="Welcome to BASED Password Generator! \n", font= "Courier 50", foreground = "green")
    welcomeLabel.pack(pady=190)
    welcomeLabel["bg"] = "black"

    leftLabel = Label(root, text="Created By: Ahmad Jundi, Ty Greve, Juan Fernandez, Saakshi Joshi.", font=("Courier", 20), bg="black", fg="green")
    leftLabel.pack()
    leftLabel.place(x=20, y=750)

    welcomeButton = Button(root, text= "Click Here To Begin", font=("Courier", 32), bg= 'green', fg= 'black', command=deleteWelcomePage)
    welcomeButton.pack(pady=20) 
    #welcomeButton.place(x=550, y=600)


# Directions/Description Page
def deleteDescriptionPage():
    descriptionPageLabel.pack_forget()
    #descriptionPageLabel.place_forget()
    descriptionPageLabel1.pack_forget()
    #descriptionPageLabel1.place_forget()
    descriptionPageLabel2.pack_forget()
    #descriptionPageLabel2.place_forget()
    descriptionPageLabel3.pack_forget()
    #descriptionPageLabel3.place_forget()
    continueButton.pack_forget()
    continueButton.place_forget()
    displayPasswordLengthPage()

def displayDescriptionPage():
    global continueButton
    global descriptionPageLabel
    global descriptionPageLabel1
    global descriptionPageLabel2
    global descriptionPageLabel3

    descriptionPageLabel1 = Label(root, text="PLEASE READ!", font= "Consolas 50 bold underline", foreground = "red")
    descriptionPageLabel1.pack(pady=50)
    #descriptionPageLabel1.place(x = 570, y = 20)
    descriptionPageLabel1["bg"] = "black"

    descriptionPageLabel = Label(root, text="This program is meant to help you create a strong password that is still simple to memorize!", font= "Consolas 20", foreground = "red")
    descriptionPageLabel.pack(pady=50)
    #descriptionPageLabel.place(x = 40, y = 200)
    descriptionPageLabel["bg"] = "black"

    descriptionPageLabel2 = Label(root, text="You will be required to input the number of characters, between 10 and 25, you wish your\n password to be", font= "Consolas 20", foreground = "red")
    descriptionPageLabel2.pack(pady=50)
    #descriptionPageLabel2.place(x = 40, y = 350)
    descriptionPageLabel2["bg"] = "black"

    descriptionPageLabel3 = Label(root, text="After this, you will need to answer 5 questions that will be used to create your new password", font= "Consolas 20", foreground = "red")
    descriptionPageLabel3.pack(pady=50)
    #descriptionPageLabel3.place(x = 40, y = 500)
    descriptionPageLabel3["bg"] = "black"

    continueButton = Button(root, text= "Lets Go!", font=("Helvetica", 32), bg= 'green', fg= 'black', command=deleteDescriptionPage)
    continueButton.pack(pady=10)
    continueButton.place(x=650, y=600)



# Password Length Selector Page
def deletePasswordLengthPage():
    global passwordLength
    passwordLengthPageLabel.pack_forget()
    okButton.pack_forget()
    okButton.place_forget()
    passwordLengthSelector.pack_forget()
    passwordLength = passwordLengthSelector.get()
    displayQuestionsPage()

def displayPasswordLengthPage(): 
    global okButton
    global passwordLengthPageLabel
    global passwordLengthSelector
    global passwordLength
    passwordLengthPageLabel = Label(root, text="Please select a password length and press 'Okay'", font= "Courier 35 ", foreground= "green")
    passwordLengthPageLabel.pack(pady=200)
    passwordLengthPageLabel["bg"] = "black"

    passwordLengthSelector = Scale(root, from_ = 10, to = 25, orient=HORIZONTAL, font=("Courier", 32), bg= 'green', fg= 'black')
    passwordLengthSelector.pack()

    okButton = Button(root, text= "Okay", font= ("Courier", 32), bg= 'green', fg= 'black', command=deletePasswordLengthPage)
    okButton.pack(pady=50)
    okButton.place(x=670, y=600)

# Questions Page
def deleteQuestionPage():
    global questions
    questionPageLabel.pack_forget()
    submitQuestionButton.pack_forget()
    submitQuestionButton.place_forget()
    questionLabel.pack_forget()
    userAnswers.append(questionEntry.get())
    questionEntry.pack_forget()
    print(len(questions) )
    questions.pop(0)
    print(userAnswers)
    questionCounter[0] += 1
    if questionCounter[0] == 6:
        displayPasswordPage()
    else:
        displayQuestionsPage()

def displayQuestionsPage(): 
    global submitQuestionButton
    global questionPageLabel 
    global questionLabel
    global questionEntry
    global questions
    questionPageLabel = Label(root, text="Please answer the following questions and press 'Submit' or press 'Skip' for a new question", font= "Courier 25 ",foreground= "green")
    questionPageLabel.pack(pady=50)
    questionPageLabel["bg"] = "black"

    # Get 3 String answer Questions and 3 Integer answer question from the Question Bank
    directory = os.getcwd()
    if questionCounter[0] < 3:
        questions = strQuestionsList.copy()
    else:
        questions = []
        questions = intQuestionsList.copy()

    # Shuffle Question list
    random.shuffle(questions)

    # Display Question
    questionLabel = Label(root, text=questions[0], font= "Courier 18 ",foreground= "green")
    questionLabel.pack(pady=100)
    questionLabel["bg"] = "black"

    # Display Question Input Box
    questionEntry = Entry(root, width=50, font= ("Courier", 15), foreground= "green")
    questionEntry.pack(pady=10)
    questionEntry["bg"] = "black"

    print(questions)
    # Display Submit Button
    submitQuestionButton = Button(root, text= "Submit", font=("Courier", 32), bg= 'green', fg= 'black', command=deleteQuestionPage)
    submitQuestionButton.pack(pady=50)
    submitQuestionButton.place(x=660, y = 550)



# Display Finished Password Page
def deletePasswordPage():
    passwordPageLabel.pack_forget()
    startTestButton.pack_forget()
    #startTestButton.place_forget()
    passwordLabel.pack_forget()
    copyButton.pack_forget()
    displayMemorizationPage1()

def copyToClipboard():
    subprocess.run("pbcopy", universal_newlines=True, input=createPassword(userAnswers, passwordLength))
    

def displayPasswordPage():
    global startTestButton
    global passwordPageLabel
    global passwordLabel
    global copyButton

    passwordPageLabel = Label(root, text="Your More Secure Password is Below!", font= "Courier 32", foreground = "green")
    passwordPageLabel.pack(pady=75)
    passwordPageLabel["bg"] = "black"

    passwordLabel = Label(root, text=createPassword(userAnswers, passwordLength), font= "Courier 25", foreground = "green")
    passwordLabel.pack(pady=50)
    passwordLabel["bg"] = "black"

    copyButton = Button(root, text= "Copy Password", font=("Courier", 32), bg= 'green', fg= 'black', command=copyToClipboard)
    copyButton.pack(pady=75)

    startTestButton = Button(root, text= "Start Memory Test!", font=("Courier", 32), bg= 'green', fg= 'black', command=deletePasswordPage)
    startTestButton.pack(pady=75)
    #tartTestButton.place(x=660, y=500)


# Delete Memorization Test Page 1
def deleteMemorizationPage1():
    memPage1Label.pack_forget()
    hintButton.pack_forget()
    hintLabel.pack_forget()
    checkButton.pack_forget()

    print("Tys: " + str(score))
    print(score[0])
    # If password is wrong update score
    if passwordEntry.get() != createPassword(userAnswers, passwordLength):
        score[0] = score[0] - 2

    passwordEntry.destroy()

    displayMemorizationPage2()

# Display Hint Page
def displayHint():
    global hintLabel
    global hintCounter
    hintLabel.pack_forget()
    hintLabel = Label(root, text="Your hint: " + userAnswers[hintCounter[0]], font= "Courier 25", foreground = "green")
    hintLabel.pack(pady=50)
    hintLabel["bg"] = "black"
    hintCounter[0] += 1
    score[0] = score[0] - 2

    
# Display Memorization Page 1
def displayMemorizationPage1():
    global hintButton
    global memPage1Label
    global hintLabel
    global passwordEntry
    global checkButton

    memPage1Label = Label(root, text="Try typing your new password below.", font= "Courier 32", foreground = "green")
    memPage1Label.pack(pady=75)
    memPage1Label["bg"] = "black"

    hintButton = Button(root, text= "I need a hint!", font=("Courier", 32), bg= 'green', fg= 'black', command=displayHint)
    hintButton.pack(pady=75)

    # Display Question Input Box
    passwordEntry = Entry(root, width=50, font= ("Courier", 15), foreground= "green")
    passwordEntry.pack(pady=10)
    passwordEntry["bg"] = "black"

    checkButton = Button(root, text= "Check my answer", font=("Courier", 32), bg= 'green', fg= 'black', command=deleteMemorizationPage1)
    checkButton.pack(pady=75)

    hintLabel = Label(root, text="Your hint: ", font= "Courier 25", foreground = "green")
    hintLabel.pack(pady=50)
    hintLabel["bg"] = "black"


# Delete Memorization Test Page 2
def deleteMemorizationPage2():
    memPage2Label.pack_forget()
    checkButton.pack_forget()

    if passwordEntry.get() != createPassword(userAnswers, passwordLength):
        score[0] = score[0] - 2

    passwordEntry.pack_forget()

    displayScorePage()

    
# Display Memorization Page 2
def displayMemorizationPage2():
    global memPage2Label
    global passwordEntry
    global checkButton

    # Display Instructions
    memPage2Label = Label(root, text="Try typing your new password below.", font= "Courier 32", foreground = "green")
    memPage2Label.pack(pady=75)
    memPage2Label["bg"] = "black"

    # Display Question Input Box
    passwordEntry = Entry(root, width=50, font= ("Courier", 15), foreground= "green")
    passwordEntry.pack(pady=10)
    passwordEntry["bg"] = "black"

    checkButton = Button(root, text= "Check my answer", font=("Courier", 32), bg= 'green', fg= 'black', command=deleteMemorizationPage2)
    checkButton.pack(pady=75)


# Delete Score Page
def deleteScorePage():
    scorePageLabel.pack_forget()
    finishButton.pack_forget()
    root.destroy()
    
# Display Score Page
def displayScorePage():
    global scorePageLabel
    global finishButton

    # Display Instructions
    scorePageLabel = Label(root, text="Your Memorization Score is: " + str(score[0]) + "/15!", font= "Courier 32", foreground = "green")
    scorePageLabel.pack(pady=150)
    scorePageLabel["bg"] = "black"

    finishButton = Button(root, text= "Finish!", font=("Courier", 32), bg= 'green', fg= 'black', command=deleteScorePage)
    finishButton.pack(pady=75)

    

displayWelcomePage()
root.mainloop()