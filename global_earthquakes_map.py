from pathlib import Path
import json

import plotly.express as px

# Считывает данные в строковом формате и преобразует в объект Python.
path = Path('eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Создает удобную для чтения версию файла данных.
path = Path('eq_data_1_day_m1.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Обработка всех землетрясений в наборе данных.
all_eq_dicts = all_eq_data['features']
ge_title = all_eq_data['metadata']['title']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])


title = ge_title
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()
