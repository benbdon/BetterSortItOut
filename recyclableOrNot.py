#!/usr/bin/env python
# this program takes user input from a keyboard (y/n)


def main():
    lidCondition = "c"
    while (True):
        #Hold prev condition
        prevLidCondition = lidCondition

        #"Manual" open/close switch
        lidCondition = raw_input("Type o and c\n")

        #Check if the lid went from open to close
        if (prevLidCondition != lidCondition and lidCondition == "c"):

            #Take image
            print "Taking image"#Call Ahalya's take image function here
            isRecyclable = raw_input("Is this recyclable?\n")
            if (isRecyclable == 'y'):
                print("This is recyclable\n")
            elif (isRecyclable == 'n'):
                print("This is not recyclable\n")

if __name__ == '__main__':
    main()
