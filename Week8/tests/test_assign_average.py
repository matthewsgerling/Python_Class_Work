from Week8.Collections.assign_average import switch_average


def testA(self):
    with self.assertRaise(ValueError):
        assert switch_average('a')


def testB(self):
    with self.assertRaise(ValueError):
        assert switch_average('b')


def testC(self):
    with self.assertRaise(ValueError):
        assert switch_average('c')


def testD(self):
    with self.assertRaise(ValueError):
        assert switch_average('d')


def testE(self):
    with self.assertRaise(ValueError):
        assert switch_average('e')



