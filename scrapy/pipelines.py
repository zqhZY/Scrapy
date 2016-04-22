# -*- coding: utf-8 -*-

from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
import time
import MySQLdb
import MySQLdb.cursors
import socket
import select
import sys
import os
import errno


class SqlTestPipeline(object):
	def __init__(self):
		self.dbpool = adbapi.ConnectionPool('MySQLdb', db = 'spide_save',  user = 'root', passwd = 'zqh',cursorclass = MySQLdb.cursors.DictCursor,charset = 'utf8',use_unicode = False)
		
	def process_item(self, item, spider):
		
		query = self.dbpool.runInteraction(self._conditional_insert, item)
		return item
	def _conditional_insert(self, tx, item):
		if item.get('title'):
			for i in range(len(item['title'])):
				tx.execute('insert into book values (%s, %s)', (item['title'][i], item['link'][i]))

				