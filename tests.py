import unittest
from contrived_func import contrived_func


class TestContrivedFunc(unittest.TestCase):
    """Optimized test suite achieving full branch and condition coverage
    with only 4 tests instead of 8.
    """

    def test_1(self):
        """a=T, b=T, c=F, d=T - Covers Block1:PathA, Block2:PathE.
        
        This test ensures:
        - Decision D1 (a or b) = True
        - Decision D2 ((a and b) or ((b and c) and d)) = True (via a and b)
        - Decision D4 (a and b) = True
        - Provides: a=T, b=T, d=T
        """
        contrived_func(1)

    def test_2(self):
        """a=F, b=T, c=T, d=F - Covers Block1:PathB, Block2:PathF.
        
        This test ensures:
        - Decision D1 (a or b) = True
        - Decision D2 ((a and b) or ((b and c) and d)) = False
        - Decision D4 (a and b) = False
        - Provides: a=F, b=T, c=T, d=F
        """
        contrived_func(40)

    def test_3(self):
        """a=F, b=F, c=T, d=F - Covers Block1:PathC, Block2:PathF.
        
        This test ensures:
        - Decision D1 (a or b) = False (enters else block)
        - Decision D3 (c, since a=F and b=F) = True
        - Decision D4 (a and b) = False
        - Provides: b=F, c=T (additional coverage)
        """
        contrived_func(42)

    def test_4(self):
        """a=F, b=F, c=F, d=F - Covers Block1:PathD, Block2:PathF.
        
        This test ensures:
        - Decision D1 (a or b) = False
        - Decision D3 (c) = False
        - Decision D4 (a and b) = False
        - Provides: c=F (completes condition coverage)
        - This is the only test where all four conditions are False
        """
        contrived_func(36)


if __name__ == '__main__':
    unittest.main()
