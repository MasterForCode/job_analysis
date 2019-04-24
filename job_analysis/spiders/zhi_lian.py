# -*- coding: utf-8 -*-
import json

import math
import scrapy

from job_analysis.items import JobAnalysisItem


class ZhiLianSpider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {
            'job_analysis.pipelines.ZhiLianPipeline': 300,
        }
    }
    name = 'zhi_lian'
    allowed_domains = ['fe-api.zhaopin.com']
    page_size = 90
    base_url = 'https://fe-api.zhaopin.com/c/i/sou?'
    middle_url = 'pageSize=' + str(page_size)
    sub_fix = '&cityId=635&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3'
    start_urls = [base_url + middle_url + sub_fix]
    first = True
    index = 1

    def parse(self, response):
        data = json.loads(response.body, encoding='utf-8')['data']
        num_found = data['numFound']
        if ZhiLianSpider.first:
            for x in range(2, math.floor(num_found / 20) + 1, 1):
                with open('./t.text', 'w') as file:
                    file.write(str(x))
                ZhiLianSpider.first = False
                yield scrapy.Request(
                    ZhiLianSpider.base_url + 'start=' + str(
                        ZhiLianSpider.page_size + 20 * x) + 'pageSize=20' + ZhiLianSpider.sub_fix,
                    callback=self.parse, dont_filter=True)
        results = data['results']
        for each in results:
            item = JobAnalysisItem()
            # 工资
            item['salary'] = each['salary']
            # 招聘公司
            item['company'] = each['company']['name']
            # 工作地点
            item['work_addr'] = each['city']['display']
            # 工作年限
            item['work_year'] = each['workingExp']['name']
            # 学历
            item['education'] = each['eduLevel']['name']
            # 行业
            item['state'] = each['company']['type']['name']
            # 公司规模
            item['company_size'] = each['company']['size']['name']
            # 最后修改时间
            item['modify_time'] = each['updateDate']
            # 福利
            item['welfare'] = each['welfare']
            yield item
