import numpy as np
import matplotlib.pyplot as plt


class SimpleIterationMethod:
    """Метод простой итерации"""
    def __init__(self, f, phi, phi_prime, a, b, epsilon, max_iter=100):
        self.iterations = None
        self.f = f
        self.phi = phi
        self.phi_prime = phi_prime
        self.a = a
        self.b = b
        self.epsilon = epsilon
        self.max_iter = max_iter
        self.root = None
        self.error = None

    def check_convergence_condition(self):
        """Проверка достаточного условия сходимости"""
        line = np.linspace(self.a, self.b, 100)
        maxi = max(abs(self.phi_prime(x)) for x in line)
        if maxi >= 1:
            raise Exception(f"Достаточное условие сходимости не выполнено: max|phi'(x)| = {maxi:.4f} >= 1")

    def choose_initial(self):
        """Выбор начального приближения"""
        return (self.a + self.b) / 2

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
        """Основной метод класса"""
        self.plot_function()
        self.check_convergence_condition()
        self.verify_interval()
        x_i = self.choose_initial()
        for i in range(1, self.max_iter + 1):
            x_new = self.phi(x_i)
            if abs(x_new - x_i) < self.epsilon:
                self.root = x_new
                self.iterations = i
                self.error = self.f(self.root)
                return x_new, self.error, i
            x_i = x_new
        raise Exception("Метод простой итерации не сошелся за заданное число итераций.")

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