from tkinter import *


window = Tk()

window.geometry("720x360")
window.title("water")

tag = Label(window,text="water")
tag.pack()

button=Button(window,text="Submit")
button.pack()
window.mainloop()
