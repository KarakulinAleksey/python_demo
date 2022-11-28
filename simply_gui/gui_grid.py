from tkinter import *
from tkinter import ttk 

root = Tk()
root.title('позициирование grid')
root.geometry('300x300')

for columnIndex in range(3):
    # if columnIndex == 1:
    #     root.columnconfigure(index=columnIndex, weight=2)
    # else:
        root.columnconfigure(index=columnIndex, weight=1)

for rowIndex in range(3):
    root.rowconfigure(index=rowIndex, weight=1)

numberLabel = 0

for rowGrid in range(3):
    for columnGrid in range(3):
        numberLabel += 1
        label = ttk.Label(text=f'label{numberLabel}', borderwidth=2, relief='solid', width=40, foreground="#B71C1C", background="#FFCDD2")
        label.grid(row=rowGrid, column=columnGrid, ipadx=160, ipady=256, padx=4, pady=4)

root.mainloop()



