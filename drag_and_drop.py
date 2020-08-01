from tkinter import * #Doenst work need fix
from tkinter import ttk

root = Tk()
root.title('Websites 4> Creators ')
root.iconbitmap('c:/code.jpg')
root.geometry('400x400')

def selected(event):
	#myLabel = Label(root, text=clicked.get()).pack()
	if clicked.get() == 'Friday':
		myLabel = Label(root, text="Yay! It's Friday").pack()
	else:
		myLabe = Label(root, text=clicked.get()).pack()

def comboclick(event):
	myLabel = Label(root, text=myCombo.get()).pack()


options = [
	"Monday",
	"Tuestay",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday",
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack(pady=20)

myCombo = tkk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)

root.mainloop()