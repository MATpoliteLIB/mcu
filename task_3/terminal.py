import serial
import time

ser = serial.Serial(
    port="COM9",
    baudrate=115200,
    timeout=1.0
)

# Ожидаем инициализацию Pico
time.sleep(2)  # Даём время на запуск
ser.reset_input_buffer()  # Очищаем буфер

while True:
    command = input("Введите команду (a): ")
    if not command:
        continue
    
    ser.write(command[0].encode())  # Отправляем только первый символ
    
    # Читаем всю строку ответа (до \n)
    response = ser.readline().decode().strip()
    if response:
        print(f"Напряжение: {response} V")