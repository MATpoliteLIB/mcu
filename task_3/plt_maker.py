import matplotlib.pyplot as plt
import numpy as np

data = []
time = []

with open("data.txt", 'r') as file:
    for line in file:
        line = line.split()
        time.append(float(line[0]))
        data.append(float(line[1]))

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(time, data, label="V(t)",
        marker="", linestyle="-",
        color='k', linewidth=1, markevery=20)

ax.minorticks_on()
ax.grid(which = 'minor', linewidth=0.3, linestyle=':')

plt.title("Процесс заряда и разряда конденсатора в RC-цепочке", size=12)
plt.xlabel('Время, сек.', fontsize = 12)
plt.ylabel('Напряжение, В',fontsize = 12)
plt.yticks(np.linspace(0, 3.5, 15))
plt.ylim(0,3.5)
plt.savefig('image_1.jpg')