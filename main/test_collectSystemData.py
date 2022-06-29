import pytest
import os.path as path
import sys
import importlib
import json
import yaml
import time
import logging
import os

parentdir = path.abspath(path.join(__file__,"../.."))
libpath = parentdir + '/Lib'
sys.path.insert(0, libpath)
from ssh_login import Login

tmpfile = ''

log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def logmessage(msg, level):
    log_formatter = '%(asctime)s %(filename)s %(name)s %(levelname)s \"%(message)s\"'
    logging.basicConfig(format=log_formatter, level=level, datefmt='%d-%b-%y %H:%M:%S')
    if level == logging.DEBUG:
        logging.debug(msg)
    if level == logging.ERROR:
        logging.error(msg)
    if level == logging.WARNING:
        logging.warning(msg)
    if level == logging.INFO:
        logging.info(msg)


@pytest.fixture
def test_importlib(filename):
    global tmpfile
    tmpfile = filename
    parentdir = path.abspath(path.join(__file__,"../.."))
    libpath = parentdir + '/Lib'
    sys.path.insert(0, libpath)
    tmppath = parentdir + '/tmp'
    sys.path.insert(1, tmppath)

    from ssh_login import Login
    Tmp = importlib.import_module(filename) 
    return Tmp;

def test_reachability(test_importlib):
    DUTInfo = test_importlib
    try:
        DUTInfo.DUT1_IP

        print("DUT1_IP variable is defined!!!")
        command = "ping -c 5 " + DUTInfo.DUT1_IP

        HOST_Status = os.system(command)

        if HOST_Status is 0:
            print("DUT1 - {} - Device is reachable - success!!!".format(DUTInfo.DUT1_IP))
        else:
            print("DUT1 - {} - Device is NOT reachable  -  Failed!!!".format(DUTInfo.DUT1_IP))
    except NameError:
        print("DUT1_IP variable is NOT defined anywhere in the configuration file")
        exit;
    
    try:
        DUTInfo.DUT2_IP

        print("DUT2_IP variable is defined!!!")
        command = "ping -c 5 " + DUTInfo.DUT2_IP

        HOST_Status = os.system(command)

        if HOST_Status is 0:
            print("DUT2 -{} - Device is reachable - Success!!!".format(DUTInfo.DUT2_IP))
        else:
            print("DUT2 - {} - Device is NOT reachable  - Failed!!!".format(DUTInfo.DUT2_IP))
    except NameError:
        print("DUT2_IP variable is NOT defined anywhere in the configuration file")
        return
    


# This fucntion will collect and store all system information from DUTs listed in testbed file.

