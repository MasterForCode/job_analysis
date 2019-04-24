# -*- coding: utf-8 -*-
import re

import scrapy

from job_analysis.items import JobAnalysisItem


class QianChengSpider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {
            'job_analysis.pipelines.QianChengPipeline': 300,
        }
    }
    name = 'qian_cheng'
    allowed_domains = ['search.51job.com']
    base_url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,'
    page = 1
    last_url = '.html'
    start_urls = [base_url + str(page) + last_url]

    # /list/000000,000000,0000,00,9,99,java,2,2.html

    def parse(self, response):
        page_info = response.xpath('//*[@id="resultList"]/div[55]/div/div/div/span[1]').extract_first()
        page = int(re.findall(r"\d+\.?\d*", page_info, flags=0)[0])
        for x in range(2, page, 1):
            yield scrapy.Request(QianChengSpider.base_url + str(x) + QianChengSpider.last_url, callback=self.parse,
                                 dont_filter=True)
        results = response.xpath('//*[@id="resultList"]/div[@class="el"]')
        for data in results:
            item = JobAnalysisItem()
            item['jobName'] = data.xpath('./p/span/a/@title')
            # 工资
            item['salary'] = data.xpath('./span[3]')
            # 招聘公司
            item['company'] = data.xpath('./span/a/@title')
            # 工作地点
            item['work_addr'] = data.xpath('./span[2]')
            detail_url = data.xpath('./p/span/a/@href')
            yield scrapy.Request(url=detail_url, meta={'item': item}, callback=self.parse_detail, dont_filter=True)
            # # 工作年限
            # item['work_year'] = each['workingExp']['name']
            # # 学历
            # item['education'] = each['eduLevel']['name']
            # # 行业
            # item['state'] = each['company']['type']['name']
            # # 公司规模
            # item['company_size'] = each['company']['size']['name']
            # # 最后修改时间
            # item['modify_time'] = data.xpath('./span[4]')
            # # 福利
            # item['welfare'] = each['welfare']

        # pass

    def parse_detail(self, response):
        item = response.meta['item']
        response.xpath('/html/body/div[2]/div[2]/div[2]/div/p[1]/text()[1]')
