from tkinter import *
from typing import Counter
import random

import os
# Set environment variable
#os.environ['TK_SILENCE_DEPRECATION'] = 1

root = Tk()
root.geometry("1500x800")
root["bg"] = "black"

userAnswers = []
questions = []
questionCounter = [0]

# Get 3 String answer Questions and 3 Integer answer question from the Question Bank
directory = os.getcwd()
# Get String Questions from Question Bank
fileName = directory + '/best-amazing-speedy-enduringbased/Code/QuestionBankStr.txt'
myFile = open(fileName, "r")
strQuestionsList = myFile.readlines()
for i in range(len(strQuestionsList)):
    strQuestionsList[i] = strQuestionsList[i].rstrip('\n')
    print(strQuestionsList[i])
myFile.close()

print("***************")

# Get Integer Questions from Question Bank
fileName = directory + '/best-amazing-speedy-enduringbased/Code/QuestionBankInt.txt'
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
    welcomeButton.place_forget()
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

    leftLabel = Label(root, text="Created By: Ahmad Jundi, TY, sarah", font=("Courier", 20), bg="black", fg="green")
    leftLabel.pack()
    leftLabel.place(x=20, y=750)

    welcomeButton = Button(root, text= "Click Here To Begin", font=("Courier", 32), bg= 'green', fg= 'black', command=deleteWelcomePage)
    welcomeButton.pack(pady=10) 
    welcomeButton.place(x=550, y=600)


# Directions/Description Page
def deleteDescriptionPage():
    descriptionPageLabel.pack_forget()
    descriptionPageLabel.place_forget()
    descriptionPageLabel1.pack_forget()
    descriptionPageLabel1.place_forget()
    descriptionPageLabel2.pack_forget()
    descriptionPageLabel2.place_forget()
    descriptionPageLabel3.pack_forget()
    descriptionPageLabel3.place_forget()
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
    descriptionPageLabel1.pack(pady=10)
    descriptionPageLabel1.place(x = 570, y = 20)
    descriptionPageLabel1["bg"] = "black"

    descriptionPageLabel = Label(root, text="This program is meant to help you create a strong password that is still simple to memorize!", font= "Consolas 20", foreground = "red")
    descriptionPageLabel.pack(pady=10)
    descriptionPageLabel.place(x = 40, y = 200)
    descriptionPageLabel["bg"] = "black"

    descriptionPageLabel2 = Label(root, text="You will be required to input the number of characters, between 10 and 25, you wish your\n password to be", font= "Consolas 20", foreground = "red")
    descriptionPageLabel2.pack(pady=10)
    descriptionPageLabel2.place(x = 40, y = 350)
    descriptionPageLabel2["bg"] = "black"

    descriptionPageLabel3 = Label(root, text="After this, you will need to answer 5 questions that will be used to create your new password", font= "Consolas 20", foreground = "red")
    descriptionPageLabel3.pack(pady=10)
    descriptionPageLabel3.place(x = 40, y = 500)
    descriptionPageLabel3["bg"] = "black"

    continueButton = Button(root, text= "Lets Go!", font=("Helvetica", 32), bg= 'green', fg= 'black', command=deleteDescriptionPage)
    continueButton.pack(pady=10)
    continueButton.place(x=650, y=600)



# Password Length Selector Page
def deletePasswordLengthPage():
    passwordLengthPageLabel.pack_forget()
    okButton.pack_forget()
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

    okButton = Button(root, text= "Okay", font= ("Courier", 12), command=deletePasswordLengthPage)
    okButton.pack(pady=10)

# Questions Page
def deleteQuestionPage():
    global questions
    questionPageLabel.pack_forget()
    submitQuestionButton.pack_forget()
    questionLabel.pack_forget()
    userAnswers.append(questionEntry.get())
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
    questionPageLabel.pack(pady=10)
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
    questionLabel.pack(pady=10)
    questionLabel["bg"] = "black"

    # Display Question Input Box
    questionEntry = Entry(root, width=50, font= ("Courier", 15), foreground= "green")
    questionEntry.pack(pady=10)
    questionEntry["bg"] = "black"

    print(questions)
    # Display Submit Button
    submitQuestionButton = Button(root, text= "Submit", font=("Courier", 12), command=deleteQuestionPage)
    submitQuestionButton.pack(pady=10)



# Display Finished Password Page
def deletePasswordPage():
    passwordPageLabel.pack_forget()
    startTestButton.pack_forget()
    startTestButton.place_forget()
    passwordLabel.pack_forget()
    

def displayPasswordPage():
    global startTestButton
    global passwordPageLabel
    global passwordLabel

    passwordPageLabel = Label(root, text="Your More Secure Password is Below!", font= "Courier 32", foreground = "green")
    passwordPageLabel.pack(pady=10)
    passwordPageLabel["bg"] = "black"

    passwordLabel = Label(root, text="Your Password", font= "Courier 25", foreground = "green")
    passwordLabel.pack(pady=10)
    passwordLabel["bg"] = "black"

    startTestButton = Button(root, text= "Start Memory Test!", font=("Courier", 32), bg= 'green', fg= 'black', command=deleteDescriptionPage)
    startTestButton.pack(pady=10)
    startTestButton.place(x=650, y=600)
    


displayWelcomePage()
root.mainloop()
