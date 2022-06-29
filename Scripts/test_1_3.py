import pytest
import os.path as path
import sys
import time
import logging
import os

parentdir = path.abspath(path.join(__file__,"../.."))
libpath = parentdir + '/Lib'
sys.path.insert(0, libpath)

from ssh_login import Login
from DeviceInfo import *

@pytest.mark.All
@pytest.mark.Sanity
def test_GetDeviceVersion():
    val = GetDeviceVersion('192.168.1.5')

    print("Current Device version: {}".format(val))
