#Python #tkinter high level graphics => lesson One ("1")

#>>> put in your pyCharm (or IDE for Python)
lecture 38, just part of the code 

def open window():
	# top = toplevel
top title('top window')
top.geometry("300x300x120+120")
button1 = BUtton(top, text="close", command=top.destroy)
button.pack()

root = Tk()
button = Button(root, text="open window", command=open_window)
button.pack()

root.geometry("300x300+120+120")
root.mainloop()