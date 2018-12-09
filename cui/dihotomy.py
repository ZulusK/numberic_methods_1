import inquirer
import tools
from sympy import abc


def end_condition(l, r, eps):
    return abs(l - r) <= eps


def process(func, a, b, eps=1e-10):
    va = tools.eval_func_at_point(func, a)
    vb = tools.eval_func_at_point(func, b)
    print("f(%s)=%s, f(%s)=%s" % (a, va, b, vb))
    left = a
    right = b
    value_at_left = va
    # value_at_right = vb
    i = 1
    prev_x = (a + b) / 2
    print("X0=%s" % prev_x)
    while True:
        curr_x = (left + right) / 2
        print("<%s> X%s=%s" % (i + 1, i, curr_x))
        if end_condition(left, right, eps):
            return curr_x
        value_at_x = tools.eval_func_at_point(func, curr_x)
        if value_at_left * value_at_x < 0:
            # value_at_right = value_at_x
            left, right = left, curr_x
        else:
            value_at_left = value_at_x
            left, right = curr_x, right
        i += 1


def init():
    # questions = [
    #     inquirer.Text('function', message="Enter source function, f(x) = "),
    #     inquirer.Text('a', message="Enter the left-border"),
    #     inquirer.Text('b', message="Enter the right-border"),
    # ]
    # answers = inquirer.prompt(questions)
    answers = {'function': 'cos(x)^3+(x^3)*exp(x)-(x^6)-35', 'a': 4, 'b': 6}
    function = tools.sympify(answers.get('function').replace('^', '**'))
    print("You entered f(x) = %s" % function)
    process(function, answers.get('a'), answers.get('b'))
# print(tools.eval_func_at_point(answers.get('function'), 4))
