import unittest
from vcf_creator.vcf import *

class TestVcf(unittest.TestCase):

    def test_vcf_generator(self):
        result = vcard_generator("test.csv")
        with open("test.vcf", "r") as file:
            vcf = file.read()
        self.assertEqual(result, vcf)       


if __name__ == '__main__':
    unittest.main()