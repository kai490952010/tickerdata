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

BINSIZES = {"1m": 1, "5m": 5, "1h": 60, "1d": 1440}

class metaApi():
    def __init__(self):
        self.exchange = exchange

    def get_min_max_ts(self, **kwargs):
        """
            Get min-max timestamps for available data of a coinpair
        """
        symbol = kwargs.get('symbol')
        granularity = kwargs.get('granularity')

        pass

class BinanceAPI():
    """
        Class creates custom functionality around
        Coingecko API to make data pulls easier
    """
    def __init__(self):
        from binance.client import Client
        api_key = os.environ.get('BINANCE_API_KEY')
        api_secret = os.environ.get('BINANCE_API_SECRET')
        self.api = Client(api_key, api_secret)
        kline_size = {
            '1m': self.api.KLINE_INTERVAL_1MINUTE,
            '5m': self.api.KLINE_INTERVAL_5MINUTE
        }

    @property
    def kline_constants(self):
        """
            Class property that returns Binance's Kline constants 
        """
        return {
            '1m': self.api.KLINE_INTERVAL_1MINUTE,
            '3m': self.api.KLINE_INTERVAL_3MINUTE,
            '5m': self.api.KLINE_INTERVAL_5MINUTE,
            '15m': self.api.KLINE_INTERVAL_15MINUTE,
            '30m': self.api.KLINE_INTERVAL_30MINUTE,
            '1h': self.api.KLINE_INTERVAL_1HOUR,
            '2h': self.api.KLINE_INTERVAL_2HOUR,
            '4h': self.api.KLINE_INTERVAL_4HOUR,
            '6h': self.api.KLINE_INTERVAL_6HOUR,
            '8h': self.api.KLINE_INTERVAL_8HOUR,
            '12h': self.api.KLINE_INTERVAL_12HOUR,
            '1d': self.api.KLINE_INTERVAL_1DAY,
            '3d': self.api.KLINE_INTERVAL_3DAY,
            '1w': self.api.KLINE_INTERVAL_1WEEK,
            '1M': self.api.KLINE_INTERVAL_1MONTH
        }

    def get_historical(self, symbol, start_ts=1388534461, end_ts=1388538061, granularity='1m'):
        start_ts = datetime.utcfromtimestamp(start_ts).strftime("%d %b %Y %H:%M:%S")
        end_ts = datetime.utcfromtimestamp(end_ts).strftime("%d %b %Y %H:%M:%S")
        # kline interval
        interval = self.kline_constants.get(granularity)
        klines = self.api.get_historical_klines(symbol, 
            interval, 
            start_ts,
            end_ts)

        data = pd.DataFrame(klines,
            columns = ['timestamp',
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
                'ignore' ])
        return data


class CoingeckoAPI():
    """
        Class creates custom functionality around
        Coingecko API to make data pulls easier
    """
    def __init__(self):
        from pycoingecko import CoinGeckoAPI
        self.api = CoinGeckoAPI()

    @property
    def exchanges(self):
        return [ex['id'] for ex in self.api.get_exchanges_list()]

    def get_coin_pairs(self, exchange='binance', **kwargs):
        """
            Gets coin pairs for all coins listed in an exchange.

            Arg:
                exchange: str. Ex: binance, bitmex
            Returns:
                list, ['ADAUSD', 'ADAEUR', 'ADABTC']..
        """
        if exchange in self.exchanges:
            pass
        else:
            raise NotImplementedError("{:s} exchange does not exist on CoinGeckoAPI".format(exchange))

    def get_history(self, granularity='30min'):
        raise NotImplementedError
