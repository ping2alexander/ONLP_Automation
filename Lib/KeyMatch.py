import pytest

class IndexNotFound(Exception):
    """Raised when specified index is not found in the dictionary"""
    print("Index is not matching")
class NoModuleFound(Exception):
    """Raised when specified module is not found in the hardware"""
    print("No modules found in the specified hardware")
class KeyNotFound(Exception):
    """Raised when specified key is not found in the dictionary"""
    print("Specified key is not present in the dictionary file")

def Validation(value):
    if value == 1:
        print("Validation passed")
    elif value == 0:
        raise KeyNotFound
    elif value == -1:
        raise IndexNotFound
    elif value == -2:
        raise NoModuleFound
    else:
        pass

def KeyValueMatch(KeyValue):
    with pytest.raises(Exception):
        assert Validation(KeyValue)
