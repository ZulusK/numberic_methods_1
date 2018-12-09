import tools
from sympy import abc


def extended_end_condition(curr_x, prev_x, q, eps):
    return abs(curr_x - prev_x) <= eps


def simple_end_condition(curr_x, prev_x, q, eps):
    return abs(curr_x - prev_x) <= (eps * (1 - q)) / q


def process(func, a, b, eps=1e-10):
    fd = tools.derivative(func)
    sd = tools.derivative(fd)
    print("f(x)'=%s" % fd)
    print("f(x)''=%s" % sd)
    va = tools.eval_func_at_point(func, a)
    vb = tools.eval_func_at_point(func, b)
    print("f(%s)=%s, f(%s)=%s" % (a, va, b, vb))
    maxFinder = tools.MaxFinder()
    minFinder = tools.MinFinder()
    tools.apply(tools.gen_function_values_list(fd, a, b), [maxFinder.visit, minFinder.visit])
    A = maxFinder.max
    B = minFinder.min
    L = 2 / (A + B) * (-1 if va > 0 else 1)
    Q = (A - B) / (A + B)
    Q = 1 if Q > 1 else Q
    phi = abc.x - L * func
    prev_x = a if va * tools.eval_func_at_point(sd, a) > 0 else b
    i = 1
    is_end_condition_happen = simple_end_condition if Q <= 0.5 else extended_end_condition
    print("X0=%s" % prev_x)
    while True:
        curr_x = tools.eval_func_at_point(phi, prev_x)
        print("<%s> X%s=%s" % (i + 1, i, curr_x))
        if is_end_condition_happen(curr_x, prev_x, Q, eps):
            return curr_x
        prev_x = curr_x
        i += 1
