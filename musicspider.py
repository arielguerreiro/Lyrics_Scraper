#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:27:45 2020

@author: ariel
"""
#reminder: scrapy runspider <name>
import scrapy 
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        pass
        

class MusicSpider(scrapy.Spider):
    name = 'music spider'
    
    def start_requests(self):
        start_urls = ['https://www.letras.mus.br/simon-e-garfunkel/']
        for url in start_urls:
            yield scrapy.Request(url = url, callback = self.parse_links)
            
    def parse_links(self, response):
        links = response.css('ol.cnt-list.cnt-list--num > li.cnt-list-row::attr(data-shareurl)').extract()
        f1 = open('links.txt', 'w')
        f1.write(str(links))
        for link in links:
            yield scrapy.Request(url = link, callback= self.parse_music)
            
    def parse_music(self, response):
        song_name = response.css('div.cnt-head_title > h1::text').extract_first()
        song_file_name = song_name.replace(' ', '_')
        song_file_name = song_file_name.replace('.', '_')
        song_file_name = song_file_name.replace('/', '_')
        
        artist_name = response.css('div.cnt-head_title > h2 > a::text').extract_first()
        createFolder('./{}/'.format(artist_name))
        
        lyrics = response.css('div.cnt-letra.p402_premium ::text').extract()
        
        
        filepath = './{}/{}.txt'.format(artist_name, song_file_name)
        f = open(filepath, 'w')
        f.write('{} : {} \n\n'.format(artist_name, song_name))
        for i in range(len(lyrics)):
            f.write('{}\n'.format(lyrics[i]))
        f.close()