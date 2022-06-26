import pytest
import os.path as path
import sys
import importlib

tmpfile = ''

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
    DUTInfo=importlib.import_module(filename)
        
    #print(DUTInfo.DUT1_IP)

    #DUT1 = Login(DUTInfo.DUT1_IP, DUTInfo.DUT1_Username, DUTInfo.DUT1_Password)
    #DUT1.SendACommand('cat onlpdump')
    #DUT1.Logout()
    
    return DUTInfo

# This fucntion will collect and store all system information from DUTs listed in testbed file.

def test_collect_sysinfo(test_importlib):
    try:
        test_importlib.DUT3_IP
        print('OK')
    except:
        print("NOT OK")
