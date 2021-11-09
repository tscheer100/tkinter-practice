import os
from tkinter import *

# key down function
def click():
    entered_text=textentry.get() 
    output.delete(0.0, END)
    try:
        definition = my_dict[entered_text]
    except:
        definition = "Sorry, there is no definition for that word. Please try again"
    output.insert(END, definition)

# close window function
def close_window():
    window.destroy()
    exit()

### directory handling
# print("the cwd is =============", os.getcwd())
os.chdir('c:/Users/Turtle/Documents/vscode projects/tkinter/')

### main
window = Tk()
window.title("My Computer Science Glossary")
window.configure(background='black')

### my photo
photo1 = PhotoImage(file='turtle.gif')
Label (window, image=photo1, bg='black') .grid(row=0, column=0, sticky=E)

# create label
Label (window, text="Enter the word you would like a definition for:", bg='black', fg ='white', font="none 12 bold") .grid(row=1, column=0, sticky=W)

# create a text entry box
textentry = Entry(window, width=20, bg='white')
textentry.grid(row=2, column=0, sticky=W)

# add a submit button
Button(window, text='Submit', width=6, command=click) .grid(row=3, column=0, sticky=W)

# create a def label
Label (window, text="\nDefinition:", bg='black', fg='white', font="none 12 bold") .grid(row=4, column=0, sticky=W)

# create a text box
output = Text(window, width=75, height=6, wrap=WORD, background='white')
output.grid(row=5, column=0, columnspan=2, sticky=W)

# create the dictionary
my_dict = {
    'algorithm': 'step by step instructions to complete a task',
    'bug': 'a piece of code that causes a program to fail'
}

# add an exit label
Label (window, text="Click to exit:", bg='black', fg='white', font="none 12 bold") .grid(row=6, column=0, sticky=W)

# add an exit button
Button(window, text='Exit', width=14, command=close_window) .grid(row=7, column=0, sticky=W)

window.mainloop()