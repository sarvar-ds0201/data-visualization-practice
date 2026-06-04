from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

name_path = input('Введите название csv файла(в формате name_file.csv): ')
path = Path(name_path)
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Находим индексы tmax, tmin, date и тд.
tmax_ind = header_row.index('TMAX')
tmin_ind = header_row.index('TMIN')
date_ind = header_row.index('DATE')
name_ind = header_row.index('NAME')


# Извлечение дат и максимальных температур.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[date_ind], '%Y-%m-%d')
    year = current_date.year
    name_place = row[name_ind]
    try:
        high = int(row[tmax_ind])
        low = int(row[tmin_ind])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Создание диаграммы максимальных температур.
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax.set_ylim(0, 140)

# Форматирование диаграммы.
ax.set_title(f"Daily High and Low Temperatures {name_place} - {year}", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()
