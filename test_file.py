import Graph_functions
import matplotlib.pyplot as plt
import numpy
import card_fetcher
import pandas as pd

import unittest

class TestAPIgivecorrectoutput(unittest.TestCase):

    def test_getting_all_card_from_url(self):
        self.assertIsInstance(card_fetcher.get_all_card_from_search(
            'https://api.scryfall.com/cards/search?q=e:m19'), list)

    def test_getting_pandas_dataframes(self):
        self.assertIsInstance(card_fetcher.get_set('m19'), type(pd.DataFrame()))


if __name__ == '__main__':
    unittest.main()
