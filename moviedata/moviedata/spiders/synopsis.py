# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
import re
from lxml import html

class SynopsisSpider(scrapy.Spider):
    name = 'synopsis'
    allowed_domains = ['imdb.com']
    start_urls = ['http://imdb.com/']

    def start_requests(self):
        movies = pd.read_csv(r'C:\Learning\NLP\Document Similarity\codeGIT\data\ml-latest-small\movies.csv')
        for index,movie in movies[0:10].iterrows():
            yield scrapy.Request(url='http://www.imdb.com/title/tt{}'.format(movie['imdbId']),\
                                 callback=self.parse)

    def parse(self, response):
        extracts = response.css('#titleStoryLine > div:nth-child(3) > p::text').extract()
        storyline = extracts[0].replace('                ','')
        # response.xpath('//div[@id="titleStoryLine"]/div[1]/p/text()').extract_first()
        yield {
            'imdbId': re.search(r'tt\d+', response.url).group(),
            'storyLine': storyline
        }


