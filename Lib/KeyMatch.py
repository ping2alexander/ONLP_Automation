import pytest

def KeyValueMatch(KeyValue, Input, Match):
    if Match == 'match':
        assert KeyValue == Input
    elif Match == 'not match':
        assert KeyValue != Input

