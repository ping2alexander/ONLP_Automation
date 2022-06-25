import pytest

def pytest_addoption(parser):
    parser.addoption("--filename", action="store", default="default name1")
    parser.addoption("--testbed", action="store", default="default name2")
    
#@pytest.fixture
#def filename(request):
#    return request.config.getoption("--filename")

#@pytest.fixture
#def testbed(request):
#    return request.config.getoption("--testbed")


def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value1 = metafunc.config.option.filename
    if 'filename' in metafunc.fixturenames and option_value1 is not None:
        metafunc.parametrize("filename", [option_value1])

    option_value2 = metafunc.config.option.testbed
    if 'testbed' in metafunc.fixturenames and option_value2 is not None:
        metafunc.parametrize("testbed", [option_value2])

