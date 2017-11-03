import csv, sys, os

project_dir = "/home/guru/workspace/django/stockchart/stock_chart/stock_chart"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from stock.models import Stockdata

data = csv.reader(open("/home/guru/workspace/django/stockchart/stock_chart/20171031UnderlyingEOD_2016.csv"), delimiter=",")
for row in data:
    if row[0] != 'underlying_symbol':
        stockdata = Stockdata()
        stockdata.underlying_symbol = row[0]
        stockdata.quote_date = row[1]
        stockdata.open = row[2]
        stockdata.high = row[3]
        stockdata.low = row[4]
        stockdata.close = row[5]
        stockdata.trade_volume = row[6]
        stockdata.vwap = row[7]
        stockdata.best_bid_1545 = row[8]
        stockdata.best_ask_1545 = row[9]
        stockdata.best_bid_eod = row[10]
        stockdata.best_ask_eod = row[11]
        stockdata.save()