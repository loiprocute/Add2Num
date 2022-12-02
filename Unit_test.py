from  MyBigNumber import *
import unittest


class Testing(unittest.TestCase):
    def test1(self):
        self.assertEqual(MyBigNumber("99999999","999999999"),99999999+999999999)

    def test2(self):
        self.assertEqual(MyBigNumber("6195","2785"),6195 + 2785)
    def test3(self):
        self.assertEqual(MyBigNumber("47836","5409"),47836 + 5409) 
    def test4(self):
        self.assertEqual(MyBigNumber("10592","10592"),  10592 + 10592)
    def test5(self):
        self.assertEqual(MyBigNumber("0","1999999999"),0+1999999999)
    def test6(self):
        self.assertEqual(MyBigNumber("99999999","1999999999"),99999999+1999999999)
    def test7(self):
        self.assertEqual(MyBigNumber("1171","227776"),1171+227776)
    def test8(self):
        self.assertEqual(MyBigNumber("999999","2269898"),999999+2269898)
    def test9(self):
        self.assertEqual(MyBigNumber("0","0"),0+0)
    def test10(self):
        self.assertEqual(MyBigNumber("117","26"),117+26)
    def test11(self):
        self.assertEqual(MyBigNumber("1","2"),1+2)
    def test12(self):
        self.assertEqual(MyBigNumber("0","26"),0+26)
    def test13(self):
        self.assertEqual(MyBigNumber("117","0"),117+0)
    def test14(self):
        self.assertEqual(MyBigNumber("117","2656666"),117+2656666)
    def test15(self):
        self.assertEqual(MyBigNumber("117","26000000"),117+26000000)

if __name__ == '__main__':
    unittest.main()