import FunctionService
import ViewService
from Methods.ChordMethod import ChordMethod
from Methods.NewtonMethod import NewtonMethod
from Methods.SimpleIterationMethod import SimpleIterationMethod

view = ViewService.ViewService()
eq_num, meth_num = view.start()
a, b, epsilon = view.read()
eq = FunctionService.equations[eq_num]

if meth_num == 1:
    root, value, iterations = ChordMethod(eq["f"], eq["f2"], a, b, epsilon).solve()
if meth_num == 2:
    root, value, iterations = NewtonMethod(eq["f"], eq["f_prime"], eq["f2"], a, b, epsilon).solve()
else:
    root, value, iterations = SimpleIterationMethod(eq["f"], eq["phi"], eq["phi_prime"], a, b, epsilon).solve()

view.write(root, value, iterations)
