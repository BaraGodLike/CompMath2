class ChordMethod:
    def __init__(self, f, f2, a, b, tol, max_iter=100):
        """
        f       : функция f(x)
        f2      : вторая производная f''(x)
        a, b    : границы интервала [a, b]
        tol     : требуемая точность
        max_iter: максимальное число итераций
        """
        self.f = f
        self.f2 = f2
        self.a = a
        self.b = b
        self.tol = tol
        self.max_iter = max_iter
        self.root = None
        self.iterations = 0
        self.error = None

    def verify_interval(self):
        """
        Проверка наличия корня на интервале [a, b].
        Корень существует, если функция меняет знак на концах интервала.
        """
        if self.func(self.a) * self.func(self.b) > 0:
            raise ValueError("На интервале нет корня или их несколько.")
        return True

    def solve(self):
        """
        Нахождение корня методом хорд.

        :return: Кортеж (root, func_value, iterations), где:
                 root - найденный корень,
                 func_value - значение функции в корне,
                 iterations - количество выполненных итераций.
        """
        # Проверка интервала
        self.verify_interval()

        # Выбор начальных точек
        a, b = self.a, self.b
        iterations = 0

        while iterations < self.max_iter:
            # Вычисление нового приближения
            f_a = self.func(a)
            f_b = self.func(b)
            x_0 = a - ((b - a) / (f_b - f_a)) * f_a
            # Проверка условия сходимости
            if abs(self.func(x_0)) < self.tol:
                return x_0, self.func(x_0), iterations

            # Обновление границ
            if self.func(x_0) * self.func(a) < 0:
                b = x_0
            else:
                a = x_0

            iterations += 1

        raise RuntimeError("Метод хорд не сошелся за заданное число итераций.")

    def plot_function(self, num_points=100):
        """
        Построение графика функции на интервале [a, b].

        :param num_points: Количество точек для построения графика.
        """
        x_vals = np.linspace(self.a, self.b, num_points)
        y_vals = [self.func(x) for x in x_vals]

        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label="f(x)")
        plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
        plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
        plt.title("График функции")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.legend()
        plt.show()
