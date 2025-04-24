import csv
import matplotlib.pyplot as plt

def read_bme280_data(filename):
    # Инициализируем пустые списки для данных
    times = []
    humidities = []
    pressures = []
    temperatures = []
    
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        
        for row in csv_reader:
            # Проверяем, что строка содержит все 4 значения
            if len(row) == 4:
                try:
                    times.append(float(row[0]))
                    humidities.append(float(row[1]))
                    pressures.append(float(row[2]))
                    temperatures.append(float(row[3]))
                except ValueError as e:
                    print(f"Ошибка преобразования данных в строке: {row}")
                    continue
    
    return times, humidities, pressures, temperatures

# Пример использования
filename = 'data_1.csv'
times, humidities, pressures, temperatures = read_bme280_data(filename)

fig = plt.figure(figsize=(10, 8))
gs = fig.add_gridspec(2, 2)  

ax1 = fig.add_subplot(gs[0, :])  
ax1.plot(times,humidities)
ax1.set_title('График зависимости влажности от времени')
ax1.set_xlabel('Время, сек.')
ax1.set_ylabel("Влажность, %")
ax1.grid(True)

# Второй график (нижняя левая ячейка)
ax2 = fig.add_subplot(gs[1, 0])  # 1-я строка, 0-й столбец
ax2.plot(times,pressures)
ax2.set_title('График зависимости давления от времени')
ax2.set_xlabel('Время, сек.')
ax2.set_ylabel('Давление, Па')
ax2.grid(True)

# Третий график (нижняя правая ячейка)
ax3 = fig.add_subplot(gs[1, 1])  # 1-я строка, 1-й столбец
ax3.plot(times, temperatures)
ax3.set_title('График зависимости температуры от времени')
ax3.set_xlabel('Время, сек')
ax3.set_ylabel(r'Температура, $^OC$')
ax3.grid(True)

# Настраиваем общий заголовок и отступы
#plt.suptitle('Измерения, полученные с датчика', fontsize=16)
plt.tight_layout()
plt.savefig("1.png")
plt.show()