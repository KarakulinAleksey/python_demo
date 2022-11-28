from tkinter import *
from tkinter import ttk

root = Tk()
root.title('позициирование pack')
root.geometry('250x200')

btn = ttk.Button(text='button')
btn.pack(expand=1)

root.mainloop()