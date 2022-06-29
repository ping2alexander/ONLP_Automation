import os
import getopt, sys

HOSTIP = ''
Device = ''
argumentList = sys.argv[1:]

Option = "I:d:"
LongOption = ["IPAddress", "DUT"]

try:
    argument, value = getopt.getopt(argumentList, Option , LongOption)

    for arg, val in argument:
        if arg in ("-I","--IPAddress"):
            HOSTIP = val
        if arg in ("-d","--DUT"):
            Device = val
except getopt.error as err:
    print(str(err))

command = "ping -c 5 " + HOSTIP

HOST_Status = os.system(command)

if HOST_Status is 0:
    print("{} - Device is reachable".format(Device))
else:
    print("{} - Device is NOT reachable".format(Device))


