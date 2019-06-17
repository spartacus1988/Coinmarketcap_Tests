from coinmarketcap import Market
import json as jsn
import time
import sys
from datetime import datetime

class CoinmarketcapSpider:

	def __init__(self):
	 	self.json = None
	 	self.start_time = None
	 	self.delta_time = None
	 	self.sizeofjson = None
	 	self.list_ids = list()
	 	self.list_timestamps = list()
	 	self.coinmarketcap = Market()

	def get_first_10_ticker_by_rank(self):
		
		self.start_time = time.time()
		self.json = self.coinmarketcap.ticker(start=0, limit=3, convert='USD', sort='rank')
		self.delta_time = time.time() - self.start_time
		self.sizeofjson = sys.getsizeof(self.json)

		

		print(jsn.dumps(self.json, sort_keys=True, indent=4))
		print(self.delta_time)
		print(self.sizeofjson)


	def fill_list_timestamps(self):
		print(self.json['data'])

		for curid in self.json['data']:
			print(curid)
			print(self.json['data'][curid]['last_updated'])
			curtimestamp = self.json['data'][curid]['last_updated']
			self.list_ids.append(curid)
			self.list_timestamps.append(curtimestamp)

		print(self.list_ids)
		print(self.list_timestamps)



	def first_test_case(self):
		self.get_first_10_ticker_by_rank()
		assert self.delta_time < 0.5

		self.fill_list_timestamps()
		for curts in self.list_timestamps:
			print(datetime.utcfromtimestamp(curts).strftime('%Y-%m-%d'))
			curtime = datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d')
			print("curtime_is:" + curtime)
			assert datetime.utcfromtimestamp(curts).strftime('%Y-%m-%d') == curtime

		assert self.sizeofjson < 10240
			
		
	
			





if __name__ == "__main__":

	CoinmarketcapSpider = CoinmarketcapSpider()
	#CoinmarketcapSpider.get_first_10_ticker_by_rank()
	CoinmarketcapSpider.first_test_case()