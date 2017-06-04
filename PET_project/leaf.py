# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 23:08:12 2017

@author: Tanichka
"""


import time
import requests
import lxml.html

class leafParser:
#    получение страницы - Первый этап
    def __init__(self, base_url):
        self.base_url = base_url
        self.last_time = ''
        
    def get_page(self):
        try:
            res = requests.get(self.base_url)
        except requests.ConnectionError:
            return
        if res.status_code<400:
            return res.content
    
    def parser(self, html):
        html_tree = lxml.html.fromstring(html)
        path=".//div[@class='bxslider']"
        last_offer = html_tree.xpath(path)
        print(last_offer)
        
        name = last_offer.xpath('.//div[@class="carousel-block"]')
        print(name)
    
    def run(self):
        pass
    
if __name__ == "__main__":
    
    parser = leafParser('http://leaf.elephant-odessa.com/')
    page = parser.get_page()
    parser.parser(page)
