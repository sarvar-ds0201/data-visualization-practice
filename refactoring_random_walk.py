from random import choice


class RandomWalk:
    """Класс для генерации случайных блужданий."""

    def __init__(self, num_points=5000):
        """Инициализирует атрибуты блуждания."""
        self.num_points = num_points

        # Все блуждания начинаются с точки (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Определяет направление и длину шага."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])

        step = direction * distance
        return step

    def fill_walk(self):
        """Вычисляет все точки блуждания."""

        # Шаги генерируются до достижения нужной длины.
        while len(self.x_values) < self.num_points:

            # Определение направления и расстояния по X и Y.
            x_step = self.get_step()
            y_step = self.get_step()

            # Пропуск шагов, не ведущих никуда.
            if x_step == 0 and y_step == 0:
                continue

            # Вычисление следующих координат.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
