#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import time
import threading
import os
import requests
from googlefinance import getQuotes
from yahoo_finance import Share
import profile

GLUU = 0
LLNW = 1
HACK = 2

# How to get quote: quote = json.dumps(getQuotes('AAPL'), indent=2)
# How to get specific thing from quote: print getQuotes('AAP')[0]['LastTradePrice']

# c = Commission

c = 9.99


# Misc Functions
# Returns percentage

def percentage(part, whole):
    return 100 * float(part) / float(whole)


# Returns current date

def date():
    dater = time.strftime('%m/%d/%Y %H:%M:%S')
    return dater
    threading.Timer(60, date).start()


class Holding:

    """Get value, Get day change, Get total change, Store holdings"""

    def __init__(
        self,
        symbol,
        shares,
        price_paid,
        ):

        self.symbol = symbol
        self.shares = shares
        self.price_paid = price_paid

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.symbol

    def day_change(self):
        dc = self.price - float(Share(self.symbol).get_prev_close())

        # tdc = Total Day Change (what we want)

        tdc = int(float(self.shares)) * dc
        return tdc

    def total_change(self):

        # Market Value - Commission - (Price Paid x Shares Owned)

        tc = self.value - c - self.price_paid * self.shares
        return tc

    def update(self, google_data):
        self.price = float(google_data['LastTradePrice'])
        self.value = self.shares * self.price


class Portfolio:

    def __init__(self):
        self.holdings = []

    def addHolding(self, holding):
        self.holdings.append(holding)
        return self.holdings

    def total_value(self):
        totalvalue = sum([h.value for h in self.holdings])
        return totalvalue

    def total_value_readable(self):
        totalvalue = sum([h.value for h in self.holdings])
        rounded = round(totalvalue, 2)

        # Total Value Readable

        tvr = '$%s' % rounded
        return tvr

    def total_day_change(self):
        totaldaychange = sum([h.day_change() for h in self.holdings])
        return totaldaychange

    def total_day_change_readable(self, perct=False):

        # perct = percentage and time

        totaldaychange = sum([h.day_change() for h in self.holdings])
        rounded = round(totaldaychange, 2)

        # Total Day Change Readable

        tdcr = '$%s' % rounded
        percent = '%s%%' % round(percentage(rounded, p.total_value() - rounded), 2)
        if perct == False:
            return tdcr
        elif perct == True:
            return percent
        else:
            return 'what?'

    def total_change(self):
        totalchange = sum([h.total_change() for h in self.holdings])
        return totalchange

    def total_change_readable(self, perct=False):

        # perct = percentage and time

        totalchange = sum([h.total_change() for h in self.holdings])
        rounded = round(totalchange, 2)

        # Total Change Readable

        tcr = '$%s' % rounded
        percent = '%s%%' % round(percentage(rounded, p.total_value() - rounded), 2)
        if perct == False:
            return tcr
        elif perct == True:
            return percent
        else:
            return 'what?'

    def update(self):
        google_data = getQuotes(['GLUU', 'LLNW', 'HACK'])
        for i in range(0,3):
            self.holdings[i].update(google_data[i])

    def quote(self, symbol):
        return float(self.holdings[symbol].price)

# All holdings

p = Portfolio()
p.addHolding(Holding('GLUU', 110, 5.055))
p.addHolding(Holding('LLNW', 109, 4.1))
p.addHolding(Holding('HACK', 16, 29.9099))
p.update()
print p.quote(GLUU)
print p.total_day_change_readable(perct=True)
print p.total_day_change_readable()
print p.total_change_readable(perct=True)
print p.total_change_readable()


# print getQuotes(['GLUU', 'LLNW', 'HACK'])[0]['LastTradePrice']

# print json.dumps(getQuotes(['GLUU', 'LLNW', 'HACK']), indent=2)