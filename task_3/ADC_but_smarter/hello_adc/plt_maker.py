import matplotlib.pyplot as plt
import numpy as np
import subprocess
import os

subprocess.run(["python", "terminal_but_smarter.py"])

data = []
time = []

relative_path = os.path.join("ADC_but_smarter", "hello_adc", "data.txt")

with open(relative_path, 'r') as file:
    for line in file:
        line = line.split()
        time.append(float(line[0]))
        data.append(float(line[1]))

fig, ax = plt.subplots(figsize=(16, 10))
ax.plot(time, data, label="V(t)",
        marker="", linestyle="-",
        color='k', linewidth=1, markevery=20)

ax.minorticks_on()
ax.grid(which = 'minor', color = 'grey', linestyle=':')

plt.title("Рис 1 Процесс заряда и разряда конденсатора в RC-цепочке", size=10)
plt.xlabel("Время, с", size=9)
plt.ylabel("Напряжение, В", size=9)
plt.legend()
plt.savefig('image_1.jpg')