# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class JobAnalysisPipeline(object):
    def process_item(self, item, spider):
        return item


class ZhiLianPipeline(object):
    path = './results'
    file_name = 'zhi_lian.csv'
    index = 0

    def __init__(self):
        with open(os.path.join(self.path, self.file_name), 'w') as file:
            file.write('job_name,salary,company,work_addr,work_year,education,company_size,state,welfare,modify_time\r')

    def process_item(self, item, spider):
        self.index += 1
        print('总数:' + str(self.index))
        with open(os.path.join(self.path, self.file_name), 'a+', encoding='utf-8') as file:
            file.write(
                ','.join([item['job_name'], item['salary'], item['company'], item['work_addr'], item['work_year'],
                          item['education'], item['company_size'], item['state'],
                          '/'.join(item['welfare']), item['modify_time']]) + '\r')


class QianChengPipeline(object):
    path = './results'
    file_name = 'zhi_lian.csv'
    index = 0

    def __init__(self):
        with open(os.path.join(self.path, self.file_name), 'w') as file:
            file.write('salary,company,work_addr,work_year,education,company_size,state,welfare,modify_time\r')

    def process_item(self, item, spider):
        self.index += 1
        print('总数:' + str(self.index))
        with open(os.path.join(self.path, self.file_name), 'a+', encoding='utf-8') as file:
            file.write(
                ','.join([item['salary'], item['company'], item['work_addr'], item['work_year'], item['education'],
                          item['company_size'], item['state'], ','.join(item['welfare']) + item['modify_time']]) + '\r')
