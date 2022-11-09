from tkinter import Tk, Scrollbar

root = Tk()
root.geometry("300x400")
ip_addr = []
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT,fill = Y)
for i in range(1,11):
    ip_addr.append(Button(root,text = str(i),bg = "grey",fg = "black",command = lambda:print("Hello"),padx = 10,pady = 10,height = 1,width = 5))
    ip_addr[i-1].pack()    
root.mainloop()