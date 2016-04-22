#-*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from sql_test.items import SqlTestItem
from scrapy.http import Request

class bookSpider(Spider):

	name = "yamaxun"
	allow_domains = ["http://www.amazon.cn"]

	start_urls = ["http://www.amazon.cn/s/ref=nb_sb_noss?__mk_zh_CN=亚马逊网站&url=search-alias%3Daps&field-keywords=计算机考研"]


	def parse_back(self , response):

		items = []

		item = SqlTestItem()
		
		item['title'] = response.selector.xpath('//ul/li[position()>0]/div[1]/div[2]/div[1]/a/@title').extract()
		item['link'] = response.selector.xpath('//ul/li[position()>0]/div[1]/div[2]/div[1]/a/@href').extract()

#item['link'] = response.selector.xpath('//span[@class = "pagnLink"]/a/@href').extract()
		items.append(item)

		return items

	def parse(self , response):

		items = []
		
		urls = response.selector.xpath('//span[@class = "pagnLink"]/a/@href').extract()
	
		print urls

		next_links = []
		for url in urls:
			url = 'http://www.amazon.cn' + url
			next_links.append(url)


		for url in next_links:
			yield Request(url , callback = self.parse_back)


