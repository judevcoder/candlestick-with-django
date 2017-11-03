# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Stockdata
import pandas as pd
import sqlite3
import datetime
import simplejson
import json
from django.shortcuts import render_to_response
import time
# Create your views here.

def index(request):

    if request.method == 'GET':
        con = sqlite3.connect("db.sqlite3")
        df = pd.read_sql("SELECT * from stockdata", con)
        open = list(df['open'])
        high = list(df['high'])
        low = list(df['low'])
        close = list(df['close'])
        date = list(df['quote_date'])
        # data = [open, high, low, close, date]
        # json_data = simplejson.dumps(data)

        return render_to_response('stock/index.html')

def stockdata(request):
    if request.method == 'GET':
        stock_data = []
        con = sqlite3.connect("db.sqlite3")
        df = pd.read_sql("SELECT * from stockdata", con)

        for idx, val in enumerate(list(df['underlying_symbol'])):
            if val == 'AMZN':
                date = list(df['quote_date'])[idx]
                # timestamp = time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").timetuple())
                open = list(df['open'])[idx]
                high = list(df['high'])[idx]
                low = list(df['low'])[idx]
                close = list(df['close'])[idx]
                data = [date, open, high, low, close]
                stock_data.append(data)
    return HttpResponse(json.dumps(stock_data), content_type="application/json")
    # open_data = []
    # high_data = []
    # low_data = []
    # close_data = []
    # for idx, val in enumerate(list(df['underlying_symbol'])):
    #     date = list(df['quote_date'])[idx]
    #     open = list(df['open'])[idx]
    #     high = list(df['high'])[idx]
    #     low = list(df['low'])[idx]
    #     close = list(df['close'])[idx]
    #     trade_volume = list(df['trade_volume'])[idx]
    #     vwap = list(df['vwap'])[idx]
    #     best_bid_1545 = list(df['best_bid_1545'])[idx]
    #     best_ask_1545 = list(df['best_ask_1545'])[idx]
    #     best_bid_eod = list(df['best_bid_eod'])[idx]
    #     best_ask_eod = list(df['best_ask_eod'])[idx]
    #     open_data.append(open)
    #     high_data.append(high)
    #     low_data.append(low)
    #     close_data.append(close)
    #     open_stock = {'open': open_data}
    #     high_stock = {'high': high_data}
    #     low_stock = {'low': low_data}
    #     close_stock = {'close': close}
    # data = Stockdata.objects.all()
    # stockdata = []
    # for idx, val in enumerate(list(data)):
    #     underlying_symbol = val.underlying_symbol
    #     quote_date = val.quote_date.date()
    #     open = float(val.open)
    #     high = float(val.high)
    #     low = float(val.low)
    #     close = float(val.close)
    #     trade_volume = val.trade_volume
    #     vwap = float(val.vwap)
    #     best_bid_1545 = float(val.best_bid_1545)
    #     best_ask_1545 = float(val.best_ask_1545)
    #     best_bid_eod = float(val.best_bid_eod)
    #     best_ask_eod = float(val.best_ask_eod)
    #     stock = [open, high, low, close, trade_volume, vwap, best_bid_1545, best_ask_1545, best_bid_eod, best_ask_eod]
    #     stockdata.append(stock)
    # date = data.quote_date
    # return HttpResponse("ddddd")

