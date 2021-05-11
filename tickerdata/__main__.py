from .cryptocurrency import BinanceAPI

if __name__ == '__main__':
	# import pdb; pdb.set_trace()	
	feed = BinanceAPI()
	x = feed.get_historical('BTCUSDT', start_ts=1502942400, end_ts=1502982400)
	print(x)