from tkinter import *
 
window = Tk()
 
window.title("Welcome to the project of CP19_48")
 
window.geometry('400x200')
 
lbl = Label(window, text="For Colour Detection ")
 
lbl.grid(column=0, row=0)
 
btn = Button(window, text="Click Here ")
 
btn.grid(column=1, row=0)
 
window.mainloop()