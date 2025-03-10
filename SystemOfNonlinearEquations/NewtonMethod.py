class NewtonMethod:
    def __init__(self, system, eps=1e-6, max_iter=100):
        self.system = system
        self.eps = eps
        self.max_iter = max_iter
        self.iterations = 0
        self.errors = []

    def compute_functions(self, x, y):
        return self.system['functions'](x, y)

    def compute_jacobian(self, x, y):
        return self.system['jacobian'](x, y)

    def solve(self, x0, y0):
        x_prev, y_prev = x0, y0
        for self.iterations in range(self.max_iter):
            # Вычисляем значения функций
            f1, f2 = self.compute_functions(x_prev, y_prev)

            # Вычисляем якобиан
            [[J11, J12], [J21, J22]] = self.compute_jacobian(x_prev, y_prev)

            # Вычисляем определитель якобиана
            det = J11 * J22 - J12 * J21
            if abs(det) < 1e-12:
                raise ValueError("Определитель якобиана близок к нулю")

            # Решаем систему J * delta = -F методом Крамера
            dx = (-f1 * J22 - (-f2) * J12) / det
            dy = (J11 * (-f2) - (-f1) * J21) / det

            # Обновляем приближение
            x_new = x_prev + dx
            y_new = y_prev + dy

            # Вычисляем погрешность
            error = math.sqrt((x_new - x_prev) ** 2 + (y_new - y_prev) ** 2)
            self.errors.append(error)

            # Вывод информации о текущей итерации
            print(f"\nИтерация {self.iterations + 1}:")
            print(f"Текущее приближение: x = {x_new:.6f}, y = {y_new:.6f}")
            print(f"Погрешность: {error:.2e}")

            # Проверка на сходимость
            if error < self.eps:
                break

            x_prev, y_prev = x_new, y_new

        # Проверка решения
        f1_final, f2_final = self.compute_functions(x_new, y_new)
        if abs(f1_final) > self.eps * 100 or abs(f2_final) > self.eps * 100:
            raise ValueError("Решение не сошлось")

        return x_new, y_new
