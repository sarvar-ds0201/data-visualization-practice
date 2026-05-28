import plotly.express as px

from random_walk import RandomWalk

# Создание случайного блуждания
rw = RandomWalk(5000)
rw.fill_walk()

# Визуализация через Plotly
fig = px.line(
    x=rw.x_values,
    y=rw.y_values,
    title="Random Walk"
)

fig.show()
