# -*- coding: utf-8 -*-
import scrapy
from dpCrawl.items import DpcrawlItem
from scrapy.selector import Selector
from scrapy.http.request import Request

class DpcrawlSpider(scrapy.Spider):
    name = "dpcrawl"
    allowed_domains = ["dianping.com"]
    # 分析注册时间从2014-01-01 开始的用户
    start_urls = ['http://www.dianping.com/member/' + str(i) for i in range(50100000, 70000000)]
    # start_urls = ['http://www.dianping.com/member/8976']

    def start_requests(self):
        cookie = {'cye':"hangzhou"}
        for url in self.start_urls:
            yield Request(url, cookies=cookie)

    def parse(self, response):
        sel = Selector(response)
        item = DpcrawlItem()
        item['url'] = response.url
        item['userId'] = response.url.split('/')[-1]
        item['userName'] = sel.xpath('//div[@class="tit"]/h2/text()').extract_first()
        # 是否是vip
        if sel.xpath('//div[@class="vip"]/a/@title').extract_first():
            item['vip'] = 1
        else:
            item['vip'] = 0

        # 贡献值
        item['contribution'] = sel.xpath('//div[@class="user-info col-exp"]/span[1]/@title').extract_first()[3:]
        #性别
        if sel.xpath('//div[@class="user-info col-exp"]/span[2]/i').extract_first():
            item['gender'] = sel.xpath('//div[@class="user-info col-exp"]/span[2]/i/@class').extract_first()
        else:
            item['gender'] = None
        #用户所在地
        item['location'] = sel.xpath('//div[@class="user-info col-exp"]/span[2]/text()').extract_first()
        #点评数、收藏、签到、图片、帖子
        totalList = sel.xpath('//div[@class="nav"]/ul/li/a/text()').extract()
        _, dpNum, collectNum, checkNum, imgNum, _, post = totalList
        item['dpNum'] = dpNum[3:-1]
        item['collectNum'] = collectNum[3:-1]
        item['checkNum'] = checkNum[3:-1]
        item['imgNum'] = imgNum[3:-1]
        item['post'] = post[3:-1]
        #关注、粉丝
        item['attention'], item['fans'] = sel.xpath('//div[@class="user_atten"]/ul/li/a/strong/text()').extract()
        #互动
        item['interactiveNum'] = sel.xpath('//div[@class="user_atten"]/ul/li/strong/text()').extract_first()
        #社区等级、注册时间
        item['level'], item['registerTime'] = sel.xpath('//div[@class="user-time"]/p/text()').extract()
        #更多个人信息
        infos = sel.xpath('//div[@id="J_UMoreInfoD"]/ul/li')
        # moreInfo = {}
        keys = list()
        values = list()
        if len(infos) > 0:
            for info in infos:
                keys.append(info.xpath('em/text()').extract_first())
                values.append(info.xpath('text()').extract_first())
            moreInfo = dict(zip(keys, values))
            if '生日：' in moreInfo.keys():
                item['birthday'] = moreInfo['生日：']
            # else:
            #     item['birthday'] = None
            if '星座：' in moreInfo.keys():
                item['constellation'] = moreInfo['星座：']
            # else:
            #     item['constellation'] = None
            if '恋爱状况：' in moreInfo.keys():
                item['love_situation'] = moreInfo['恋爱状况：']
            if '行业职业：' in moreInfo.keys():
                item['occupation'] = moreInfo['行业职业：']
            if '毕业大学：' in moreInfo.keys():
                item['university'] = moreInfo['毕业大学：']
            # else:
            #     item['love_situation'] = None
        else:
            item['birthday'] = None
            item['constellation'] = None
            item['love_situation'] = None
            item['occupation'] = None
            item['university'] = None
        return item