# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class UsdaItem(Item):
    symbol = Field()
    group = Field()
    family = Field()
    scientific_name = Field() 
    common_name = Field()