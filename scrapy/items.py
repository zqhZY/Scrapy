import scrapy

class SqlTestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	title = scrapy.Field()
	link = scrapy.Field()

	url = scrapy.Field()
	
	pass
	