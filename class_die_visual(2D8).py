import plotly.express as px

from class_die import Die

# Создание кубиков D8.
die_1 = Die(8)
die_2 = Die(8)

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(1_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов.
title = "Results of Rolling Two D8 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Дальнейшая настройка диаграммы.
fig.update_layout(xaxis_dtick=1)

fig.show()
