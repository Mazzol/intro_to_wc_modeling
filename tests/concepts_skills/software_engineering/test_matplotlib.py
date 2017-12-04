""" Tests the matplotlib example

:Author: Jonathan Karr <jonrkarr@gmail.com>
:Date: 2017-07-11
:Copyright: 2017, Karr Lab
:License: MIT
"""

from intro_to_wc_modeling.concepts_skills.software_engineering import matplotlib_example
import unittest


class TestMatplotlibExample(unittest.TestCase):

    def test(self):
        matplotlib_example.main()
