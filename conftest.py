import pytest
from praktikum.bun import Bun
from data import BUN_PRICE, BUN_NAME

@pytest.fixture(scope='session')
def bun():
    bun = Bun(price=BUN_PRICE, name=BUN_NAME)
    return bun