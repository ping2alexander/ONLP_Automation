import yaml
from ssh_login import Login


def Get_Fan_Value(IPAddress, FanIndex, key):
    DUT = Login(IPAddress, 'root', 'onl')

    data = DUT.SendACommand('onlpdump -ery')

    with open('test.yml','w') as w:
        w.write(data)
    with open('test.yml', 'r') as r:
        input1 = yaml.safe_load(r)

    Fan_Dict = input1["Fans"]
    
    FanIndex = FanIndex - 1

    if FanIndex <= len(Fan_Dict):
        if key in Fan_Dict[FanIndex]:
            return Fan_Dict[FanIndex][key]
        else:
            print("Specified key is not present in the dictionary file")
    else:
        print("Index is not matching")
        return -1

def Get_PSU_Value(IPAddress, PSU, key):
    DUT = Login(IPAddress, 'root', 'onl')

    data = DUT.SendACommand('onlpdump -ery')

    with open('test.yml','w') as w:
        w.write(data)
    with open('test.yml', 'r') as r:
        input1 = yaml.safe_load(r)

    PSU_Dict = input1["PSUs"]
    PSUIndex = PSU - 1

    if PSUIndex <= len(PSU_Dict):
        if key in PSU_Dict[PSUIndex]:
            return PSU_Dict[PSUIndex][key]
        else:
            print("Specified key is not present in the dictionary file")
    else:
        print("Index is not matching")
        return -1

def Get_PSU_FAN_Value(IPAddress, PSU, FAN, key):
    DUT = Login(IPAddress, 'root', 'onl')

    data = DUT.SendACommand('onlpdump -ery')

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
    DUT = Login(IPAddress, 'root', 'onl')

    data = DUT.SendACommand('onlpdump -ery')

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


def Get_Thermal_Value(IPAddress, Thermal, key):
    DUT = Login(IPAddress, 'root', 'onl')

    data = DUT.SendACommand('onlpdump -ery')

    with open('test.yml','w') as w:
        w.write(data)
    with open('test.yml', 'r') as r:
        input1 = yaml.safe_load(r)

    Thermal_Dict = input1["Thermals"]

    ThermalIndex = Thermal - 1

    if ThermalIndex <= len(Thermal_Dict):
        if key in Thermal_Dict[ThermalIndex]:
            return Thermal_Dict[ThermalIndex][key]
        else:
            print("Specified key is not present in the dictionary file")
    else:
        print("Index is not matching")
        return -1


def Get_LED_Value(IPAddress, LED, key):
    DUT = Login(IPAddress, 'root', 'onl')

    data = DUT.SendACommand('onlpdump -ery')

    with open('test.yml','w') as w:
        w.write(data)
    with open('test.yml', 'r') as r:
        input1 = yaml.safe_load(r)

    LED_Dict = input1["LEDs"]

    LEDIndex = LED - 1

    if LEDIndex <= len(LED_Dict):
        if key in LED_Dict[LEDIndex]:
            return LED_Dict[LEDIndex][key]
        else:
            print("Specified key is not present in the dictionary file")
    else:
        print("Index is not matching")
        return -1

