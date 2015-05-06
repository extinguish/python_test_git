# demonstrate the usage of the scrapy to get all of the 
# BT information
import scrapy

class TorrentItem(scrapy.Item):
	url = scrapy.Field()
	name = scrapy.Field()
	description = scrapy.Field()
	size = scrapy.Field()
