import inquirer
from methods import dihotomy
from methods import fixedPointIterations
from methods import simplifiedNewton
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


def ask_function():
    questions = [
        inquirer.Text('function', message="Enter source function, f(x) = "),
        inquirer.Text('a', message="Enter the left-border"),
        inquirer.Text('b', message="Enter the right-border"),
    ]
    answers = inquirer.prompt(questions)
    # answers = {'function': 'cos(x)^3+(x^3)*exp(x)-(x^6)-35', 'a': 4, 'b': 6}
    function = tools.sympify(answers.get('function').replace('^', '**'))
    print("You entered f(x) = %s" % function)
    return answers.get('function'), answers.get('a'), answers.get('b')


def init():
    questions = [
        inquirer.List('mode',
                      message="Choose method of computations:",
                      choices=[SIMPLIFIED_NEWTON, FIXED_POINT_ITERATIONS, DICHOTOMY, EXIT],
                      ),
    ]
    while True:
        try:
            answers = inquirer.prompt(questions)
            (function, a, b) = ask_function()
            mode = answers.get('mode')
            if mode == SIMPLIFIED_NEWTON:
                simplifiedNewton.process(function, a, b)
            if mode == DICHOTOMY:
                dihotomy.process(function, a, b)
            if mode == FIXED_POINT_ITERATIONS:
                fixedPointIterations.process(function, a, b)
            if mode == EXIT:
                return
        except tools.MethodError as e:
            print(e)
