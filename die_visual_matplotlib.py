import matplotlib.pyplot as plt

from class_die import Die

# Создание кубика D8.
die_1 = Die(8)
die_2 = Die(8)

# Моделирование серии бросков с сохранением результатов в списке.
results = [die_1.roll() + die_2.roll() for roll_num in range(1_000)]

# Анализ результатов.
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
frequencies = [results.count(value) for value in poss_results]

# Строим столбчатую диаграмму частот результатов бросков.
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
ax.bar(poss_results, frequencies)

# Задание заголовок диаграммы и меток осей.
ax.set_title("Results of Rolling Two D8 1,000 Times", fontsize=24)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency of Result", fontsize=14)
ax.tick_params(labelsize=14)


plt.show()
