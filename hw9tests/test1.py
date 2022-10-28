import unittest
from code_func import summ_digits
from code_func import delete_word
from code_func import first_rle
from code_func import sec_rle

class TestFunc(unittest.TestCase):
    def test_summ(self):
        self.assertEqual(summ_digits(123), 6)

    def test_delword(self):
        self.assertEqual(delete_word("абвесили меня сегодня абвечером абв ноабве", "абв"), "меня сегодня")

    def test_coder(self):
        self.assertEqual(first_rle("AAAAAAAAAAAAAABBBBBCDDDDDEEEEEF"),"14A5B1C5D5E1F")

    def test_decoder(self):
        self.assertEqual(sec_rle("14A5B1C5D5E1F"),"AAAAAAAAAAAAAABBBBBCDDDDDEEEEEF")

