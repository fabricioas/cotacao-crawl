# -*- coding: utf-8 -*-
import scrapy
import json

class CotacaoSpider(scrapy.Spider):
    name = 'cotacao'
    start_urls = ['file:///home/fabricio/git/cotacao-crawl/siglas.json']

    def parse(self, response):
        siglas = json.loads(response.body)
        for s in siglas:
            yield response.follow("http://cotacao.b3.com.br/mds/api/v1/DailyFluctuationHistory/"+ s['sigla'], self.parse_dados)

    def parse_dados(self, response):
        dados = json.loads(response.body)
        cotacao = dados['TradgFlr']['scty']['lstQtn'][-1]
        sigla = dados['TradgFlr']['scty']['symb']
        cotacao['sigla'] = sigla
        yield cotacao
        
