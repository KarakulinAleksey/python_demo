from tkinter import *
from tkinter import ttk
from pathlib import Path
path = Path('img', 'apple.ico')
print(path)

def finish():
    # root.destroy()
    print('Close window')

root = Tk()
root.title('GUI')
# root.iconbitmap(default = path)
# root.iconphoto(False, PhotoImage(file=path))
root.geometry('200x100+800+200')
# root.attributes('-toolwindow', True)
# root.attributes("-alpha", 0.5)
# root.attributes("-fullscreen", True)
# root.resizable(False, False)
# root.minsize(200, 150)
# root.maxsize(400, 300)
# root.update_idletasks()
# print(root.geometry())
app = Frame(root)
# app.grid()
lbl = Label(app, text = 'Label text')
lbl.grid()
bttn_ttk = ttk.Button(text='ttk')
bttn_ttk.pack()
bttn1 = Button(app, text = 'bttn1')
bttn1.grid()
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = 'bttn2')

bttn_clicks = 0
def update_count():
    global bttn_clicks 
    bttn_clicks += 1
    bttn3['text'] = f'{bttn_clicks}'

bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "bttn3"
bttn3["command"] = update_count

# root.protocol('WM_DELETE_WINDOW', finish)

root.mainloop()
