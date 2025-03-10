import numpy as np


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

    def check_convergence_condition(self):
        """Проверка достаточного условия сходимости"""
        line = np.linspace(self.a, self.b, 100)
        maxi = max(abs(self.phi_prime(x)) for x in line)
        if maxi >= 1:
            raise Exception(f"Достаточное условие сходимости не выполнено: max|phi'(x)| = {maxi:.4f} >= 1")
        return True

    def choose_initial(self):
        """Выбор начального приближения"""
        return (self.a + self.b) / 2

    def solve(self):
        """Основной метод класса"""
        if not (self.check_convergence_condition()):
            return

        x_i = self.choose_initial()
        for i in range(1, self.max_iter + 1):
            x_new = self.phi(x_i)
            if abs(x_new - x_i) < self.epsilon:
                self.root = x_new
                self.iterations = i
                return x_new
            x_i = x_new
        raise Exception("Метод простой итерации не сошелся за заданное число итераций.")
