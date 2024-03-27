import os

# Script is in the top-level of project
script_dir = os.path.dirname(__file__)  # Get the directory of script
os.chdir(script_dir)

FILEPATH = r'todos.txt'
todos_log = r'todos_log.txt'

def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns the list of to-do items,
        ensuring each item is on a separate line.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local  # Already a list of lines


def write_todos(todos_arg, filepath=FILEPATH):
    """Writes the to-do item list in the text file,
       each item on a separate line.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)  # writelines takes care of newlines


def read_completed_log(log=todos_log):
    with open(log, 'r') as file_log:
        completed_todos = file_log.readlines()
        print("Completed todos: ", completed_todos)
        return completed_todos


# print(__name__)
if __name__ in "__main__":
    print("Hello")
    print(get_todos())
