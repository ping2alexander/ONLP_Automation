import yaml
import time
import os

from ssh_login import Login

def GetProductName(IPAddress):

    DUT = Login(IPAddress, 'alexander', 'Dafne@140820')
    input1 = DUT.SendACommand('cat onlpdump')

    with open('tmp.yml', 'w') as f:
        f.write(input1.strip())
    with open('tmp.yml','r') as r:
        res = yaml.safe_load(r)
    
    product_Name = res['System Information']['Product Name']
    os.remove('tmp.yml')
    return product_Name

def GetPartNumber(IPAddress):

    DUT = Login(IPAddress, 'alexander', 'Dafne@140820')
    input1 = DUT.SendACommand('cat onlpdump')

    with open('tmp.yml', 'w') as f:
        f.write(input1.strip())
    with open('tmp.yml','r') as r:
        res = yaml.safe_load(r)

    part_Number = res['System Information']['Part Number']
    os.remove('tmp.yml')

    return part_Number

def GetSerialNumber(IPAddress):

    DUT = Login(IPAddress, 'alexander', 'Dafne@140820')
    input1 = DUT.SendACommand('cat onlpdump')

    with open('tmp.yml', 'w') as f:
        f.write(input1.strip())
    with open('tmp.yml','r') as r:
        res = yaml.safe_load(r)

    Serial_Number = res['System Information']['Serial Number']
    os.remove('tmp.yml')

    return Serial_Number

def GetDeviceMAC(IPAddress):

    DUT = Login(IPAddress, 'alexander', 'Dafne@140820')
    input1 = DUT.SendACommand('cat onlpdump')

    with open('tmp.yml', 'w') as f:
        f.write(input1.strip())
    with open('tmp.yml','r') as r:
        res = yaml.safe_load(r)

    Device_MAC = res['System Information']['MAC']
    os.remove('tmp.yml')

    return Device_MAC

def GetDeviceManufacturer(IPAddress):

    DUT = Login(IPAddress, 'alexander', 'Dafne@140820')
    input1 = DUT.SendACommand('cat onlpdump')

    with open('tmp.yml', 'w') as f:
        f.write(input1.strip())
    with open('tmp.yml','r') as r:
        res = yaml.safe_load(r)

    Device_Manufacturer = res['System Information']['Manufacturer']
    os.remove('tmp.yml')

    return Device_Manufacturer


def GetDeviceVendor(IPAddress):

    DUT = Login(IPAddress, 'alexander', 'Dafne@140820')
    input1 = DUT.SendACommand('cat onlpdump')

    with open('tmp.yml', 'w') as f:
        f.write(input1.strip())
    with open('tmp.yml','r') as r:
        res = yaml.safe_load(r)

    Device_Vendor = res['System Information']['Vendor']
    os.remove('tmp.yml')

    return Device_Vendor

def GetPlatformName(IPAddress):

    DUT = Login(IPAddress, 'alexander', 'Dafne@140820')
    input1 = DUT.SendACommand('cat onlpdump')

    with open('tmp.yml', 'w') as f:
        f.write(input1.strip())
    with open('tmp.yml','r') as r:
        res = yaml.safe_load(r)

    Platform_Name = res['System Information']['Platform Name']
    os.remove('tmp.yml')

    return Platform_Name

def GetDeviceVersion(IPAddress):
    DUT = Login(IPAddress, 'alexander', 'Dafne@140820')
    input1 = DUT.SendACommand('cat onlpdump')

    with open('tmp.yml', 'w') as f:
        f.write(input1.strip())
    with open('tmp.yml','r') as r:
        res = yaml.safe_load(r)

    Device_Version = res['System Information']['Device Version']
    os.remove('tmp.yml')

    return Device_Version


def GetLabelRevision(IPAddress):
    DUT = Login(IPAddress, 'alexander', 'Dafne@140820')
    input1 = DUT.SendACommand('cat onlpdump')

    with open('tmp.yml', 'w') as f:
        f.write(input1.strip())
    with open('tmp.yml','r') as r:
        res = yaml.safe_load(r)

    Device_LabelRevision = res['System Information']['Label Revision']
    os.remove('tmp.yml')

    return Device_LabelRevision


def GetDiagVersion(IPAddress):
    DUT = Login(IPAddress, 'alexander', 'Dafne@140820')
    input1 = DUT.SendACommand('cat onlpdump')

    with open('tmp.yml', 'w') as f:
        f.write(input1.strip())
    with open('tmp.yml','r') as r:
        res = yaml.safe_load(r)

    Device_DiagVersion = res['System Information']['Diag Version']
    os.remove('tmp.yml')

    return Device_DiagVersion


def GetServiceTag(IPAddress):
    DUT = Login(IPAddress, 'alexander', 'Dafne@140820')
    input1 = DUT.SendACommand('cat onlpdump')

    with open('tmp.yml', 'w') as f:
        f.write(input1.strip())
    with open('tmp.yml','r') as r:
        res = yaml.safe_load(r)

    Device_ServiceTag = res['System Information']['Service Tag']
    os.remove('tmp.yml')

    return Device_ServiceTag


def GetONIEVersion(IPAddress):
    DUT = Login(IPAddress, 'alexander', 'Dafne@140820')
    input1 = DUT.SendACommand('cat onlpdump')

    with open('tmp.yml', 'w') as f:
        f.write(input1.strip())
    with open('tmp.yml','r') as r:
        res = yaml.safe_load(r)

    Device_ONIEVersion = res['System Information']['ONIE Version']
    os.remove('tmp.yml')

    return Device_ONIEVersion


def GetCountryCode(IPAddress):
    DUT = Login(IPAddress, 'alexander', 'Dafne@140820')
    input1 = DUT.SendACommand('cat onlpdump')

    with open('tmp.yml', 'w') as f:
        f.write(input1.strip())
    with open('tmp.yml','r') as r:
        res = yaml.safe_load(r)

    Device_CountryCode = res['System Information']['Country Code']
    os.remove('tmp.yml')

    return Device_CountryCode


