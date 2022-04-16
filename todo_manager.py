"""
This is the main code of the application. The user will insert from the command-line interface the proper command
to use the provided functionalities.
"""
import sys
from modules import todo_processor
from modules import file_handler

file_handler.init_data_file()

match sys.argv[1]:
    case "a":
        todo_processor.add_todo(sys.argv[2])
    case "ls":
        print(todo_processor.list_desc())
    case "d":
        id_todo = int(input("Insert the id of the to do item\n"))
        todo_processor.delete_todo(id_todo)
    case "t":
        id_todo = int(input("Insert the id of the to do item\n"))
        todo_processor.change_state(id_todo)
    case "h":
        print("help")
    case "s":
        print("search")
    case "e":
        print("edit")
    case _:
        print("default")
