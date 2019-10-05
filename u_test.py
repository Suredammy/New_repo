from hot_potato import hot_potato
import unittest
names = ["Bill","David","Susan","Jane","Kent","Brad"]
class Test_hot_potato(unittest.TestCase):
    def testEqual(self):
        self.assertEqual(hot_potato(names,9), "Davd")

    if __name__ == "__main__":
        unittest.main()
