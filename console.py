#!/usr/bin/python3
""" write as class Console manage (create, update, destroy, etc) objects via a console / command interpreter
"""
import cmd
import models
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
        self.prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        return True

    """ commands:
        create:
            create a new instances of BaseModel and save data base and print the id
            If the class name is missing, print ** class name missing ** (ex: $ create)
            If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
        show: Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
            If the class name is missing, print ** class name missing ** (ex: $ show)
            If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
            If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
            If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)
    """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
