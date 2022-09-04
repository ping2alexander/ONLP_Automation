import pytest
import unittest

#class IndexNotFound(Exception):
#    """Raised when specified index is not found in the dictionary"""
#    return "Index is not matching"
#class NoModuleFound(Exception):
#    """Raised when specified module is not found in the hardware"""
#    return "No modules found in the specified hardware"
#class KeyNotFound(Exception):
#    """Raised when specified key is not found in the dictionary"""
#    return "Specified key is not present in the dictionary file"

class CheckKeyValue(unittest.TestCase):
    def KeyValueMatch(self, val):
        self.assertEqual(val, 1, msg=self.Failure_type(val))

    def Failure_type(self, value):
        if value == 0:
            return "Index is not matching"
        elif value == -2:
            return "No modules found in the specified hardware"
        elif value == -1:
            return "Specified key is not present in the dictionary file"
        else:
            pass

#def KeyValueMatch(KeyValue):
#    with pytest.raises(Exception):
#        assert Validation(KeyValue)
