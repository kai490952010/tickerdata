"""
    Implements helper functions to get crypto
    ticker data.

    API used: Binance (for historical data), CoinGeckoAPI
"""

import os
from datetime import datetime
import pandas as pd

from sqlalchemy import create_engine
from .meta import get_sql_engine

class BinanceAPI():
    """
        Class creates custom functionality around
        Binance API to make data pulls easier
    """

    def __init__(self):
        from binance.client import Client

        api_key = os.environ.get('BINANCE_API_KEY')
        api_secret = os.environ.get('BINANCE_API_SECRET')
        if not all([api_key, api_secret]):
            raise Exception("Binance API could not find API key/secret.")
        self.api = Client(api_key, api_secret)


    def get_historical(self, symbol, start_ts=None, end_ts=None, granularity='1m'):
        """
            Calls Binance api to get data for given timestamp range.

            Args:
                symbol (str): Symbol for which data is to be extracted.
                start_ts (int): Epoch timestamp in seconds to denote the starting period
                end_ts (int): Epoch timestamp in seconds to denote the ending period
                granularity (str): Candlestick timeframe. ex: 1m will return 1 minute 
                    candles. For full list of available options, see function kline_constants.

            Returns:
                Pandas dataframe
        """
        # interval = self.kline_constants.get(granularity)
        interval = granularity
        
        if start_ts and end_ts and interval:
            start_ts = datetime.utcfromtimestamp(start_ts).strftime("%d %b %Y %H:%M:%S")
            end_ts = datetime.utcfromtimestamp(end_ts).strftime("%d %b %Y %H:%M:%S")
            klines = self.api.get_historical_klines(symbol, 
                interval, 
                start_ts,
                end_ts)

            data = pd.DataFrame(klines,
                columns = ['open_time',
                    'open',
                    'high',
                    'low',
                    'close',
                    'volume',
                    'close_time',
                    'quote_av',
                    'trades',
                    'tb_base_av',
                    'tb_quote_av',
                    'ignore' ],
                dtypes={
                    'open_time': int,
                    'close_time': int
                })
            data = data.drop(['ignore'], axis=1)
            data.loc[:, "symbol"] = symbol
            data.loc[:, "symbol_id"] = 0
            return data
        else:
            raise Exception("Binance API: Start and end timestamps not specified.")


class CoingeckoAPI():
    """
        Class creates custom functionality around
        Coingecko API to provide metadata on crypto market data.
    """
    def __init__(self):
        from pycoingecko import CoinGeckoAPI
        self.api = CoinGeckoAPI()

    @property
    def exchanges(self):
        """
            Provides list of available exchanges with data available on Coingecko.

            Returns:
                List of exhanges.
        """
        return [ex['id'] for ex in self.api.get_exchanges_list()]

    def get_coin_pairs(self, exchange='binance', **kwargs):
        """
            Gets coin pairs for the top 100 coins listed in an exchange,
            by market cap.

            Arg:
                exchange: str. Ex: binance, bitmex
            Returns:
                list, ['ADAUSD', 'ADAEUR', 'ADABTC']..
        """
        coinfeeds = self.api.get_exchanges_tickers_by_id('binance')
        coinlistings = coinfeeds.get('tickers')
        coins = [
                    "".join([l['base'], l['target']]) 
                    for l in coinlistings
                ]
        return coins