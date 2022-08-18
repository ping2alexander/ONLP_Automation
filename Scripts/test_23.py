import pytest
import os.path as path
import sys
import time
import logging
import os
import importlib

parentdir = path.abspath(path.join(__file__,"../.."))
libpath = parentdir + '/Lib'
sys.path.insert(0, libpath)

from ssh_login import Login
from DeviceInfo import *
from GetKeyValue import *
from KeyMatch import *

@pytest.fixture
def test_importlib(filename):
    tmpfile = filename
    tmppath = parentdir + '/tmp'
    sys.path.insert(1, tmppath)

    Tmp = importlib.import_module(filename)
    return Tmp;

#####################################################################
# Testcase No: 23
# Description: FAN description test
# Test area  : ONL API Test
# Priority   : P2
####################################################################

@pytest.mark.All
@pytest.mark.Sanity
@pytest.mark.P2
def test_Check_FAN_Description(test_importlib):

    DUTInfo = test_importlib

    fan1 = Get_FAN_Value(DUTInfo.DUT1_IP, 1, 'Description')
    fan2 = Get_FAN_Value(DUTInfo.DUT1_IP, 2, 'Description')
    fan3 = Get_FAN_Value(DUTInfo.DUT1_IP, 3, 'Description')
    fan4 = Get_FAN_Value(DUTInfo.DUT1_IP, 4, 'Description')

    fan1_result = KeyValueMatch(fan1, 'chassis Fan 1', 'Match')
    fan2_result = KeyValueMatch(fan2, 'chassis Fan 2', 'Match')
    fan3_result = KeyValueMatch(fan3, 'chassis Fan 3', 'Match')
    fan4_result = KeyValueMatch(fan4, 'chassis Fan 4', 'Match')


    psu_1_fan = Get_PSU_FAN_Value(DUTInfo.DUT1_IP, 1, 1, 'Description')
    psu_2_fan = Get_PSU_FAN_Value(DUTInfo.DUT1_IP, 2, 1, 'Description')

    psu_1_fan_result = KeyValueMatch(psu_1_fan, 'PSU Fan 1', 'Match')
    psu_2_fan_result = KeyValueMatch(psu_2_fan, 'PSU Fan 2', 'Match')
