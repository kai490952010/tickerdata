import os
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