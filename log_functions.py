#!/usr/bin/env python

import sys
import datetime

def log(arg):
    f = open("trash_log.txt","a")

    # log time and the string response
    # s = str(datetime.datetime.now()) + " : " + arg + '\n'
    s = arg + '\n'
    f.write(s)

    f.close()


def new_log():
    f = open("trash_log.txt","w")

    f.write('')
    f.close()
