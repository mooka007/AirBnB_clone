#!/usr/bin/python3
"""Console that contains the entry point of the comm interpreter"""

import cmd
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Bla Bla """
    promt = "(hbnb)"
    classes = ["BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"]
    attributes = ["updated_at", "created_at", "id"]
    specs = ["\'", "\""]

    def do_EOF(self, line):
        """ Exits """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True
    
    def emptyline(self):
        """an empty line + ENTER shouldnt execute anything\n"""
        pass
    def do_create(self, line):
        """ bla bla """
        if not line:
            print("** Class name missing **")
        elif line not in self.classes:
            print("** Class doesn't exist **")
        else:
            new_item = eval(line)()
            print(new_item.id)
            new_item.save()
    def do_clear(self, arg):
        """ clear """
        storage.all().clear()
        self.do_all(arg)
        print("** The data has been made clear **")

    def do_show(self, arg):
        """ Prints the string representation of an instance """
        if self.valid(arg, True):
            args = arg.split()
            __key = args[0] + "." + args[1]
            print(storage.all()[__key])

    def do_destroy(self, line):
        # gra instead of in
        """ method to delete an instance """
        if self.valid(line, True):
            args = line.split()
            __key = args[0] + "." + args[1]
            del storage.all()[__Key]
            storage.save()

    def do_all(self, arg):
        """ prints all instance  """
        args = arg.split()
        _len = len(args)
        my_list = []
        if _len >= 1:
            if args[0] not in HBNBCommand.all_class:
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if args[0] in key:
                    my_list.append(str(value))
        else:
            for key, value in storage.all().items():
                my_list.append(str(value))
        print(my_list)
    def do_update(self, line):
        """ Updates an instance based on the class name and id  """
        comm = line.split()
        if not line:
            print("** class name missing **")
        elif comm[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(comm) == 1:
            print("** instance id missing **")
            return
        elif comm[0] + "." + comm[1] not in storage.all().keys():
            print("** no instance found **")
            return
        elif len(comm) == 2:
            print("** attribute name missing **")
            return
        elif len(comm) == 3:
            print("** value missing **")
            return
        else:
            object = storage.all()
            key = comm[0] + "." + comm[1]
            if key in object:
                if comm[2] not in self.attributes:
                    if comm[3][0] in self.specs and comm[3][-1] in self.specs:
                        setattr(object[key], comm[2], str(comm[3][1: -1]))
                    else:
                        setattr(object[key], comm[2], str(comm[3]))
                    storage.save()
            else:
                print("** no instance found **")
                return


if __name__ == '__main__':
        HBNBCommand().cmdloop()
