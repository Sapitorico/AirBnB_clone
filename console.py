#!/usr/bin/python3
""" write as class Console manage (create, update, destroy, etc)
objects via a console / command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Your class definition must be: class HBNBCommand(cmd.Cmd):"""

    prompt = '(hbnb) '
    classes = ["BaseModel"]
    """ Mensajes de error: """
    error_class = {'missing_class': '** class name missing **',
                   'dont_exists_class': "** class doesn't exist **",
                   'missing_id': '** instance id missing **',
                   'dont_exists_id': '** no instance found **',
                   'missing_attribute': '** attribute name missing **',
                   'missing_value': '** value missing **'}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print(self.error_class["missing_class"])
        elif arg not in ["BaseModel"]:
            print(self.error_class["dont_exists_class"])
        else:
            _class = globals().get(arg)
            if not _class:
                print(self.error_class["dont_exists_class"])
            else:
                obj = _class()
                storage.new(obj)
                storage.save()
                print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        args = arg.split()
        if not args:
            print(self.error_class["missing_class"])
        elif len(args) < 2:
            if len(args) == 1:
                print(self.error_class["missing_id"])
            else:
                print(self.error_class["missing_attribute"])
        else:
            class_name = args[0]
            obj_id = args[1]
            if class_name not in self.classes:
                print(self.error_class["dont_exists_class"])
            else:
                objects = storage.all()
                obj_key = f"{class_name}.{obj_id}"
                if obj_key not in objects:
                    print(self.error_class["dont_exists_id"])
                else:
                    print(objects[obj_key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print(self.error_class["missing_class"])
        elif args[0] not in self.classes:
            print(self.error_class["dont_exists_class"])
        elif len(args) < 2:
            print(self.error_class["missing_id"])
        else:
            obj_id = args[1]
            objects = storage.all()
            for key, obj in objects.items():
                if obj_id == obj['id'] and args[0] == obj['__class__']:
                    del objects[key]
                    storage.save()
                    return
            print(self.error_class["dont_exists_id"])

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg and arg not in self.classes:
            print(self.error_class["dont_exists_class"])
        else:
            objects = storage.all()
            objs_list = [str(objs) for objs in objects.values()]
            print(objs_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print(self.error_class["missing_class"])
        elif args[0] not in self.classes:
            print(self.error_class["dont_exists_class"])
        elif len(args) < 2:
            print(self.error_class["missing_id"])
        elif len(args) < 3:
            print(self.error_class["missing_attribute"])
        elif len(args) < 4:
            print(self.error_class["missing_value"])
        else:
            class_name = args[0]
            obj_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]
            objects = storage.all()
            obj_key = f"{class_name}.{obj_id}"
            if obj_key not in objects:
                print(self.error_class["dont_exists_id"])
            else:
                obj = objects[obj_key]
                if attribute_name in ["id", "created_at", "updated_at"]:
                    return
                if hasattr(obj, attribute_name):
                    attribute_type = type(getattr(obj, attribute_name))
                    setattr(obj, attribute_name, attribute_type
                            (attribute_value))
                    obj.save()
                else:
                    return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
