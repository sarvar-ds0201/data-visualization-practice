from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('death_valley_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Извлечение дат и осадков.
dates, precipitations = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    precipitation = float(row[3])
    dates.append(current_date)
    precipitations.append(precipitation)

print(precipitations)

# Нанесение данных на диаграмму.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, precipitations, color='blue')

# Форматирование диаграммы.
ax.set_title("Daily Precipitation Death Valley - 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Precipitation', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
