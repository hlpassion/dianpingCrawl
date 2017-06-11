# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class DpcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()
    userId = Field()    #用户id
    userName = Field()  #用户名
    vip = Field()       #是否是vip
    contribution = Field()  # 贡献值
    gender = Field()  # 性别
    location = Field()  #用户所在地
    dpNum = Field()     #点评数
    collectNum = Field()    #收藏数
    checkNum = Field()  #签到数
    imgNum = Field()    #图片数
    post = Field()      #帖子数
    attention = Field() #关注数
    fans = Field()      #粉丝数
    interactiveNum = Field()    #互动次数
    level = Field()     #社区等级
    registerTime = Field()  #注册时间
    birthday = Field()      #生日
    constellation = Field() #星座
    love_situation = Field() #恋爱情况
    occupation = Field()        #职业
    university = Field()        #大学