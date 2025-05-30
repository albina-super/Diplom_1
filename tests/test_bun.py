from data import BUN_NAME, BUN_PRICE


class TestBun:

    def test_get_name(self, bun):
        assert bun.get_name() == BUN_NAME


    def test_get_price(self, bun):
        assert bun.get_price() == BUN_PRICE