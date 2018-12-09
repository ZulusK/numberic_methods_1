from sympy import sympify, abc, diff


def eval_func_at_point(func, point):
    """
    Calculates value of function at specified point and returns it
    :param func: function for evaluation
    :param point: the x value
    :return: value e of function at specified point
    """
    if type(func) is str:
        func = str_to_func(func)
    return func.subs(abc.x, point).evalf()


def derivative(func, level=1):
    """
    Calculates derivative of a function and returns it sympy equivalent
    :param func: source function
    :param level: count of derivation
    :return: sympy equivalent of a function derivative
    """
    if level < 1:
        raise ValueError("Level must be greater than 1")
    if type(func) is str:
        func = str_to_func(func)
    return diff(func, abc.x, level)


def str_to_func(formula):
    return sympify(formula)
