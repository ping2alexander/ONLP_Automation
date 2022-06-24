from schema import Schema, SchemaError, Optional
import yaml
import pytest
import time
import logging

key = 0
new_filename = ''
log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@pytest.fixture
def test_convert_yml_to_dict():
    with open('./../cfg/testbed.yml', 'r') as f:
        my_dict = yaml.safe_load(f)
      
    print(my_dict)
    return my_dict

@pytest.fixture
def test_check_syntax_error(test_convert_yml_to_dict):    
    config_schema = Schema({'HardwareList': {'DUT1': {'Hardware_type': str, 'access': {'protocol': str, 'ip': str, 'port': int}, 'credentials': {'username': str, 'password': str}}, 'DUT2': {'Hardware_type': str, 'access': {'protocol': str, 'ip': str, 'port': int}, 'credentials': {'username': str, 'password': str}}}, Optional('Connection'): {'DUT1': {Optional('interfaces'): [{'LocalPort': str, 'RemoteDevice': str, 'RemotePort': str}]}, 'DUT2': {Optional('interfaces'): [{'LocalPort': str, 'RemoteDevice': str, 'RemotePort': str}]}}})

    try:
        config_schema.validate(test_convert_yml_to_dict)
        print("No syntax error found in the testbed file.")
        return 0;
    except SchemaError as se:
        raise se
        return -1;
    

def test_parse_testbed_file(test_check_syntax_error):
    if test_check_syntax_error != 0:
        print("Error in the testbed file. script terminated !!!")
        return -1;
    else:
        print("No syntax error found in the testbed file.")

def test_CheckKeyExist(test_convert_yml_to_dict):
    global key

    my_dict = test_convert_yml_to_dict
    key = 'Connection'

    if key in my_dict:
        key = 1
    else:
        key = 0

def test_createTmpfile(filename):

    global new_filename
    timestr = time.strftime("%Y%m%d-%H%M%S") 
    new_filename = filename + timestr + '.py'
    return new_filename
    

def test_create_tmpfile(test_convert_yml_to_dict):
    global new_filename
    temp = test_convert_yml_to_dict
    temp1 = './../tmp/'
    new_filename = temp1 + new_filename

    print(new_filename)

    with open(new_filename, 'w+') as f:
        DUT1_HwType = temp['HardwareList']['DUT1']['Hardware_type']
        DUT1_Protocol = temp['HardwareList']['DUT1']['access']['protocol']
        DUT1_IP = temp['HardwareList']['DUT1']['access']['ip']
        DUT1_Port = temp['HardwareList']['DUT1']['access']['port']
        DUT1_Username = temp['HardwareList']['DUT1']['credentials']['username']
        DUT1_Password = temp['HardwareList']['DUT1']['credentials']['password']
        DUT2_HwType = temp['HardwareList']['DUT2']['Hardware_type']
        DUT2_Protocol = temp['HardwareList']['DUT2']['access']['protocol']
        DUT2_IP = temp['HardwareList']['DUT2']['access']['ip']
        DUT2_Port = temp['HardwareList']['DUT2']['access']['port']
        DUT2_Username = temp['HardwareList']['DUT2']['credentials']['username']
        DUT2_Password = temp['HardwareList']['DUT2']['credentials']['password']
        
        f.write(str('DUT1_HwType') + "=" + DUT1_HwType + '\n')
        f.write(str('DUT1_Protocol') + "=" + DUT1_Protocol + '\n')
        f.write(str('DUT1_IP') + "=" + DUT1_IP + '\n')
        f.write(str('DUT1_Username') + "=" + DUT1_Username + '\n')
        f.write(str('DUT1_Password') + "=" + DUT1_Password + '\n')
        f.write(str('DUT2_HwType') + "=" + DUT2_HwType + '\n')
        f.write(str('DUT2_Protocol') + "=" + DUT2_Protocol + '\n')
        f.write(str('DUT2_IP') + "=" + DUT2_IP + '\n')
        f.write(str('DUT2_Username') + "=" + DUT2_Username + '\n')
        f.write(str('DUT2_Password') + "=" + DUT2_Password + '\n')
        
        if key == 1:
        
            DUT1interfaceList = temp['Connection']['DUT1']['interfaces']
            DUT2interfaceList = temp['Connection']['DUT2']['interfaces']

            Trunk = dict()

            Trunk[1] = dict()
            Trunk[1][2] = dict()

            Trunk[2] = dict()
            Trunk[2][1] = dict()

            i = 0
            j = 1

            while i < len(DUT1interfaceList):
                Trunk[1][2][j] = DUT1interfaceList[i]['LocalPort']
                f.write(str('Trunk[1][2]') + '[' + str(j) + ']' + "=" + Trunk[1][2][j] + '\n')
                i = i + 1
                j = j + 1

            i = 0
            j = 1

            while i < len(DUT2interfaceList):
                Trunk[2][1][j] = DUT2interfaceList[i]['LocalPort']
                f.write(str('Trunk[2][1]') + '[' + str(j) + ']' + "=" + Trunk[2][1][j] + '\n')
                i = i + 1
                j = j + 1

   

