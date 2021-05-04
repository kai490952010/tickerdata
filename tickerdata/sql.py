CREATE_TICKER_DATA_TABLE = """
	CREATE TABLE tickerdata_1m (
		open numeric(10, 9),
		high numeric(10, 9),
		low numeric(10, 9),
		close numeric(10, 9),
		date_id bigint,
		time_id bigint,
		symbol varchar(50),
		exchange_id int,
		market_id int
	)
"""

CREATE_DATE_DIM = """
	CREATE TABLE date_dim(
		date_id bigint,
		date_str varchar(10),
		weekday varchar(15),
		day_of_week int,
		week_of_year int,
		year int
	)
"""

CREATE_TIME_DIM = """
	CREATE TABLE time_dim(
		time_id bigint,
		time_str varchar(10),
		hour int,
		minute int
	)
"""

CREATE_EXCHANGE_DIM = """
	CREATE TABLE exchange_dim (
		exchange_id int,
		exchange_name varchar(100),
		-- exchange_created_at
	)
"""

CREATE_MARKET_DIM = """
	CREATE TABLE market_dim (
		market_id int,
		market_name varchar(100)
	)
"""