from unittest import TestCase

from gender_conv import convert_gender


class Test(TestCase):
    def test_convert_gender_for_male(self):
        expected = 'MALE'
        actual = convert_gender('m')
        self.assertEqual(actual, expected)

    def test_convert_gender_for_female(self):
        expected = 'FEMALE'
        actual = convert_gender('f')
        self.assertEqual(actual, expected)
