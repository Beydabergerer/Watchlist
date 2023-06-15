from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Create button definition
def new():
    a = entry.get()
    if a != "":
        tree.insert('', 'end', text="1", values=a)
        entry.delete(0, "end")
    else:
        messagebox.showwarning("ALARM!")

# Delete Button definition
def delete():
        selected_items = tree.selection()
        for selected_item in selected_items:
            tree.delete(selected_item)

# erstellen eines Fenster mit tkinter

ws = Tk()
ws.geometry('600x450+500+200')
ws.title('🎬Watchlist🎥')
ws.resizable(width=False, height=False)
frame = Frame(ws)
frame.pack(pady=10)

s = ttk.Style()
s.theme_use('clam')

# Add a Treeview widget
tree = ttk.Treeview(ws, column=("c1", "c2"), show='headings', height=5)

tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Titel")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Genre")

# Insert the data in Treeview widget
tree.insert('', 'end', text="1", values=("rick and morty", 'comedy'))

tree.pack()

# erstellen der Tabelle mit:
# https://www.tutorialspoint.com/how-to-display-a-listbox-with-columns-using-tkinter

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

entry = Entry(ws)
entry.pack(pady=20)

frame = Frame(ws)
frame.pack(pady=20)

addB = Button(frame, text='+', command=new)
addB.pack(fill=BOTH, expand=True, side=LEFT)

delB = Button(frame, text='-', command=delete)
delB.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
