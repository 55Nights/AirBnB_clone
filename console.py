#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self):
        """Default behavior for cmd module when input is invalid"""
        
        

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
