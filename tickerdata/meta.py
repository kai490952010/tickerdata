import os
from datetime import datetime
from sqlalchemy import create_engine

def get_sql_engine():
	"""
		Gets postgres sql connection using
		credentials in environment.
	"""
	username = os.environ.get('TA_USERNAME')
	password = os.environ.get('TA_PASSWORD')
	host = os.environ.get('TA_HOST')
	database = os.environ.get('TA_DATABASE')

	sql_engine = create_engine(
	    "postgresql://{:s}:{:s}@{:s}/{:s}".format(
	    	username, password, host, database),
	    execution_options={
	        "isolation_level": "REPEATABLE READ"
	    }
	)
	return sql_engine


class metaApi():
    def __init__(self):
        pass

    @property
    def current_epoch_ts(self):
        return round(datetime.now().timestamp())

    def get_min_max_ts(self, symbol, granularity, **kwargs):
        """
            Get min-max timestamps for available data of a coinpair,
            to restart data collection from latest end timestamp.

            Args:
                symbol (str): symbol to get latest available timestamps for.
                granularity (str): used to get SQL table because
                    granularity will be a component of table name.
                    Options: 1m, 5m, 30m, 1h, 4h, 1D, 1W, 1M

            Returns:
                tuple, (start_ts, end_ts)

            TODO: 
            	Implement functionality
        """
        self.symbol = kwargs.get('symbol')
        self.granularity = kwargs.get('granularity')
        raise NotImplementedError