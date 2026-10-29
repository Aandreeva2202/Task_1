from praktikum.bun import Bun


class TestBun:

    def test_bun_get_name(self):
        bun = Bun("black bun", 100.0)
        assert bun.get_name() == "black bun"

    def test_bun_get_price(self):
        bun = Bun("white bun", 200.5)
        assert bun.get_price() == 200.5

    def test_bun_price_type(self):
        bun = Bun("test bun", 99.9)
        assert isinstance(bun.get_price(), float)
