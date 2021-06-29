
# pynput package requires X window
# keyboard package requires root on linux (but not windows)
# curses seems reasonable, but no anaconda package
# ncurses (new curses) seems like a possibility
# termios possible?

import curses
import os

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

targetString = "Type this"
print(targetString)

numTyped = 0



#for i in range(len(targetString)):
#    thisChar = targetString[i]
#    val = input("Type now")
#    print(colored(255, 0, 0, val))
