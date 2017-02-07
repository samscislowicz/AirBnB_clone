#!/usr/bin/python3
"""
Console 0.0.1
"""
import cmd


class Console(cmd.Cmd):
    """ Command processor for AirBnB Console """

    prompt = '(hbnb) ';

    def do_EOF(self, line):
        """ exits console on EOF """
        return True
    def do_quit(self, line):
        """ exits console on quit """
        return True

if __name__ == '__main__':
    Console().cmdloop()
