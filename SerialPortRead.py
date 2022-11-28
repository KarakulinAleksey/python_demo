import serial
import time

def readAnalogVal(adress, number_of_channels):
    values_channels = {}
    for channel in range(0, number_of_channels):
        command_write_sp = f'#0{adress}{channel}\r'
        sp.write(command_write_sp.encode('UTF-8'))
        # print(command_write_sp.encode('UTF-8'))
        time.sleep(0.1)
        value_channel = sp.read_all()
        values_channels[channel] = value_channel.decode('UTF-8')[1:-1]
        # print(channel, float(value_channel.decode('ascii')[1:10]))
    return values_channels


while True:
    values_channels_moduls = {}
    sp = serial.Serial(port ='COM3', 
                       baudrate = 9600, 
                       bytesize = 8, 
                       timeout = 100, 
                       stopbits = serial.STOPBITS_ONE, 
                       parity = serial.PARITY_NONE
                       )

    values_channels_module1 = readAnalogVal(adress=1, number_of_channels=6) 
    print('value_channels_module1', values_channels_module1)
    
    values_channels_module2 = readAnalogVal(adress=3, number_of_channels=8)                       
    print('value_channels_module2', values_channels_module2)

    sp.close()

    values_channels_moduls['1'] = values_channels_module1
    values_channels_moduls['2'] = values_channels_module2

    print('values_channels_moduls', values_channels_moduls)


