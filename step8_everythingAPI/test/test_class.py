# content of test_class.py
class TestClass:
    """
    This Function declaring two functions, with pytest
    """
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")


