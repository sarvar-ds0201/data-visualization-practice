import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)


# Задание заголовка диаграммы и меток осей.
ax.set_title("Cubes Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubes of Value", fontsize=14)

# Задание размера шрифта делений на осях.
ax.tick_params(labelsize=14)

# Задание диапазона для каждой оси.
ax.axis([0, 5100, 0, 130_000_000_000])
ax.ticklabel_format(style='plain')

plt.show()
