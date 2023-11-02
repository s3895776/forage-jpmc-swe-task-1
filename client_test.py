import unittest
from client3 import getDataPoint
from client3 import getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      actual_data_point = getDataPoint(quote)
      expected_stock = quote['stock']
      expected_bid_price = quote['top_bid']['price']
      expected_ask_price = quote['top_ask']['price']
      expected_price = (expected_bid_price + expected_ask_price) / 2
      expected_data_point = (expected_stock, expected_bid_price, expected_ask_price, expected_price)

      self.assertEqual(actual_data_point, expected_data_point)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      actual_data_point = getDataPoint(quote)
      expected_stock = quote['stock']
      expected_bid_price = quote['top_bid']['price']
      expected_ask_price = quote['top_ask']['price']
      expected_price = (expected_bid_price + expected_ask_price) / 2
      expected_data_point = (expected_stock, expected_bid_price, expected_ask_price, expected_price)

      self.assertEqual(actual_data_point, expected_data_point)


  """ ------------ Add more unit tests ------------ """

  def test_getRatio_edgeCases(self):
    prices_a = (0,1,-1, 0,-1,1,0,1)
    prices_b = (0,0,0,-1,-1,-1,1,1)
    for i in range(len(prices_a)):
      price_a = prices_a[i]
      price_b = prices_b[i]

      if (price_b == 0):
        self.assertEqual(getRatio(price_a,price_b), None)
      else:
        self.assertEqual(getRatio(price_a,price_b), price_a/price_b)


if __name__ == '__main__':
    unittest.main()
