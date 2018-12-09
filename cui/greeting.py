import inquirer
from cui import simplifiedNewton
from tools.MethodError import MethodError

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
EXIT = 'exit'


def init():
    questions = [
        inquirer.List('mode',
                      message="Choose mode of work?",
                      choices=[SIMPLIFIED_NEWTON, EXIT],
                      ),
    ]
    # while True:
    # try:
    #     answers = inquirer.prompt(questions)
    #     mode = answers.get('mode')
    #     if mode == SIMPLIFIED_NEWTON:
    simplifiedNewton.init()
#     if mode == EXIT:
#         return
# except MethodError as e:
#     print(e)
