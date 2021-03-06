import pandas as pd
from unittest import TestCase
from ..build import plot_corr
from inspect import getfullargspec

data = pd.read_csv('data/house_prices_multivariate.csv')


class TestPlot_corr(TestCase):
    def test_plot_corr_arguments(self):
    # Input parameters tests
        args = getfullargspec(plot_corr)
        self.assertEqual(len(args[0]), 2, "Expected arguments %d, Given %d" % (2, len(args[0])))
    def test_plot_corr_defaults(self):
        args = getfullargspec(plot_corr)
        self.assertEqual(args[3], (11,), "Expected default values do not match given default values")