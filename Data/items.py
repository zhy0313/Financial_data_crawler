# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DataItem(scrapy.Item):
    web_name = scrapy.Field()              # 网站名  用以插入数据库时区分，不实际进入数据库

    time = scrapy.Field()                  # 时间

    deliverymonth = scrapy.Field()         # 交割月份

    presettlementprice = scrapy.Field()    # 前结算

    closeprice = scrapy.Field()            # 收盘价

    highestprice = scrapy.Field()          # 最高价

    lowestprice = scrapy.Field()           # 最低价

    openinterest = scrapy.Field()          # 持仓手

    openinterestchg = scrapy.Field()       # 持仓变化

    openprice = scrapy.Field()             # 今开盘

    productname = scrapy.Field()           # 商品名称

    settlementprice = scrapy.Field()       # 今结算参考价

    volume = scrapy.Field()                # 成交手

    zd1_chg = scrapy.Field()               # 涨跌1
    zd2_chg = scrapy.Field()               # 涨跌2

    deliverynum = scrapy.Field()           # 交收量

    deliverypoint = scrapy.Field()         # 交收方向

    deliveryprice = scrapy.Field()         # 交割结算价

    turnover = scrapy.Field()              # 成交额

    averageprice = scrapy.Field()          # 均价