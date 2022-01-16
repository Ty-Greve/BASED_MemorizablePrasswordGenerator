from tkinter import *
from typing import Counter

#import os
# Set environment variable
#os.environ['TK_SILENCE_DEPRECATION'] = 1

root = Tk()
root.geometry("1500x800")
root["bg"] = "black"

# Welcome Page
def deleteWelcomePage():
    welcomeLabel.pack_forget()
    welcomeButton.pack_forget()
    welcomeEntry.pack_forget()
    displayPasswordLengthPage()

def displayWelcomePage(): 
    global welcomeButton
    global welcomeLabel
    global welcomeEntry  
    welcomeLabel = Label(root, text="Welcome to BASED Password Generator!", font= "Courier 50", foreground = "green")
    welcomeLabel.pack(pady=190)
    welcomeLabel["bg"] = "black"

    welcomeEntry = Entry(root, width=50, font= ("Courier", 15), foreground= "green")
    welcomeEntry.pack(pady=10)
    welcomeEntry["bg"] = "black"

    welcomeButton = Button(root, text= "Start", font=("Courier", 12), bg= 'black', fg= 'green', command=deleteWelcomePage)
    welcomeButton.pack(pady=10)   


# Password Length Selector Page
def deletePasswordLengthPage():
    passwordLengthPageLabel.pack_forget()
    okButton.pack_forget()
    passwordLengthSelector.pack_forget()
    displayQuestionsPage()

def displayPasswordLengthPage(): 
    global okButton
    global passwordLengthPageLabel
    global passwordLengthSelector  
    passwordLengthPageLabel = Label(root, text="Please select a password length and press 'Okay'", font= "Courier 25 ", foreground= "green")
    passwordLengthPageLabel.pack(pady=10)
    passwordLengthPageLabel["bg"] = "black"

    passwordLengthSelector = Scale(root, from_ = 10, to = 25, orient=HORIZONTAL)
    passwordLengthSelector.pack()

    okButton = Button(root, text= "Okay", command=deletePasswordLengthPage)
    okButton.pack(pady=10)

# Questions Page
def deleteQuestionPage():
    questionPageLabel.pack_forget()
    submitQuestionButton.pack_forget()

def displayQuestionsPage(): 
    global submitQuestionButton
    global questionPageLabel  
    questionPageLabel = Label(root, text="Please answer the following questions and press 'Submit' or press 'Skip' for a new question", font= "Courier 25 ",foreground= "green")
    questionPageLabel.pack(pady=10)
    questionPageLabel["bg"] = "black"

    submitQuestionButton = Button(root, text= "Submit", command=deleteQuestionPage)
    submitQuestionButton.pack(pady=10)
    


displayWelcomePage()
root.mainloop()
