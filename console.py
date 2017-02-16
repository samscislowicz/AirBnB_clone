#!/usr/bin/python3
"""
Console 0.0.1
"""
import cmd
import json
from models import *
import re


class HBNBCommand(cmd.Cmd):
    """ Command processor for AirBnB Console """

    prompt = '(hbnb) '
    classes = ["BaseModel", "User", "State", "Amenity",
               "Review", "Place", "City"]

    def do_EOF(self, line):
        """exits console on EOF """
        return True

    def do_quit(self, line):
        """Quit command to exit the program """
        return True

    def emptyline(self):
        """ Returns an Empty Line """
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel, save it (to JSON), prints id"""
        args = line.split(' ')
        if len(args) < 1:
            print("** class name missing **")
        else:
            if args[0] in HBNBCommand.classes:
                if args[0] == "BaseModel":
                    new_model = BaseModel()
                if args[0] == "User":
                    new_model = User()
                if args[0] == "State":
                    new_model = State()
                if args[0] == "Amenity":
                    new_model = Amenity()
                if args[0] == "Review":
                    new_model = Review()
                if args[0] == "Place":
                    new_model = Place()
                if args[0] == "City":
                    new_model = City()
                new_model.save()
                print(new_model.id)

    def do_show(self, line):
        """ Prints the string representation of an instance based on
            class name and id """
        args = line.split(' ')
        if len(args) < 2:
            if len(args[0]) != 36:
                print("** instance id missing **")
            else:
                print("** class name missing **")
        else:
            if args[0] in HBNBCommand.classes:
                storage.reload()
                my_dict = storage.all()
                if args[1] not in my_dict:
                    print("** no instance found **")
                else:
                    for key in my_dict:
                        if args[0] in str(my_dict[key]):
                            if args[1] in my_dict.keys():
                                print(my_dict[args[1]])
                                break
                            else:
                                print("** no instance found **")
                                break
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """ Deletes an instance based on class name and id """
        args = line.split(' ')
        if len(args) < 2:
            print("** class name missing **")
        else:
            if args[0] in HBNBCommand.classes:
                storage.reload()
                my_dict = storage.all()
                if args[1] in my_dict.keys():
                    if (str(args[0]) in str(my_dict[args[1]])):
                        del my_dict[args[1]]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """ Prints all string representation of all instances
            based or not on the class name """
        args = line.split(' ')
        if (len(args) > 0 and args[0] != '') or len(args) > 1:
            if len(args) == 2:
                args[0], args[1] = args[1], args[0]
            if args[0] in HBNBCommand.classes or \
               args[1] in HBNBCommand.classes:
                storage.reload()
                my_dict = storage.all()
                for key in my_dict.keys():
                    if args[0] in str(my_dict[key]):
                        print(my_dict[key])
            else:
                print("** class doesn't exist **")
        else:
            storage.reload()
            my_dict = storage.all()
            for key in my_dict.keys():
                print(my_dict[key])

    def do_update(self, line):
        """ Updates an instance based on class name and id by adding
            or updating the change into JSON file"""
        args = line.split(' ')
        if len(args) < 4:
            if len(args) == 0:
                print("** class name missing **")
            if len(args) == 1:
                print("** instance id missing **")
            if len(args) == 2:
                print("** value missing **")
            if len(args) == 3:
                print("** value missing **")
            return
        else:
            class_name = args[0]
            inst_id = args[1]
            attr_name = args[2]
            if type(args[3]) is int or type(args[3]) is float:
                attr_valu = args[3]
            else:
                attr_val = args[3].replace('\"', '')
            storage.reload()
            my_dict = storage.all()
            if class_name in HBNBCommand.classes:
                if inst_id in my_dict:
                    my_obj = my_dict[inst_id]
                    setattr(my_obj, attr_name, attr_val)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_count(self, line):
        """ Counts the number of instances of a class """
        args = line.split(' ')
        count = 0
        if len(args) > 1:
            if args[1] in HBNBCommand.classes:
                storage.reload()
                my_dict = storage.all()
                for key in my_dict.keys():
                    if args[1] in str(my_dict[key]):
                        count += 1
        else:
            storage.reload()
            my_dict = storage.all()
            for key in my_dict.keys():
                count += 1
        print(count)

    # Class Methods
    def do_User(self, line):
        """ Performs commands on the User class"""
        line = line.replace('()', '')
        args = line.split('.')
        cmd_str = " User"
        if line == ".all":
            self.do_all(cmd_str)
        if line == ".count":
            self.do_count(cmd_str)
        if "show" in line:
            id_str = re.sub('.show\("', '', line)
            id_str = re.sub('"\)', '', id_str)
            self.do_show("User " + id_str)
        if "destroy" in line:
            id_str = re.sub('.destroy\("', '', line)
            id_str = re.sub('"\)', '', id_str)
            self.do_destroy("User " + id_str)
        if "update" in line:
            id_str = re.sub('.update\("', '', line)
            id_str = re.sub('\)', '', id_str)
            id_str = re.sub('"', '', id_str)
            id_str = re.sub(' ', '', id_str)
            id_str = id_str.split(",")
            id = id_str[0]
            arg_name = id_str[1]
            arg_variable = id_str[2]
            self.do_update("User " + id + " " + arg_name + " " + arg_variable)

    def do_BaseModel(self, line):
        """ Performs commands on the BaseModel class """
        line = line.replace('()', '')
        args = line.split('.')
        cmd_str = " BaseModel"
        if line == ".all":
            self.do_all(cmd_str)
        if line == ".count":
            self.do_count(cmd_str)
        if "show" in line:
            id_str = re.sub('.show\("', '', line)
            id_str = re.sub('"\)', '', id_str)
            self.do_show("BaseModel " + id_str)
        if "destroy" in line:
            id_str = re.sub('.destroy\("', '', line)
            id_str = re.sub('"\)', '', id_str)
            self.do_destroy("BaseModel " + id_str)
        if "update" in line:
            id_str = re.sub('.update\("', '', line)
            id_str = re.sub('\)', '', id_str)
            id_str = re.sub('"', '', id_str)
            id_str = re.sub(' ', '', id_str)
            id_str = id_str.split(",")
            id = id_str[0]
            arg_name = id_str[1]
            arg_variable = id_str[2]
            self.do_update("BaseModel " + id + " " +
                           arg_name + " " + arg_variable)

    def do_State(self, line):
        """ Performs comands on the State class """
        line = line.replace('()', '')
        args = line.split('.')
        cmd_str = " State"
        if line == ".all":
            self.do_all(cmd_str)
        if line == ".count":
            self.do_count(cmd_str)
        if "show" in line:
            id_str = re.sub('.show\("', '', line)
            id_str = re.sub('"\)', '', id_str)
            self.do_show("State " + id_str)
        if "destroy" in line:
            id_str = re.sub('.destroy\("', '', line)
            id_str = re.sub('"\)', '', id_str)
            self.do_destroy("State " + id_str)
        if "update" in line:
            id_str = re.sub('.update\("', '', line)
            id_str = re.sub('\)', '', id_str)
            id_str = re.sub('"', '', id_str)
            id_str = re.sub(' ', '', id_str)
            id_str = id_str.split(",")
            id = id_str[0]
            arg_name = id_str[1]
            arg_variable = id_str[2]
            self.do_update("State " + id + " " + arg_name + " " + arg_variable)

    def do_Amenity(self, line):
        """ Performs commands on the Amenity class """
        line = line.replace('()', '')
        args = line.split('.')
        cmd_str = " Amenity"
        if line == ".all":
            self.do_all(cmd_str)
        if line == ".count":
            self.do_count(cmd_str)
        if "show" in line:
            id_str = re.sub('.show\("', '', line)
            id_str = re.sub('"\)', '', id_str)
            self.do_show("Amenity " + id_str)
        if "destroy" in line:
            id_str = re.sub('.destroy\("', '', line)
            id_str = re.sub('"\)', '', id_str)
            self.do_destroy("Amenity " + id_str)
        if "update" in line:
            id_str = re.sub('.update\("', '', line)
            id_str = re.sub('\)', '', id_str)
            id_str = re.sub('"', '', id_str)
            id_str = re.sub(' ', '', id_str)
            id_str = id_str.split(",")
            id = id_str[0]
            arg_name = id_str[1]
            arg_variable = id_str[2]
            self.do_update("Amenity " + id + " " +
                           arg_name + " " + arg_variable)

    def do_Review(self, line):
        """ Performs commands on the Review class """
        line = line.replace('()', '')
        args = line.split('.')
        cmd_str = " Review"
        if line == ".all":
            self.do_all(cmd_str)
        if line == ".count":
            self.do_count(cmd_str)
        if "show" in line:
            id_str = re.sub('.show\("', '', line)
            id_str = re.sub('"\)', '', id_str)
            self.do_show("Review " + id_str)
        if "destroy" in line:
            id_str = re.sub('.destroy\("', '', line)
            id_str = re.sub('"\)', '', id_str)
            self.do_destroy("Review " + id_str)
        if "update" in line:
            id_str = re.sub('.update\("', '', line)
            id_str = re.sub('\)', '', id_str)
            id_str = re.sub('"', '', id_str)
            id_str = re.sub(' ', '', id_str)
            id_str = id_str.split(",")
            id = id_str[0]
            arg_name = id_str[1]
            arg_variable = id_str[2]
            self.do_update("Review " + id + " " +
                           arg_name + " " + arg_variable)

    def do_City(self, line):
        """ Performs commands on the City Class """
        line = line.replace('()', '')
        args = line.split('.')
        cmd_str = " City"
        if line == ".all":
            self.do_all(cmd_str)
        if line == ".count":
            sel.do_count(cmd_str)
        if "show" in line:
            id_str = re.sub('.show\("', '', line)
            id_str = re.sub('"\)', '', id_str)
            self.do_show("City " + id_str)
        if "destroy" in line:
            id_str = re.sub('.destroy\("', '', line)
            id_str = re.sub('"\)', '', id_str)
            self.do_destroy("City " + id_str)
        if "update" in line:
            id_str = re.sub('.update\("', '', line)
            id_str = re.sub('\)', '', id_str)
            id_str = re.sub('"', '', id_str)
            id_str = re.sub(' ', '', id_str)
            id_str = id_str.split(",")
            id = id_str[0]
            arg_name = id_str[1]
            arg_variable = id_str[2]
            self.do_update("City " + id + " " + arg_name + " " + arg_variable)

    def do_Place(self, line):
        """ Performs commands on the Place Class """
        line = line.replace('()', '')
        args = line.split('.')
        cmd_str = " Place"
        if line == ".all":
            self.do_all(cmd_str)
        if line == ".count":
            self.do_count(cmd_str)
        if "show" in line:
            id_str = re.sub('.show\("', '', line)
            id_str = re.sub('"\)', '', id_str)
            self.do_show("Place " + id_str)
        if "destroy" in line:
            id_str = re.sub('.destroy\("', '', line)
            id_str = re.sub('"\)', '', id_str)
            self.do_destroy("Place " + id_str)
        if "update" in line:
            id_str = re.sub('.update\("', '', line)
            id_str = re.sub('\)', '', id_str)
            id_str = re.sub('"', '', id_str)
            id_str = re.sub(' ', '', id_str)
            id_str = id_str.split(",")
            id = id_str[0]
            arg_name = id_str[1]
            arg_variable = id_str[2]
            self.do_update("Place " + id + " " + arg_name + " " + arg_variable)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
