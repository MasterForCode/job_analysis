# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobAnalysisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位
    job_name = scrapy.Field()
    # 工资
    salary = scrapy.Field()
    # 招聘公司
    company = scrapy.Field()
    # 工作地点
    work_addr = scrapy.Field()
    # 工作年限
    work_year = scrapy.Field()
    # 学历
    education = scrapy.Field()
    # 公司规模
    company_size = scrapy.Field()
    # 公司状况
    state = scrapy.Field()
    # 最后修改时间
    modify_time = scrapy.Field()
    # 福利
    welfare = scrapy.Field()
    pass
