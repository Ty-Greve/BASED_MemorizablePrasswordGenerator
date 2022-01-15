from tkinter import *
import pygame
root = Tk()
root.title('Password Generator')
root.iconbitmap('c:/Users/akjun/Documents/Sound Effects/Play_icon.png')
root.geometry("500x400")

pygame.mixer.init()

def play():
    pygame.mixer.music.load("c:/Users/akjun/Documents/Sound Effects/Correct-answer.mp3")
    pygame.mixer.music.play(loops=0)

my_button = Button(root, text="Play Song", font=("Helvetica:", 32), command=play)
my_button.pack(pady=20)

root.mainloop()
