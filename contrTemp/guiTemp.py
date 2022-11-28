from tkinter import *
from tkinter import ttk

tempTitle = {
    '1':'01.Темп. кухня пол',
    '2':'02.Темп. зал пол-стена',
    '3':'03.Темп. зал пол-окно',
    '4':'04.Темп. 2-й этаж комната-1',
    '5':'05.Темп. 2-й этаж комната-2',
    '6':'06.Темп. 2-й этаж комната-3',
    '7':'07.Темп. веранда воздух',
    '8':'08.Темп. веранда батарея-2',
    '9':'09.Темп. гараж',
    '10':'10.Темп. чердак',
    '11':'11.Темп. подача ТП',
    '12':'12.Темп. обратка-1 ТП',
    '13':'13.Темп. обратка-2 ТП',
    '14':'14.Темп. улица'
}

tempValue = {
    '1':'1',
    '2':'2',
    '3':'3',
    '4':'4',
    '5':'5',
    '6':'6',
    '7':'7',
    '8':'8',
    '9':'9',
    '10':'10',
    '11':'11',
    '12':'12',
    '13':'13',
    '14':'14'
}

def createLabelTitle(frame, titleVal):
        label = ttk.Label(frame, text=titleVal)
        label.pack(anchor=NW)
        return label

def createFrameControlTemp(distValue):
    frame = ttk.Frame(borderwidth = 1, relief=SOLID, padding=10)
    for titleLabel in distValue.values():
        createLabelTitle(frame, titleLabel)
    return frame

root = Tk()
root.title('Контроль температуры')
root.geometry('400x400+1500+100')

for c in range(2):root.columnconfigure(index=c, weight=1)
for i in range(2):root.rowconfigure(index=i)

title = ttk.Label(text='Измерение температуры.')
title.grid(row=0, column=0, columnspan=2, pady=[20, 20])

FrameControlTempTitle = createFrameControlTemp(tempTitle)
FrameControlTempTitle.grid(row=1, column=0, sticky=E)

FrameControlTempValue = createFrameControlTemp(tempValue)
FrameControlTempValue.grid(row=1, column=1, sticky=W)

root.mainloop()