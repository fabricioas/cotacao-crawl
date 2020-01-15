# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = [
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=0&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=1&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=2&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=3&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=4&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=5&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=6&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=7&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=8&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=9&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=A&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=B&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=C&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=D&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=E&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=F&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=G&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=H&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=I&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=J&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=K&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=L&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=M&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=N&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=O&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=P&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=Q&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=R&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=S&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=T&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=U&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=V&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=W&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=X&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=Y&idioma=pt-BR',
    'http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/ResumoTitulosNegociaveis.aspx?or=bus&tip=I&cb=Z&idioma=pt-BR',]

    def parse(self, response):
        trList = response.xpath("//*[@id='ctl00_contentPlaceHolderConteudo_grdEmpresas_ctl01']/tbody/tr")
        for item in trList:
            link = item.xpath("td[1]/a/@href").get().strip()
            razao = item.xpath("td[1]/a/text()").get().strip()
            nome = item.xpath("td[2]/a/text()").get().strip()
            yield response.follow("http://bvmf.bmfbovespa.com.br/cias-listadas/Titulos-Negociaveis/" + link, self.parse_detail)

    def parse_detail(self, response):
        trList = response.xpath('//*[@id="ctl00_contentPlaceHolderConteudo_ctl00_grdDados_ctl01"]/tbody/tr')
        for item in trList:
            nome = item.xpath("td[1]/text()").get().strip()
            sigla = item.xpath("td[3]/text()").get().strip()
            yield {"nome": nome, "sigla":sigla}
