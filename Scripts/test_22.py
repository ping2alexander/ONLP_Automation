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

@pytest.mark.All
@pytest.mark.Sanity
def test_CheckPSUType(test_importlib):

    DUTInfo = test_importlib
    val = Get_PSU_Value(DUTInfo.DUT1_IP, 1, 'Type')

    result = KeyValueMatch(val)

    print(result)

