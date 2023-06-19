from ttkwidgets.autocomplete import AutocompleteEntry
from tkinter import *
from tkinter import messagebox
# Inhalte für Autocomplete, müssen später aus Datenbank entnommen werden
countries = [
      "Avengers Infinity War", "Avengers Endgame", "Godfather", "Psycho", "Harry Potter", "Blacklist", "oohioi", "kbjbjj", "Wubalubadubdub"
        ]
# Eintrag hinzufügen
def new():
    a = entry.get()
    if a != "":
        lb.insert(END, a)
        entry.delete(0, "end")
    else:
        messagebox.showwarning("ALARM!")
# Eintrag entfernen
def delete():
    lb.delete(ANCHOR)

#Fenster definieren
ws = Tk()
ws.geometry('500x450')
ws.title('🎬Watchlist🎥')

ws.resizable(width=False, height=False)
frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(frame, activestyle="none")
lb.pack(side=LEFT, fill=BOTH)

list = ['Rick and Morty']   # Inhalte Watchlist, müssen später in Datenbank gespeichert werden

for i in list:
    lb.insert(END, i)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

Label(text="Film hinzufügen").pack()

# Autocomplete mit gegebenen Inhalten
entry = AutocompleteEntry(completevalues=countries)
entry.pack(pady=20)

frame = Frame(ws)
frame.pack(pady=20)

# definieren von Buttons
addB = Button(frame, text='+', command=new)
addB.pack(fill=BOTH, expand=True, side=LEFT)

delB = Button(frame, text='-', command=delete)
delB.pack(fill=BOTH, expand=True, side=LEFT)



ws.mainloop()
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

entry = Entry(ws)
entry.pack(pady=20)

frame = Frame(ws)
frame.pack(pady=20)

addB = Button(frame, text='+', command=new)
addB.pack(fill=BOTH, expand=True, side=LEFT)

delB = Button(frame, text='-', command=delete)
delB.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
