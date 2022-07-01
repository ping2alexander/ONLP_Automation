import yaml
from ssh_login import Login
import enum


def Get_Fan_Value(IPAddress, FanIndex, key):
    DUT = Login(IPAddress, 'alexander', 'Dafne@140820')

    data = DUT.SendACommand('cat onlpdump_ery.yml')

    with open('test.yml','w') as w:
        w.write(data)
    with open('test.yml', 'r') as r:
        input1 = yaml.safe_load(r)

    Fan_Dict = input1["Fans"]
    
    FanIndex = FanIndex - 1

    if FanIndex <= len(Fan_Dict):
        print(Fan_Dict[FanIndex])
        return Fan_Dict[FanIndex][key]
    else:
        print("Index is not matching")
        return -1

def Get_PSU_Value(IPAddress, PSU, key):
    DUT = Login(IPAddress, 'alexander', 'Dafne@140820')

    data = DUT.SendACommand('cat onlpdump_ery.yml')

    with open('test.yml','w') as w:
        w.write(data)
    with open('test.yml', 'r') as r:
        input1 = yaml.safe_load(r)

    PSU_Dict = input1["PSUs"]
    PSUIndex = PSU - 1

    if PSUIndex <= len(PSU_Dict):
        print(PSU_Dict[PSUIndex])
        return PSU_Dict[PSUIndex][key]
    else:
        print("Index is not matching")
        return -1

def Get_PSU_FAN_Value(IPAddress, PSU, FAN, key):
    DUT = Login(IPAddress, 'alexander', 'Dafne@140820')

    data = DUT.SendACommand('cat onlpdump_ery.yml')

    with open('test.yml','w') as w:
        w.write(data)
    with open('test.yml', 'r') as r:
        input1 = yaml.safe_load(r)

    PSU_Dict = input1["PSUs"]
    PSUIndex = PSU - 1
    FANIndex = FAN - 1
    if PSUIndex <= len(PSU_Dict):
        if FANIndex <= len(PSU_Dict[PSUIndex]["Fans"]):
            if key in PSU_Dict[PSUIndex]["Fans"][FANIndex]:
                print(PSU_Dict[PSUIndex]["Fans"][FANIndex][key])
            else:
                print("Specified key is not present in the dictionary file")
    else:
        print("Index is not matching")
        return -1

def Get_PSU_Thermal_Value(IPAddress, PSU, Thermal, key):
    DUT = Login(IPAddress, 'alexander', 'Dafne@140820')

    data = DUT.SendACommand('cat onlpdump_ery.yml')

    with open('test.yml','w') as w:
        w.write(data)
    with open('test.yml', 'r') as r:
        input1 = yaml.safe_load(r)

    PSU_Dict = input1["PSUs"]
    PSUIndex = PSU - 1
    ThermalIndex = Thermal- 1
    if PSUIndex <= len(PSU_Dict):
        if ThermalIndex <= len(PSU_Dict[PSUIndex]["Fans"]):
            if key in PSU_Dict[PSUIndex]["Thermals"][ThermalIndex]:
                print(PSU_Dict[PSUIndex]["Thermals"][ThermalIndex][key])
            else:
                print("Specified key is not present in the dictionary file")
    else:
        print("Index is not matching")
        return -1




res = Get_PSU_Thermal_Value('192.168.1.6', 1, 2, 'Temperature')


