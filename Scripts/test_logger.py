import pytest
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def test_print():
    print("Hello.. This is just a sample code !!!!")
    logger.info("mesaage printed successfully")
def test_compare():
    assert 1 == 2
    logger.error("Assertion failed.")
def test_add():
    var1 = 1
    var2 = 2
    result = var1 + var2

    return result

def test_multiply():
    var1 = 10
    var2 = 10

    result = var1 * var2

    return result
