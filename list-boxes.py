from tkinter import * #Need to fix

root = Tk()
root.title('Codemy.com') 
root.iconbitmap('c:/gui/code.ico')
root.geometry("400x400")

#Listbox!
my_listbox = Listbox(root)
my_listbox.pack(pady=15)

#Add item to listbox
my_listbox.insert(END, "This is an item")
my_listbox.insert(END, "Second Item!")

#Add list of items
my
for item in my_list:
	my_listbox.insert(END, item)

	my_listbox.delete(END, item)

my_button = Button(root, text="Delete", command=)	

root.mainloop()









