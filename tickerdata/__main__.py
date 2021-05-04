from .cryptocurrency import BinanceAPI

if __name__ == '__main__':
	feed = BinanceAPI()
	x = feed.get_historical('BTCUSDT', start_ts=1502942400, end_ts=1503942400)
	import pdb; pdb.set_trace()