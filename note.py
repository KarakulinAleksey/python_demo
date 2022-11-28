import serial
import time
from tkinter import *
import string
#import threading
import locale
import chardet

print(locale.getpreferredencoding())



# tk = Tk()
# btn = Button(tk, text='Ok', command=hello)
# btn.pack()
# tk.mainloop()

#while True:
    #hello()
    #time.sleep(1)
    #timer = threading.Timer(1, hello)
    #timer.start()

def readAnalogVal(adress, number_of_channels):
    for channel in range(0, number_of_channels):
        # time.sleep(0.5)
        command_write_sp = f'#0{adress}{channel}\r'
        sp.write(command_write_sp.encode('UTF-8'))
        print(command_write_sp.encode('UTF-8'))
        time.sleep(0.5)
        value_channel = sp.read_all()
        # print(channel, float(value_channel.decode('utf-8')[1:10]))
        print(channel, float(value_channel.decode('ascii')[1:10]))
        # print(channel, float(ascii(value_channel)[2:10]))
        # print(channel, value_channel)


while True:
   
    sp = serial.Serial(port ='COM3', 
                       baudrate = 9600, 
                       bytesize = 8, 
                       timeout = None, 
                       stopbits = serial.STOPBITS_ONE, 
                       parity = serial.PARITY_NONE,
                       xonxoff = False,
                       rtscts = False,
                       dsrdtr = False,
                       writeTimeout = None
                       )

    sp.flushInput() #flush input buffer, discarding all its contents
    sp.flushOutput() #flush output buffer, aborting current output 
                 #and discard all that is in buffer

    readAnalogVal(adress=1, number_of_channels=6) 
    readAnalogVal(adress=3, number_of_channels=8)                       
    #time.sleep(0.5)
    # command_write_sp = '#014\r\n'
    # sp.write(b'#014\r')
    
    # time.sleep(0.5)
    # value_channel = sp.read(58)
    # value_channel = sp.read(42)
    # value_channel = sp.read_all()
    #value_channel = sp.read_until('\r', 9)
        # print(channel, float(value_channel.decode('utf-8')[1:10]))
    # print(value_channel.decode('unicode_escape'))
    # print(chardet.detect('ZŠŠÊrÊ¢jþ'))
    # print(value_channel.decode('ascii'))
    
    # print(''.join(chr(x) for x in value_channel))
            # value = ''
            # for i in range(4, 10):
            #     value = value + str(readSP)[i]
            # print(float(value))
            # print(sp.is_open)
    sp.close()

#adam-4017 python
#https://tproger.ru/translations/unicode-and-encoding-python-guide/#121_1
#http://plc-blog.com.ua/obzor-adam-4017
#https://pyserial.readthedocs.io/en/latest/examples.html#miniterm
#https://habr.com/ru/post/340196/
#https://docviewer.yandex.ru/view/91210595/?page=41&*=vxhBL0oVqsiqC3JcgQj47qNIWvR7InVybCI6Imh0dHA6Ly9lbGliLnNmdS1rcmFzLnJ1L2JpdHN0cmVhbS9oYW5kbGUvMjMxMS8zNDQ5NC92a3ItMS5wZGY%2Fc2VxdWVuY2U9MSIsInRpdGxlIjoidmtyLTEucGRmP3NlcXVlbmNlPTEiLCJub2lmcmFtZSI6dHJ1ZSwidWlkIjoiOTEyMTA1OTUiLCJ0cyI6MTY2ODA3MDcyNDk0OCwieXUiOiI2MDgzNjQ3MjQxNjYzODQxOTQyIiwic2VycFBhcmFtcyI6InRtPTE2NjgwNjU5NDgmdGxkPXJ1Jm5hbWU9dmtyLTEucGRmP3NlcXVlbmNlPTEmdGV4dD1hZGFtLTQwMTcrcHl0aG9uJnVybD1odHRwJTNBLy9lbGliLnNmdS1rcmFzLnJ1L2JpdHN0cmVhbS9oYW5kbGUvMjMxMS8zNDQ5NC92a3ItMS5wZGYlM0ZzZXF1ZW5jZSUzRDEmbHI9MTExMTMmbWltZT1wZGYmbDEwbj1ydSZzaWduPTM1Y2YxMmFkMzcxMzg3YmUzNzUyZGJkOGNlOWZjZWI0JmtleW5vPTAifQ%3D%3D