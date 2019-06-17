from coinmarketcap import Market
import json as jsn

class CoinmarketcapSpider:

	def __init__(self):
	 	self.json = None
	 	self.coinmarketcap = Market()

	def get_first_10_ticker_by_rank(self):
		

		self.json = self.coinmarketcap.ticker(start=0, limit=3, convert='USD')

		#self.json = jsn.loads(self.json)
		print(jsn.dumps(self.json, sort_keys=True, indent=4))
		#print(self.json)





if __name__ == "__main__":

	CoinmarketcapSpider = CoinmarketcapSpider()
	CoinmarketcapSpider.get_first_10_ticker_by_rank()