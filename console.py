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
