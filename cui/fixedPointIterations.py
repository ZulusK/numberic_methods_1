import inquirer
from tools import analyzer
from tools.MethodError import MethodError


def process(func, a, b, eps=1e-10):
    fd = analyzer.derivative(func)
    sd = analyzer.derivative(fd)
    print("f(x)'=%s" % fd)
    print("f(x)''=%s" % sd)
    va = analyzer.eval_func_at_point(func, a)
    vb = analyzer.eval_func_at_point(func, b)
    print("f(%s)=%s, f(%s)=%s" % (a, va, b, vb))
    if abs(va) < eps:
        return a
    if abs(vb) < eps:
        return b
    if va * vb > 0:
        raise MethodError("f(%s)*f(%s)>0" % (a, b))
    prev_x = a if va * analyzer.eval_func_at_point(sd, a) > 0 else b
    divider = analyzer.eval_func_at_point(fd, prev_x)
    i = 1
    print("X0=%s" % prev_x)
    while True:
        curr_x = prev_x - analyzer.eval_func_at_point(func, prev_x) / divider
        print("<%s> X%s=%s" % (i + 1, i, curr_x))
        if abs(prev_x - curr_x) < eps:
            return curr_x
        prev_x = curr_x
        i += 1


def init():
    # questions = [
    #     inquirer.Text('function', message="Enter source function, f(x) = "),
    #     inquirer.Text('a', message="Enter the left-border"),
    #     inquirer.Text('b', message="Enter the right-border"),
    # ]
    # answers = inquirer.prompt(questions)
    answers = {'function': 'cos(x)^3+(x^3)*exp(x)-(x^6)-35', 'a': 4, 'b': 6}
    function = analyzer.sympify(answers.get('function').replace('^', '**'))
    print(analyzer.eval_func_at_point(function, 4.54803012545095))
    print("You entered f(x) = %s" % function)
    process(function, answers.get('a'), answers.get('b'))
# print(tools.eval_func_at_point(answers.get('function'), 4))