def test_collect_sysinfo(test_importlib):
    DUTInfo = test_importlib
    try:
        DUTInfo.DUT1_IP
        print("DUT1_IP variable is defined!!!")
    except NameError:
        print("NOT OK")
        exit

    DUT1 = Login(DUTInfo.DUT1_IP, DUTInfo.DUT1_Username, DUTInfo.DUT1_Password)

    input1 = DUT1.SendACommand('cat onlpdump')

    with open('a.yml', 'w') as f:
        f.write(input1.strip())
    
    with open('a.yml','r') as r:
        res = yaml.safe_load(r)
     
    temp1 = './../tmp/'
    new_filename = temp1 + tmpfile + '.py'
    print('\n')

    with open(new_filename, 'a') as f:
        DUT1_Product_Name = str(res['System Information']['Product Name'])
        DUT1_Part_Number = str(res['System Information']['Part Number'])
        DUT1_Serial_Number = str(res['System Information']['Serial Number'])
        DUT1_MAC = str(res['System Information']['MAC'])
        DUT1_MAC_Range = str(res['System Information']['MAC Range'])
        DUT1_Manufacturer = str(res['System Information']['Manufacturer'])
        DUT1_Manufacture_Date = str(res['System Information']['Manufacture Date'])
        DUT1_Vendor = str(res['System Information']['Vendor'])
        DUT1_Platform_Name = str(res['System Information']['Platform Name'])
        DUT1_Device_Version = str(res['System Information']['Device Version'])
        DUT1_Label_Revision = str(res['System Information']['Label Revision'])
        DUT1_Country_Code = str(res['System Information']['Country Code'])
        DUT1_Diag_Version = str(res['System Information']['Diag Version'])
        DUT1_Service_Tag = str(res['System Information']['Service Tag'])
        DUT1_ONIE_Version = str(res['System Information']['ONIE Version'])

        f.write(str('DUT1_Product_Name') + "=" + "\"" + DUT1_Product_Name + "\"" + '\n')
        f.write(str('DUT1_Part_Number') + "=" + "\"" + DUT1_Part_Number + "\"" + '\n')
        f.write(str('DUT1_Serial_Number') + "=" + "\"" + DUT1_Serial_Number + "\"" + '\n')
        f.write(str('DUT1_MAC') + "=" + "\"" + DUT1_MAC + "\"" + '\n')
        f.write(str('DUT1_MAC_Range') + "=" + "\"" + DUT1_MAC_Range + "\"" + '\n')
        f.write(str('DUT1_Manufacturer') + "=" + "\"" + DUT1_Manufacturer + "\"" + '\n')
        f.write(str('DUT1_Manufacture_Date') + "=" + "\"" + DUT1_Manufacture_Date + "\"" + '\n')
        f.write(str('DUT1_Vendor') + "=" + "\"" + DUT1_Vendor + "\"" + '\n')
        f.write(str('DUT1_Platform_Name') + "=" + "\"" + DUT1_Platform_Name + "\"" + '\n')
        f.write(str('DUT1_Device_Version') + "=" + "\"" + DUT1_Device_Version + "\"" + '\n')
        f.write(str('DUT1_Label_Revision') + "=" + "\"" + DUT1_Label_Revision + "\"" + '\n')
        f.write(str('DUT1_Country_Code') + "=" + "\"" + DUT1_Country_Code + "\"" + '\n')
        f.write(str('DUT1_Diag_Version') + "=" + "\"" + DUT1_Diag_Version + "\"" + '\n')
        f.write(str('DUT1_Service_Tag') + "=" + "\"" + DUT1_Service_Tag + "\"" + '\n')
        f.write(str('DUT1_ONIE_Version') + "=" + "\"" + DUT1_ONIE_Version + "\"" + '\n')

    try:
        DUTInfo.DUT2_IP
        print("DUT2_IP variable is defined!!!")
     
        DUT2 = Login(DUTInfo.DUT2_IP, DUTInfo.DUT2_Username, DUTInfo.DUT2_Password)

        input2 = DUT2.SendACommand('cat onlpdump')

        with open('a.yml', 'w') as f:
            f.write(input2.strip())

        with open('a.yml','r') as r:
            res = yaml.safe_load(r)
    
        with open(new_filename, 'a') as f:
            DUT2_Product_Name = str(res['System Information']['Product Name'])
            DUT2_Part_Number = str(res['System Information']['Part Number'])
            DUT2_Serial_Number = str(res['System Information']['Serial Number'])
            DUT2_MAC = str(res['System Information']['MAC'])
            DUT2_MAC_Range = str(res['System Information']['MAC Range'])
            DUT2_Manufacturer = str(res['System Information']['Manufacturer'])
            DUT2_Manufacture_Date = str(res['System Information']['Manufacture Date'])
            DUT2_Vendor = str(res['System Information']['Vendor'])
            DUT2_Platform_Name = str(res['System Information']['Platform Name'])
            DUT2_Device_Version = str(res['System Information']['Device Version'])
            DUT2_Label_Revision = str(res['System Information']['Label Revision'])
            DUT2_Country_Code = str(res['System Information']['Country Code'])
            DUT2_Diag_Version = str(res['System Information']['Diag Version'])
            DUT2_Service_Tag = str(res['System Information']['Service Tag'])
            DUT2_ONIE_Version = str(res['System Information']['ONIE Version'])


            f.write(str('DUT2_Product_Name') + "=" + "\"" + DUT2_Product_Name + "\"" + '\n')
            f.write(str('DUT2_Part_Number') + "=" + "\"" + DUT2_Part_Number + "\"" + '\n')
            f.write(str('DUT2_Serial_Number') + "=" + "\"" + DUT2_Serial_Number + "\"" + '\n')
            f.write(str('DUT2_MAC') + "=" + "\"" + DUT2_MAC + "\"" + '\n')
            f.write(str('DUT2_MAC_Range') + "=" + "\"" + DUT2_MAC_Range + "\"" + '\n')
            f.write(str('DUT2_Manufacturer') + "=" + "\"" + DUT2_Manufacturer + "\"" + '\n')
            f.write(str('DUT2_Manufacture_Date') + "=" + "\"" + DUT2_Manufacture_Date + "\"" + '\n')
            f.write(str('DUT2_Vendor') + "=" + "\"" + DUT2_Vendor + "\"" + '\n')
            f.write(str('DUT2_Platform_Name') + "=" + "\"" + DUT2_Platform_Name + "\"" + '\n')
            f.write(str('DUT2_Device_Version') + "=" + "\"" + DUT2_Device_Version + "\"" + '\n')
            f.write(str('DUT2_Label_Revision') + "=" + "\"" + DUT2_Label_Revision + "\"" + '\n')
            f.write(str('DUT2_Country_Code') + "=" + "\"" + DUT2_Country_Code + "\"" + '\n')
            f.write(str('DUT2_Diag_Version') + "=" + "\"" + DUT2_Diag_Version + "\"" + '\n')
            f.write(str('DUT2_Service_Tag') + "=" + "\"" + DUT2_Service_Tag + "\"" + '\n')
            f.write(str('DUT2_ONIE_Version') + "=" + "\"" + DUT2_ONIE_Version + "\"" + '\n')
        
    except NameError:
        print("DUT2_IP is not defined in the configuration file")

    result = path.exists(new_filename)

    if result:
        logmessage("Temp file is created and values are populated", logging.INFO)
        try:
            with open(new_filename, 'r') as r:
                data = r.read()
                print("********************************************************************")
                print(new_filename)
                print("********************************************************************")
                print(data)
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
    else:
        logmessage("Temp file is NOT created", logging.ERROR)

    DUT1.Logout()


