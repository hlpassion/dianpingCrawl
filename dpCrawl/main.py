from scrapy import cmdline

import time

cmdline.execute("scrapy crawl dpcrawl -s CLOSESPIDER_ITEMCOUNT=500".split())