import os
import unittest
from vcf_creator.vcf import *

csv = os.path.join(os.path.dirname(__file__), 'test.csv')
vcf = os.path.join(os.path.dirname(__file__), 'test.vcf')


class TestVcf(unittest.TestCase):

    def test_vcf_generator(self):
        result = vcard_generator(csv)
        with open(vcf, "r") as file:
            text = file.read()
        self.assertEqual(result, text)


if __name__ == '__main__':
    unittest.main()
