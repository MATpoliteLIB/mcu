import serial
import time as tm

ser = serial.Serial(
    port="COM9", 
    baudrate=115200, 
    timeout=1.0
)

def read_line(ser):
    """Чтение одной строки с последовательного порта"""
    line = b''
    while True:
        c = ser.read(1)
        if c == b'\n' or c == b'':
            break
        line += c
    return line.decode('utf-8').strip()

while True:
    prog_begin = input('Введите i для начала сбора информации: ')
    if prog_begin == 'i':
        all_time = float(input('Введите время измерений (в секундах): '))
        print("Запуск сбора информации...")
        
        with open('data_1.csv', 'w') as file:
            # Записываем заголовки столбцов
            file.write("Время (сек);Влажность (%);Давление (Па);Температура (°C)\n")
            
            ser.write('i'.encode('ascii'))
            start_time = tm.time()
            
            while tm.time() - start_time <= all_time:
                try:
                    # Отправляем запрос данных
                    ser.write('i'.encode('ascii'))
                    
                    # Читаем данные с датчика
                    humidity = read_line(ser)
                    pressure = read_line(ser)
                    temperature = read_line(ser)
                    
                    # Рассчитываем текущее время
                    current_time = tm.time() - start_time
                    
                    # Формируем строку для записи
                    data_line = f"{current_time:.2f};{humidity};{pressure};{temperature}\n"
                    
                    # Записываем в файл и выводим в консоль
                    file.write(data_line)
                    print(data_line.strip())  # Вывод без лишних переносов
                    
                    # Небольшая пауза между измерениями
                    tm.sleep(0.5)
                    
                except Exception as e:
                    print(f"Ошибка: {e}")
                    tm.sleep(1)  # Пауза при ошибке
        
        print(f"\nЗавершено! Данные сохранены в data_1.csv\n")