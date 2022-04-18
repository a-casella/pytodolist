"""
This is the main code of the application. The user will insert from the command-line interface the proper command
to use the provided functionalities.
"""
import sys
import i18n
import configparser
from modules import todo_processor
from modules import input_validator
from modules import file_handler

config = configparser.ConfigParser()
config.read("config.ini")
file_handler.init_data_file()
i18n.load_path.append(config["DEFAULT"]["i18nPath"])
i18n.set("locale", config["DEFAULT"]["i18nLocale"])
i18n.set("fallback", config["DEFAULT"]["i18nFallback"])
i18n.set("file_format", config["DEFAULT"]["i18nFileFormat"])

match sys.argv[1]:
    case "a":
        title = sys.argv[2]
        if input_validator.validate_title_length(title):
            todo_processor.add_todo(title)
        else:
            print(i18n.t("validator.wrongTitleLength"))
    case "ls":
        print(todo_processor.list_desc())
    case "d":
        todo_processor.delete_todo(int(sys.argv[2]))
    case "t":
        todo_processor.change_state(int(sys.argv[2]))
    case "h":
        print(i18n.t("ui.help"))
    case "s":
        print(todo_processor.search_todo(sys.argv[2]))
    case "e":
        title = sys.argv[3]
        if input_validator.validate_title_length(title):
            todo_processor.edit_todo(int(sys.argv[2]), title)
        else:
            print(i18n.t("validator.wrongTitleLength"))
    case _:
        print(i18n.t("ui.commandNotFound"))
