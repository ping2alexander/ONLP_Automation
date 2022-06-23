d1 = {'HardwareList': {'DUT1': {'Hardware_type': 'Questone', 'access': {'protocol': 'ssh', 'ip': '10.1.1.1', 'port': 22}, 'credentials': {'username': 'root', 'password': 'onl'}}, 'DUT2': {'Hardware_type': 'Questone', 'access': {'protocol': 'ssh', 'ip': '10.1.1.2', 'port': 22}, 'credentials': {'username': 'admin', 'password': 'onl'}}}, 'Connection': {'DUT1': {'interfaces': [{'LocalPort': 'Ethernet1', 'RemoteDevice': 'DUT2', 'RemotePort': 'Ethernet11'}, {'LocalPort': 'Ethernet2', 'RemoteDevice': 'DUT2', 'RemotePort': 'Ethernet12'}]}, 'DUT2': {'interfaces': [{'LocalPort': 'Ethernet11', 'RemoteDevice': 'DUT1', 'RemotePort': 'Ethernet1'}, {'LocalPort': 'Ethernet12', 'RemoteDevice': 'DUT1', 'RemotePort': 'Ethernet2'}]}}}

login = d1['HardwareList']
DUT1interfaceList = d1['Connection']['DUT1']['interfaces']
DUT2interfaceList = d1['Connection']['DUT2']['interfaces']

Trunk = dict()

Trunk[1] = dict()
Trunk[1][2] = dict()

Trunk[2] = dict()
Trunk[2][1] = dict()

i = 0
j = 1

while i < len(DUT1interfaceList):
    Trunk[1][2][j] = DUT1interfaceList[i]['LocalPort']
    i = i + 1
    j = j + 1


i = 0
j = 1

while i < len(DUT2interfaceList):
    Trunk[2][1][j] = DUT2interfaceList[i]['LocalPort']
    i = i + 1
    j = j + 1


print(Trunk[1][2][1])
print(Trunk[1][2][2])

print(Trunk[2][1][1])
print(Trunk[2][1][2])
