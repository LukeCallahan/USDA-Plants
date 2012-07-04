from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from usda.items import UsdaItem

class UsdaSpider(CrawlSpider):
	name = "usda"
	allowed_domains = ["plants.usda.gov"]
	start_urls = [
		"http://plants.usda.gov/java/imageGallery?txtparm=&category=sciname&familycategory=all&duration=all&growthhabit=all&nativestatus=all&wetland=all&artist=all&copyright=nocopyright&imagetype=all&cite=all&location=all&viewsort=text&sort=sciname&submit2.x=50&submit2.y=11"
	]
	
	
	#start link follow rules
	
	rules = [
	
	
		Rule(SgmlLinkExtractor(allow=(r'/java/profile\?symbol=[A-Z0-9]+$'), restrict_xpaths = ('//table[@summary="PLANTS Name Search Results"]')))
		]

	
#	def parse(self, response):
# 		filename = response.url.split("/")[-2]
# 		open(filename, 'wb').write(response.body)


	def parse_item(self, response):		
		hxs = HtmlXPathSelector(response)
		item  = UsdaItem()
		item['symbol'] = hxs.select('//td[starts-with(.,"Symbol:")]/following-sibling::td[@class="search"]/text()').extract()
		item['group'] = hxs.select('//td[starts-with(.,"Group:")]/following-sibling::td[@class="search"]/text()').extract()
		item['family'] = hxs.select('//td[starts-with(.,"Family:")]/following-sibling::td[@class="search"]/text()').extract()
		
		
		
		return item
		
		
		# tutorial on scrapy
# def parse_item(self, response):
#         self.log('Hi, this is an item page! %s' % response.url)
# 
#         hxs = HtmlXPathSelector(response)
#         item = Item()
#         item['id'] = hxs.select('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
#         item['name'] = hxs.select('//td[@id="item_name"]/text()').extract()
#         item['description'] = hxs.select('//td[@id="item_description"]/text()').extract()
#         return item