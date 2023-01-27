FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list
    of to-do items.
    """
    with open(filepath, 'r') as file1:
        todolist = file1.readlines()
    return todolist


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in
    the text file. """
    with open(filepath, 'w') as file2:
        file2.writelines(todos_arg)
