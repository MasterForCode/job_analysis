# -*- coding: utf-8 -*-
import json
from random import choice

import requests


class MyProxy(object):
    get_proxy_url = 'http://api.faceme.site/proxy/'

    def round_http_proxy(self):
        return choice(self.get_proxy()[0])

    def round_https_proxy(self):
        return choice(self.get_proxy()[1])

    def get_proxy(self):
        response = requests.get(MyProxy.get_proxy_url)
        result = json.loads(response.content)
        http_proxy = []
        https_proxy = []
        if result['code'] == 200:
            for each in result['data']:
                if 'http' in each['scheme']:
                    http_proxy.append(each['proxy'])
                if 'https' in each['scheme']:
                    https_proxy.append(each['proxy'])
        else:
            print('未获取到免费代理')
        return http_proxy, https_proxy
