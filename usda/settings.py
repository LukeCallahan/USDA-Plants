# Scrapy settings for usda project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'usda'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['usda.spiders']
NEWSPIDER_MODULE = 'usda.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)


HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 60 * 60 * 24 * 7 * 2
