# -*- coding: utf-8 -*-
import scrapy
import json


class B3Spider(scrapy.Spider):
    name = 'b3'
    start_urls = ['http://cotacao.b3.com.br/mds/api/v1/DailyFluctuationHistory/EMAE4']

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        list = jsonresponse['TradgFlr']['scty']['lstQtn']
        lastItem = list[-1] #seleciona o ultimo valor
        return lastItem
