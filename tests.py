import unittest
from contrived_func import contrived_func


class TestContrivedFunc(unittest.TestCase):
    """Test suite for contrived_func achieving full branch and condition
    coverage."""

    def test_1(self):
        """Test with a=T, b=T, c=F, d=T."""
        contrived_func(1)

    def test_2(self):
        """Test with a=T, b=T, c=F, d=F."""
        contrived_func(2)

    def test_3(self):
        """Test with a=T, b=F, c=F, d=T."""
        contrived_func(0)

    def test_4(self):
        """Test with a=T, b=F, c=F, d=F."""
        contrived_func(3)

    def test_5(self):
        """Test with a=F, b=T, c=T, d=F."""
        contrived_func(40)

    def test_6(self):
        """Test with a=F, b=T, c=F, d=F."""
        contrived_func(20)

    def test_7(self):
        """Test with a=F, b=F, c=T, d=F."""
        contrived_func(42)

    def test_8(self):
        """Test with a=F, b=F, c=F, d=F."""
        contrived_func(36)


if __name__ == '__main__':
    unittest.main()
