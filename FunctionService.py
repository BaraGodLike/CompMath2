import math


def f1(x):
    """f(x)=x^3-x-2"""
    return x ** 3 - x - 2


def f1_prime(x):
    return 3 * x ** 2 - 1


def f1_2(x):
    return 6 * x


def phi1(x):
    if x + 2 >= 0:
        return (x + 2) ** (1 / 3)
    else:
        return -((-x - 2) ** (1 / 3))


def phi1_prime(x):
    return 1 / (3 * abs(x + 2) ** (2 / 3))


def f2(x):
    """f(x) = cos(x) - x"""
    return math.cos(x) - x


def f2_prime(x):
    return -math.sin(x) - 1


def f2_2(x):
    return -math.cos(x)


def phi2(x):
    return math.cos(x)


def phi2_prime(x):
    return -math.sin(x)


def f3(x):
    """f(x) = exp(x) - 3*x"""
    return math.exp(x) - 3 * x


def f3_prime(x):
    return math.exp(x) - 3


def f3_2(x):
    return math.exp(x)


def phi3(x):
    return math.exp(x) / 3


def phi3_prime(x):
    return math.exp(x) / 3


def f4(x):
    """f(x) = 2x^3 - 1.89x^2 - 5x + 2.34"""
    return 2 * x ** 3 - 1.89 * x ** 2 - 5 * x + 2.34


def f4_prime(x):
    return 6 * x ** 2 - 3.78 * x - 5


def f4_2(x):
    return 12 * x - 3.78


def phi4(x):
    return (0.945 * x ** 2 + 2.5 * x - 1.17) ** (1 / 3)


def phi4_prime(x):
    numerator = (2 * 0.945 * x + 2.5)
    denominator = 3 * ((0.945 * x ** 2 + 2.5 * x - 1.17) ** (2 / 3))
    return numerator / denominator


equations = {
    1: {
        "description": "f(x) = x^3 - x - 2",
        "f": f1,
        "f_prime": f1_prime,
        "f2": f1_2,
        "phi": phi1,
        "phi_prime": phi1_prime
    },
    2: {
        "description": "f(x) = cos(x) - x",
        "f": f2,
        "f_prime": f2_prime,
        "f2": f2_2,
        "phi": phi2,
        "phi_prime": phi2_prime
    },
    3: {
        "description": "f(x) = exp(x) - 3*x",
        "f": f3,
        "f_prime": f3_prime,
        "f2": f3_2,
        "phi": phi3,
        "phi_prime": phi3_prime
    },
    4: {
        "description": "f(x) = 2x^3 - 1.89x^2 - 5x + 2.34",
        "f": f4,
        "f_prime": f4_prime,
        "f2": f4_2,
        "phi": phi4,
        "phi_prime": phi4_prime
    }
}
