import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    # stock, bid_price, ask_price, price
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # self.assertEqual(getDataPoint(quotes[0]), ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2))
    # self.assertEqual(getDataPoint(quotes[1]), ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2))

    for q in quotes:
       bid_price_test = q['top_bid']['price']
       ask_price_test = q['top_ask']['price']
       self.assertEqual(getDataPoint(q), (q['stock'], bid_price_test, ask_price_test, (bid_price_test + ask_price_test) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for q in quotes:
      bid_price_test = q['top_bid']['price']
      ask_price_test = q['top_ask']['price']
      self.assertEqual(getDataPoint(q), (q['stock'], bid_price_test, ask_price_test, (bid_price_test + ask_price_test) / 2))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
    # Use same quotes from prior unit tests
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    # for q in quotes:
    #   stock, bid_price, ask_price, price = getDataPoint(q)
    #   self.assertEqual(getRatio())

    # Iterate through quotes and test ratio of every two quotes.
    # Requires quotes to be of even length
    for i in range(len(quotes) - 1):
      stock_a, bid_a, ask_a, price_a = getDataPoint(quotes[i])
      stock_b, bid_b, ask_b, price_b = getDataPoint(quotes[i + 1])

      self.assertEqual(getRatio(price_a=price_a, price_b=price_b), (price_a / price_b))
  
  # "Negative" test to make sure a zero price_b returns nothing to avoid a Divide by Zero error
  def test_getRatio_Zero(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    stock_a, bid_a, ask_a, price_a = getDataPoint(quotes[0])
    stock_b, bid_b, ask_b, price_b = getDataPoint(quotes[1])
    self.assertIsNone(getRatio(price_a=price_a, price_b=price_b))



if __name__ == '__main__':
    unittest.main()
