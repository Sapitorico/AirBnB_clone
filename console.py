#!/usr/bin/python3
""" write as class Console manage (create, update, destroy, etc) objects via a console / command interpreter
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Your class definition must be: class HBNBCommand(cmd.Cmd):
    Your command interpreter should implement:
    quit and EOF to exit the program
    help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
    a custom prompt: (hbnb)
    an empty line + ENTER shouldn’t execute anything
    """
    def __init__(self):
        super().__init__()
        self.prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
