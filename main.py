import twitter
import reddit
import speech

import tkinter
from tkinter.ttk import Progressbar

pos = 0

def execute():
    global pos
    searchFor = str(search_for.get())

    result_twitter = twitter.search(searchFor)

    # Fake progress bar lmao
    progress['value'] = 50
    window.update_idletasks()

    listbox.insert(pos, result_twitter)
    pos += 1

    progress['value'] = 100

window = tkinter.Tk()
window.wm_geometry("600x500")

row = 0
l1 = tkinter.Label(window, text="Φωνητική Αναζήτηση σε ΜΚΔ!")
l1.grid(row=row)
row += 1

ltext = tkinter.Label(window, text="Κείμενο Αναζήτησης")
ltext.grid(row=row)
search_for = tkinter.Entry(window)
search_for.grid(row=row, column=1)
row += 1

b1 = tkinter.Button(window, text="Ψάξε", command=execute)
b1.grid(row=row)
row += 1

listbox = tkinter.Listbox(window)
listbox.grid(row=row)
row += 1

progress = Progressbar(window, orient=tkinter.HORIZONTAL, length=200)
progress.grid(row=row)
row += 1

window.mainloop()
