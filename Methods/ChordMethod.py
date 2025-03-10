import numpy as np
import matplotlib.pyplot as plt


class ChordMethod:
    def __init__(self, f, f2, a, b, tol, max_iter=100):
        """
        f       : функция f(x)
        f2      : вторая производная f''(x)
        a, b    : границы интервала [a, b]
        tol     : требуемая точность
        max_iter: максимальное число итераций
        """
        if not callable(f) or not callable(f2):
            raise TypeError("f и f2 должны быть вызываемыми объектами (функциями).")

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("a и b должны быть числами.")

        if a >= b:
            t = b
            b = a
            a = t

        if not isinstance(tol, (int, float)) or tol <= 0:
            raise ValueError("tol должен быть положительным числом.")

        if not isinstance(max_iter, int) or max_iter <= 0:
            raise ValueError("max_iter должен быть положительным целым числом.")

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
        f_a = self.f(self.a)
        f_b = self.f(self.b)

        if f_a * f_b > 0:
            raise ValueError("На интервале нет корня или их несколько.")
        elif f_a == 0:
            return self.a
        elif f_b == 0:
            return self.b

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
        self.plot_function()
        interval_check = self.verify_interval()
        if isinstance(interval_check, (int, float)):
            self.root = interval_check
            self.iterations = 0
            self.error = abs(self.f(self.root))
            return self.root, self.f(self.root), self.iterations

        # Выбор начальных точек
        a, b = self.a, self.b
        iterations = 0

        while iterations < self.max_iter:
            try:
                # Вычисление нового приближения
                f_a = self.f(a)
                f_b = self.f(b)
                x_0 = a - ((b - a) / (f_b - f_a)) * f_a

                if np.isnan(x_0) or np.isinf(x_0):
                    raise ArithmeticError("Вычисленное значение x_0 является NaN или бесконечностью.")

                # Проверка условия сходимости
                if abs(self.f(x_0)) < self.tol:
                    self.root = x_0
                    self.iterations = iterations
                    self.error = abs(self.f(x_0))
                    return x_0, self.f(x_0), iterations

                # Обновление границ
                if self.f(x_0) * self.f(a) < 0:
                    b = x_0
                else:
                    a = x_0

                iterations += 1
            except ZeroDivisionError:
                raise ZeroDivisionError("Деление на ноль при вычислении нового приближения.")

        raise RuntimeError("Метод хорд не сошелся за заданное число итераций.")

    def plot_function(self, num_points=100):
        """
        Построение графика функции на интервале [a, b].

        :param num_points: Количество точек для построения графика.
        """
        if not isinstance(num_points, int) or num_points <= 0:
            raise ValueError("num_points должен быть положительным целым числом.")

        x_vals = np.linspace(self.a, self.b, num_points)
        y_vals = [self.f(x) for x in x_vals]

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
