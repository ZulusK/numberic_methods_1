import inquirer
from methods import lobachevskiy, simplifiedNewton, fixedPointIterations, dihotomy
import re
import tools

# inquirer.List('size',
#               message="What size do you need?",
#               choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
#               ),
# inquirer.Text('phone', message="What's your phone number",
#               validate=lambda _, x: re.match('\+?\d[\d ]+\d', x),
#               )
# inquirer.Checkbox('interests',
#                   message="What are you interested in?",
#                   choices=['Computers', 'Books', 'Science', 'Nature', 'Fantasy', 'History'],
#                   default=['Computers', 'Books']),
# inquirer.Path('log_file',
#                  message="Where logs should be located?",
#                  path_type=inquirer.Path.DIRECTORY,
#                 ),
SIMPLIFIED_NEWTON = 'simplified newton method'
DICHOTOMY = 'dichotomy method'
FIXED_POINT_ITERATIONS = 'fixed points iterations method'
EXIT = 'exit'
NUMBER_REGEXP = re.compile("^[-+]?\d*(\.\d+)?$")


def ask_function():
    questions = [
        inquirer.Text('function', message="Enter source function, f(x) = ", validate=lambda _, v: len(v) > 0),
        inquirer.Text('a', message="Enter the left-border", validate=lambda _, v: NUMBER_REGEXP.match(v)),
        inquirer.Text('b', message="Enter the right-border", validate=lambda _, v: NUMBER_REGEXP.match(v)),
    ]
    answers = None
    while True:
        answers = inquirer.prompt(questions)
        a = float(answers.get('a'))
        b = float(answers.get('b'))
        if a >= b:
            print('Caution! a==b, try again')
        else:
            answers['a'] = a
            answers['b'] = b
            break
    function = tools.sympify(answers.get('function').replace('^', '**'))
    print("You entered f(x) = %s" % function)
    return function, answers.get('a'), answers.get('b')


def init():
    print('x=%s' % lobachevskiy.process([12, 6, -15, -6, 1]))
    # questions = [
    #     inquirer.List('mode',
    #                   message="Choose method of computations:",
    #                   choices=[SIMPLIFIED_NEWTON, FIXED_POINT_ITERATIONS, DICHOTOMY, EXIT],
    #                   ),
    # ]
    # while True:
    #     try:
    #         answers = inquirer.prompt(questions)
    #         (function, a, b) = ask_function()
    #         x = None
    #         mode = answers.get('mode')
    #         if mode == SIMPLIFIED_NEWTON:
    #             x = simplifiedNewton.process(function, a, b)
    #         if mode == DICHOTOMY:
    #             x = dihotomy.process(function, a, b)
    #         if mode == FIXED_POINT_ITERATIONS:
    #             x = fixedPointIterations.process(function, a, b)
    #         if mode == EXIT:
    #             return
    #     except tools.MethodError as e:
    #         print('Caution! %s' % e)
    #         print('Answer x=%s', x)
# cos(x)^3+(x^3)*exp(x)-(x^6)-35
