"""
This is the main code of the application. The user will insert from the command-line interface the proper command
to use the provided functionalities.
"""
import sys
from modules import todo_processor
from modules import file_handler
import i18n

file_handler.init_data_file()
i18n.load_path.append("translations")
i18n.set("locale", "it")
i18n.set("fallback", "en")
i18n.set("file_format", "json")

match sys.argv[1]:
    case "a":
        todo_processor.add_todo(sys.argv[2])
    case "ls":
        print(todo_processor.list_desc())
    case "d":
        todo_processor.delete_todo(int(sys.argv[2]))
    case "t":
        todo_processor.change_state(int(sys.argv[2]))
    case "h":
        print(i18n.t("help.text"))
    case "s":
        print(todo_processor.search_todo(sys.argv[2]))
    case "e":
        todo_processor.edit_todo(int(sys.argv[2]), sys.argv[3])
    case _:
        print("default")
