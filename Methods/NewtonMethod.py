class NewtonMethod:
    """Метод Ньютона"""
    def __init__(self, f, f_prime, f_prime2, a, b, epsilon, max_iter=100):
        self.iterations = None
        self.f = f
        self.f_prime = f_prime
        self.a = a
        self.b = b
        self.epsilon = epsilon
        self.max_iter = max_iter
        self.f_prime2 = f_prime2
        self.root = None

    def check_convergence_condition(self):
        """Проверка условия сходимости"""
        if self.f(self.a) * self.f(self.b) >= 0:
            raise Exception("Неверный интервал: функция не меняет знак на [a, b].")

    def choose_initial(self):
        """Выбор начального приближения f(x)*f''(x) > 0"""
        if self.f(self.a) * self.f_prime2(self.a) > 0:
            return self.a
        else:
            return self.b

    def solve(self):
        """Основной метод класса"""
        self.check_convergence_condition()

        x_i = self.choose_initial()
        for i in range(1, self.max_iter + 1):
            f_x = self.f(x_i)
            f_prime_x = self.f_prime(x_i)
            if f_prime_x == 0:
                raise ZeroDivisionError(f"Производная равна нулю в точке x = {x_i}")
            x_new = x_i - f_x / f_prime_x
            if abs(x_new - x_i) < self.epsilon:
                self.root = x_new
                self.iterations = i
                return x_new
            x_i = x_new
        raise Exception("Метод Ньютона не сошелся за заданное число итераций.")
