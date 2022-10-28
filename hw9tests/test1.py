import unittest
from code_func import summ_digits
from code_func import delete_word
from code_func import first_rle
from code_func import sec_rle
from code_func import from10to2
from code_func import lst_keyboard
from code_func import fibonacci
from code_func import even_fn
from code_func import odd
from code_func import secfibonacci


class TestFunc(unittest.TestCase):
    """класс тестов номер 1"""
    def test_summ(self):
        self.assertEqual(summ_digits(123), 6)

    def test_delword(self):
        self.assertEqual(delete_word("абвесили меня сегодня абвечером абв ноабве", "абв"), "меня сегодня")

    def test_coder(self):
        self.assertEqual(first_rle("AAAAAAAAAAAAAABBBBBCDDDDDEEEEEF"), "14A5B1C5D5E1F")

    def test_decoder(self):
        self.assertEqual(sec_rle("14A5B1C5D5E1F"), "AAAAAAAAAAAAAABBBBBCDDDDDEEEEEF")

    def test_cc(self):
        self.assertEqual(from10to2(10), "1010")


class TestFunc2(unittest.TestCase):
    """класс тестов номер 2"""
    def test_lst(self):
        self.assertEqual(lst_keyboard(2), [-2, -1, 0, 1, 2])

    def test_fibo(self):
        self.assertEqual(fibonacci(2), 1)

    def test_even_dig(self):
        self.assertTrue(even_fn(6), True)

    def test_odd_dig(self):
        self.assertFalse(odd(6),True)

    def test_fibo_2(self):
        self.assertEqual(fibonacci(5),secfibonacci(5))
