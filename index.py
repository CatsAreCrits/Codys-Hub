#!/usr/bin/python
# -*- coding: utf-8 -*-

# INDEX.PY - Created 5/21/2015
# Includes code made for the WEBSITE ONLY, test things in stock.py

import json
import time
import threading
import os
from bottle import route, run, template
from googlefinance import getQuotes
from yahoo_finance import Share


# Portfolio Tracker 
# Last Updated.. idk
# Cody Morton

# How to get quote: quote = json.dumps(getQuotes('AAPL'), indent=2)
# How to get specific thing from quote: print getQuotes('AAP')[0]['LastTradePrice']

# c = Commission
# Change this to whatever your commission from your broker is..

c = 9.99


# Misc Functions
# Returns percentage

def percentage(part, whole):
	return 100 * float(part) / float(whole)


# Returns current date

def date():
	dater = time.strftime('%m/%d/%Y')
	return dater


	# threading.Timer(60, date).start()

class Holding:

	"""Get value, Get day change, Get total change, Store holdings"""

	def __init__(self, symbol, shares, price_paid):

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

# Updates the prices for each holding

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

	def total_true_change(self, perct=False):
		trueChangeV = p.total_value() - 1200

		rounded = round(trueChangeV, 2)

		# Total True Change Readable
		ttcr = '$%s' % rounded
		percentT = '%s%%' % round(percentage(rounded, p.total_value()), 2)
		if perct == False:
			return ttcr
		elif perct == True:
			return percentT
		else:
			return 'what?'

# Gets the update for each holding.. edit the list with your symbol(s)
	def update(self):
		google_data = getQuotes(['GLUU', 'BGMD', 'BGMD', 'HACK'])

		# Make this the range for your stocks. If you have 5 stocks the range is 0,5

		for i in range(0, 4):
			self.holdings[i].update(google_data[i])

# Returns the share price of a stock.

	def quote(self, symbol):
		return float(self.holdings[symbol].price)


# All holdings

p = Portfolio()
p.addHolding(Holding('GLUU', 110, 5.055))
p.addHolding(Holding('BGMD', 100, 2.8492))
p.addHolding(Holding('BGMD', 50, 2.84))
p.addHolding(Holding('HACK', 16, 29.9099))
p.update()

# Loan Tracker
# Last Updated.. 7/12/2015
# Cody Morton
import praw
from operator import itemgetter

r = praw.Reddit(user_agent='Codys_Loan_Tracker')
submissions = r.get_subreddit('borrow').get_new(limit=7)
list = [str(x) for x in submissions]
# print '\n'.join(list)
list1 = itemgetter(0)(list)
list2 = itemgetter(1)(list)
list3 = itemgetter(2)(list)
list4 = itemgetter(3)(list)
list5 = itemgetter(4)(list)
list6 = itemgetter(5)(list)
list7 = itemgetter(6)(list)

# Run the site

@route('/')
def index():
	main_dict = {
		'holdings': p.total_value_readable(),
		'day_change_percent': p.total_day_change_readable(perct=True),
		'day_change_dollar': p.total_day_change_readable(),
		'total_change_percent': p.total_true_change(perct=True),
		'total_change_dollar': p.total_true_change(),
		'date': date(),
		'gluu_q': getQuotes('GLUU')[0]['LastTradePrice'],
		'hack_q': getQuotes('HACK')[0]['LastTradePrice'],
		'bgmd_q': getQuotes('BGMD')[0]['LastTradePrice'],
		'list1': list1,
		'list2': list2,
		'list3': list3,
		'list4': list4,
		'list5': list5,
		'list6': list6,
		'list7': list7
		}
	p.update()
	return template('index', **main_dict)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 8080))
	run(host='0.0.0.0', port=port, debug=True, server='cherrypy')
