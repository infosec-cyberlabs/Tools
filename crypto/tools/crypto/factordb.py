# -*- coding: utf-8 -*-
# @Author: caleb
# @Date:   2016-05-28 10:31:45
# @Last Modified by:   caleb
# @Last Modified time: 2016-05-28 11:14:43
from bs4 import BeautifulSoup
import requests

URL = 'http://factordb.com/'

class FactorDBException(Exception):
	def __init__(self):
		super(FactorDBException, self).__init__('Number not found in FactorDB')

def factor(number):
	r = requests.get(URL + 'index.php?query=' + str(number))
	html = r.text
	soup = BeautifulSoup(html, 'html.parser')
	table = soup.find_all('table')[1]
	row = table.find_all('tr')[2]
	cells = row.find_all('td')
	status = cells[0].string

	if status != 'FF':
		raise FactorDBException('Number not found in factordb!')

	pID = cells[2].find_all('a')[1]['href'].split('=')[1]
	qID = cells[2].find_all('a')[2]['href'].split('=')[1]
	p = getnum(pID)
	q = getnum(qID)

	return (p,q)

def getnum(ID):
	r = requests.get(URL + 'index.php?showid=' + ID)
	html = r.text
	soup = BeautifulSoup(html, 'html.parser')
	table = soup.find_all('table')[1]
	cells = table.find_all('tr')[2].find_all('td')
	number = cells[1].get_text().replace('\n', '')
	return int(number.strip())
