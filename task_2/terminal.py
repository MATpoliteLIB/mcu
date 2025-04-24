import serial
import time as tm

ser = serial.Serial(
    port="COM9", 
    baudrate=115200, 
    timeout=1.0
    )

while True:
    print("\nКоманда 'e' - включение LED \nКоманда 'd' - выключение LED \nКоманда 'r' - работа с памятью")
    command = input("Введите команду: ")[0]  # Берём только первый введённый символ
    if (command == 'e'):
        ser.write('e'.encode('ascii'))
        tm.sleep(1)
    elif (command == 'd'):
        ser.write('d'.encode('ascii'))
        tm.sleep(1)
    elif (command == 'r'):  # 0x20000000
        ser.write('r'.encode('ascii'))
        byte = input('Введите 10-символьный шестнадцатеричный адрес: ')
        ser.write(byte.encode('ascii'))
        print(ser.read(20).decode('ascii'))