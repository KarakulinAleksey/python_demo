from tkinter import *
from tkinter import ttk

root = Tk()
root.title('позициирование place')
root.geometry('250x200')

lb_1 = ttk.Label(root, text='Label_1', borderwidth=1, relief='solid')
# lb_1.place(x=20, y=30)
lb_1.place(relx=.5, rely=.5, anchor=CENTER)

bt_1 = ttk.Button(text='button_1')
bt_1.place(relx=0.1, rely=0.5, anchor=W)

root.mainloop()