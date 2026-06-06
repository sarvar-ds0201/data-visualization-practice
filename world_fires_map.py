from pathlib import Path
import csv
import plotly.express as px
from datetime import datetime

path = Path('world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Находим индексы .
longitude_ind = header_row.index('longitude')
latitude_ind = header_row.index('latitude')
date_ind = header_row.index('acq_date')
brightness_ind = header_row.index('bright_t31')
frp_ind = header_row.index('frp')

# Извлечение координат, дат и тд
lons, lats, brightness, frps = [], [], [], []
for row in reader:
    current_date = datetime.strptime(row[date_ind], '%Y-%m-%d')
    try:
        lon = float(row[longitude_ind])
        lat = float(row[latitude_ind])
        brightn = float(row[brightness_ind])
        frp = float(row[frp_ind])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        lons.append(lon)
        lats.append(lat)
        brightness.append(brightn)
        frps.append(frp)

fig = px.scatter_geo(lat=lats, lon=lons, size=frps,
                     title=f"World fires 1-day, {current_date.strftime('%Y-%m-%d')}",
                     color=brightness,
                     color_continuous_scale='YlOrRd',
                     labels={'color': 'Brightness', 'size': 'FRP'},
                     projection='natural earth',
                     size_max=18,
                     opacity=0.6
                     )
fig.show()




