import yaml
from ssh_login import Login


def Get_Fan_Value(IPAddress, FanIndex, key):
    DUT = Login(IPAddress, 'root', 'onl')

    data = DUT.SendACommand('/lib/platform-config/current/onl/bin/onlpdump -ery')

    with open('test.yml','w') as w:
        w.write(data)
    with open('test.yml', 'r') as r:
        input1 = yaml.safe_load(r)

    Fan_Dict = input1["Fans"]
    Index = FanIndex
    FanIndex = FanIndex - 1

    if FanIndex <= len(Fan_Dict):
        if key in Fan_Dict[FanIndex]:
            print("Fan-{} {} : {}".format(Index, key, Fan_Dict[FanIndex][key]))
            return 1
        else:
            #print("Specified key is not present in the dictionary file")
            return 0
    else:
        #print("Index is not matching")
        return -1

def Get_PSU_Value(IPAddress, PSU, key):
    DUT = Login(IPAddress, 'root', 'onl')

    data = DUT.SendACommand('/lib/platform-config/current/onl/bin/onlpdump -ery')

    with open('test.yml','w') as w:
        w.write(data)
    with open('test.yml', 'r') as r:
        input1 = yaml.safe_load(r)

    PSU_Dict = input1["PSUs"]
    PSUIndex = PSU - 1

    if PSUIndex <= len(PSU_Dict):
        if key in PSU_Dict[PSUIndex]:
            print("PSU-{} {}: {}".format(PSU, key, PSU_Dict[PSUIndex][key]))
            return 1
        else:
            #print("Specified key is not present in the dictionary file")
            return 0
    else:
        #print("Index is not matching")
        return -1

def Get_PSU_FAN_Value(IPAddress, PSU, FAN, key):
    DUT = Login(IPAddress, 'root', 'onl')

    data = DUT.SendACommand('/lib/platform-config/current/onl/bin/onlpdump -ery')

    with open('test.yml','w') as w:
        w.write(data)
    with open('test.yml', 'r') as r:
        input1 = yaml.safe_load(r)

    PSU_Dict = input1["PSUs"]

    PSUIndex = PSU - 1
    FANIndex = FAN - 1

    if PSU_Dict[PSUIndex]["Fans"] != None:
        if PSUIndex <= len(PSU_Dict):
            if FANIndex <= len(PSU_Dict[PSUIndex]["Fans"]):
                if key in PSU_Dict[PSUIndex]["Fans"][FANIndex]:
                    print("PSU-{} Fan-{} {}: {}".format(PSU, FAN, key, PSU_Dict[PSUIndex]["Fans"][FANIndex][key]))
                    return 1
                else:
                    #print("Specified key is not present in the dictionary file")
                    return 0
        else:
            #print("Index is not matching")
            return -1
    else:
        #print("No Fan modules found in the PSU")
        return -2

def Get_PSU_Thermal_Value(IPAddress, PSU, Thermal, key):
    DUT = Login(IPAddress, 'root', 'onl')

    data = DUT.SendACommand('/lib/platform-config/current/onl/bin/onlpdump -ery')

    with open('test.yml','w') as w:
        w.write(data)
    with open('test.yml', 'r') as r:
        input1 = yaml.safe_load(r)

    PSU_Dict = input1["PSUs"]
    PSUIndex = PSU - 1
    ThermalIndex = Thermal- 1

    if PSU_Dict[PSUIndex]["Thermals"] != None:
        if PSUIndex <= len(PSU_Dict):
            if ThermalIndex <= len(PSU_Dict[PSUIndex]["Fans"]):
                if key in PSU_Dict[PSUIndex]["Thermals"][ThermalIndex]:
                    print("PSU-{} Thermal-{} {}: {}".format(PSU, Thermal, key, PSU_Dict[PSUIndex]["Thermals"][ThermalIndex][key]))
                    return 1
                else:
                    #print("Specified key is not present in the dictionary file")
                    return 0
        else:
            #print("Index is not matching")
            return -1
    else:
        #print("No thermal modules found in the PSU")
        return -2

def Get_Thermal_Value(IPAddress, Thermal, key):
    DUT = Login(IPAddress, 'root', 'onl')

    data = DUT.SendACommand('/lib/platform-config/current/onl/bin/onlpdump -ery')

    with open('test.yml','w') as w:
        w.write(data)
    with open('test.yml', 'r') as r:
        input1 = yaml.safe_load(r)

    Thermal_Dict = input1["Thermals"]

    ThermalIndex = Thermal - 1

    if ThermalIndex <= len(Thermal_Dict):
        if key in Thermal_Dict[ThermalIndex]:
            print("Thermal-{} {}: {}".format(Thermal, key, Thermal_Dict[ThermalIndex][key]))
            return 1
        else:
            #print("Specified key is not present in the dictionary file")
            return 0
    else:
        #print("Index is not matching")
        return -1


def Get_LED_Value(IPAddress, LED, key):
    DUT = Login(IPAddress, 'root', 'onl')

    data = DUT.SendACommand('/lib/platform-config/current/onl/bin/onlpdump -ery')

    with open('test.yml','w') as w:
        w.write(data)
    with open('test.yml', 'r') as r:
        input1 = yaml.safe_load(r)

    LED_Dict = input1["LEDs"]

    LEDIndex = LED - 1

    if LEDIndex <= len(LED_Dict):
        if key in LED_Dict[LEDIndex]:
            print("LED-{} {}: {}".format(LED, key, LED_Dict[LEDIndex][key]))
            return 1
        else:
            #print("Specified key is not present in the dictionary file")
            return 0
    else:
        #print("Index is not matching")
        return -1

