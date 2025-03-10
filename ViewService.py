import FunctionService


class ViewService:
    """Класс для ввода и вывода данных"""

    def __init__(self):
        self.mode = None
        self.mode_output = None
        self.eq = None
        self.method = None

    def start(self):
        """Возвращает выражение и метод"""
        print("Введите номер уравнения:")
        for i in sorted(FunctionService.equations.keys()):
            print(f"\t{i}: {FunctionService.equations[i]['description']}")
        num = input()
        if num not in ["1", "2", "3", "4"]:
            raise ValueError("Недействительный номер уравнения!")
        self.eq = int(num)

        print("Введите номер метода:")
        print("1: Метод хорд")
        print("2: Метод Ньютона")
        print("3: Метод простой итерации")
        num = input()
        if num not in ["1", "2", "3"]:
            raise ValueError("Недействительный номер метода!")
        self.method = int(num)

        print("0 - клавиатура")
        print("1 - файл 'input.txt' (<a> <b> <epsilon> <mode_output>)")
        num = input("Выберите способ ввода данных: ")
        if num not in ["0", "1"]:
            raise ValueError("Недействительный способ ввода")
        self.mode = int(num)

        return self.eq, self.method

    def from_keyboard(self):
        a = input("Введите левую границу интервала 'a': ")
        try:
            float(a)
        except ValueError:
            raise ValueError("'a' должно быть числом!")

        b = input("Введите правую границу интервала 'b': ")
        try:
            float(b)
        except ValueError:
            raise ValueError("'b' должно быть числом!")

        if float(a) > float(b):
            raise ValueError("Недопустимые границы интервала!")

        epsilon = input("Введите epsilon (допустимую погрешность): ")
        try:
            float(epsilon)
        except ValueError:
            raise ValueError("Погрешность должна быть числом!")

        print("0 - консоль")
        print("1 - файл")
        mode_output = input("Выберите способ вывода данных: ")
        if not mode_output in ["0", "1"]:
            raise ValueError("Недействительный способ вывода")

        self.mode_output = int(mode_output)

        return float(a), float(b), float(epsilon)

    def from_file(self):
        file_ = open("input.txt").readline().split()
        if len(file_) != 4:
            raise ValueError("Недостаточно данных! Файл должен содержать a b epsilon mode_output!")

        try:
            float(file_[0])
        except ValueError:
            raise ValueError("'a' должно быть числом!")

        try:
            float(file_[1])
        except ValueError:
            raise ValueError("'b' должно быть числом!")

        try:
            float(file_[2])
        except ValueError:
            raise ValueError("Погрешность должна быть числом!")

        if not file_[3] in ["0", "1"]:
            raise ValueError("Недействительный способ вывода")
        self.mode_output = int(file_[3])

        return tuple(map(float, file_[:3]))

    def read(self):
        """Возвращает a, b, epsilon"""
        if self.mode == 0:
            return self.from_keyboard()
        else:
            return self.from_file()

    def write(self, root, error, iterations):
        if self.mode_output == 0:
            ViewService.to_console(root, error, iterations)
        else:
            ViewService.to_file(root, error, iterations)

    @staticmethod
    def to_console(root, error, iterations):
        print(f"Ответ: {root}, f({root})={round(error, 6)}, количество итераций: {iterations}")

    @staticmethod
    def to_file(root, error, iterations):
        file_ = open("output.txt", 'w')
        file_.write(f"Ответ: {root}, f({root})={round(error, 6)}, количество итераций: {iterations}")

        file_.close()
