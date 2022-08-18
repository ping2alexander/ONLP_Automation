import yaml
import sys
import getopt

num_of_dut = 0
Trunk = 0
num_of_trunk = 0
interface_index = 0

argList = sys.argv[1:]

option = "f:"
loption = ["filename"]
arg, val = getopt.getopt(argList, option, loption)

for a, v in arg:
    if a in ("-f", "--filename"):
        fname = v

newname = './../cfg/' + fname

with open(newname,"r") as r:
    data = yaml.safe_load(r)

#print(data)    
#print(type(data))

key = 'DUT1'

if 'DUT1' in data['Devices']:
    num_of_dut = 1
if 'DUT2' in data['Devices']:
    num_of_dut = 2

if 'Topology' in data:
    num_of_trunk  = len(data['Topology']['DUT1']['interfaces'])


#print("Number of DUTs: {}".format(num_of_dut))
#print("Number of Trunks: {}".format(num_of_trunk))

if num_of_dut == 2:
    print (" ", end='')
    for i in range(24):
        print ("-", end='')
    #print("")

    for i in range(49):
        print(" ", end='')
    #print("|", end='')

    print (" ", end='')
    for i in range(24):
        print ("-", end='')
    print("")

    for i in range(num_of_trunk * 2):
        print("|", end='')
        if i != int(num_of_trunk / 2):
            for p in range(24):
                print(" ", end='')
            print("|", end='') 
        elif i == int(num_of_trunk / 2):
            label_len = len('DUT1')
            remain_len = 24 - label_len
            l1 = remain_len / 2
            l2 = remain_len / 2
            for k in range(int(l1)):
                print(" ", end='')
            print('DUT1', end='')
            for l in range(int(l2)):
                print(" ", end='')
            print("|", end='')
         
        if i % 2 != 0:
            for j in range(48):
                print(" ", end='')
            print("|", end='')
        if i % 2 == 0:
            if interface_index < num_of_trunk:
                t1 = len('(' + data['Topology']['DUT1']['interfaces'][interface_index]['LocalPort'] + ')')
                t2 = len('(' + data['Topology']['DUT1']['interfaces'][interface_index]['RemotePort'] + ')')
                remaining_len = 48 - (t1 + t2)
                print('(' + data['Topology']['DUT1']['interfaces'][interface_index]['LocalPort'] + ')', end='')
                for j in range(remaining_len):
                    print("-", end='')
                print('(' + data['Topology']['DUT1']['interfaces'][interface_index]['RemotePort'] + ')', end='')
                interface_index = interface_index + 1
            print("|", end='')

        if i != int(num_of_trunk / 2):
            for i in range(24):
                print(" ", end='')
            print("|")
        elif i == int(num_of_trunk / 2):
            label_len = len('DUT2')
            remain_len = 24 - label_len
            l1 = remain_len / 2
            l2 = remain_len / 2
            for i in range(int(l1)):
                print(" ", end='')
            print('DUT2', end='')
            for i in range(int(l2)):
                print(" ", end='')
            print("|")

    print (" ", end='')
    for i in range(24):
        print ("-", end='')
    for i in range(49):
        print(" ", end='')
    #print("|", end='')

    print (" ", end='')
    for i in range(24):
        print ("-", end='')

    print("\n")

elif num_of_dut == 2:
    pass
