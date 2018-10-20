#!/usr/bin/env python

import sys
import datetime










def main():

    f = open("trash_log.txt", "w")


    while(1):

        response = raw_input("Was that trash? \n(y/n/x)")

        case(response)

        f.write("string")







    # Handle Shutdown




def log(arg):
    f = open("trash_log.txt","a")

    # log time and the string response
    s = str(datetime.datetime.now()) + " : " + arg + '\n'
    f.write(s)

    f.close()







if __name__ == '__main__':
    main()
