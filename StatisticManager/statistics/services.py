from clickhouse_driver import Client
from views import balance
from time import time

c = Client('localhost')

def create_db():
    c.execute('CREATE DATABASE statistics_db'
        'CREATE TABLE total_balance ( balance UInt64, datetime DateTime) ENGINE = StripeLog')

def new_entry():
    c.execute('INSERT INTO total_balance (balance, datetime) VALUES (%d, %d)') % {balance.as_views(),int(time())}
