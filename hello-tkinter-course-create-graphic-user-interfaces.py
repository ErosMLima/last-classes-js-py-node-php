from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5, bg="gray", fg="lightgreen")
e.pack()

def myClick():
    myLabel = label(root, text=e.get())
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, padx=150, pady=100)
myButton.pack()


root.mainloop()
break




#Hanoi towEr problem with 3 disks
#Solving problems algorithms 



def move(f,t) :
	print("Move disc from {} to {}!".format(f,t))

def hanoi(n,f,h,t):
	hanoi(n-1,f,t,h)
	move(f,t)
	hanoi(n-1, h,f,t)

hanoi(4, "A", "B", "C")	




#Recursion Wrong Way

#