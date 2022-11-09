from tkinter import Tk, Text, Frame

window = Tk()

messages = Text(window)
messages.pack()

input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)


frame = Frame(window) 
input_field.bind("<Return>", Enter_pressed)
frame.pack()

window.mainloop()