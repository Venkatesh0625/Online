from tkinter import Tk, Text, Frame

window = Tk()

messages = Text(window)
messages.pack()

input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)

def Enter_pressed_custom(event):
    input_get = input_field.get()
    print(input_get)
    messages.insert(INSERT, '%s\n' % input_get)
    input_user.set('')
    return "break"

frame = Frame(window) 
input_field.bind("<Return>", Enter_pressed)
frame.pack()

window.mainloop()