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
    continueButton.pack_forget()
    continueButton.place_forget()
    displayPasswordLengthPage()

def displayDescriptionPage():
    global continueButton
    global descriptionPageLabel

    descriptionPageLabel = Label(root, text="You are going to recieve a set of instructions.", font= "Courier 32", foreground = "green")
    descriptionPageLabel.pack(pady=190)
    descriptionPageLabel["bg"] = "black"

    continueButton = Button(root, text= "Lets Go!", font=("Courier", 32), bg= 'green', fg= 'black', command=deleteDescriptionPage)
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
    questionPageLabel.pack_forget()
    submitQuestionButton.pack_forget()
    questionLabel.pack_forget()
    userAnswers.append(questionEntry.get())
    print(userAnswers)

def displayQuestionsPage(): 
    global submitQuestionButton
    global questionPageLabel 
    global questionLabel
    global questionEntry
    questionPageLabel = Label(root, text="Please answer the following questions and press 'Submit' or press 'Skip' for a new question", font= "Courier 25 ",foreground= "green")
    questionPageLabel.pack(pady=10)
    questionPageLabel["bg"] = "black"

    # Get Question from Question Bank
    directory = os.getcwd()
    fileName = directory + '/best-amazing-speedy-enduringbased/Code/QuestionBank.txt'
    myFile = open(fileName, "r")
    questions = myFile.readlines()
    for i in range(len(questions)):
        questions[i] = questions[i].rstrip('\n')
        print(questions[i])
    myFile.close()

    random.shuffle(questions)

    # Display Question
    questionLabel = Label(root, text=questions[0], font= "Courier 25 ",foreground= "green")
    questionLabel.pack(pady=10)
    questionLabel["bg"] = "black"

    # Display Question Input Box
    questionEntry = Entry(root, width=50, font= ("Courier", 15), foreground= "green")
    questionEntry.pack(pady=10)
    questionEntry["bg"] = "black"

    # Display Submit Button
    submitQuestionButton = Button(root, text= "Submit", font=("Courier", 12), command=deleteQuestionPage)
    submitQuestionButton.pack(pady=10)
    


displayWelcomePage()
root.mainloop()
