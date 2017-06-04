# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 18:28:49 2017

@author: Tanichka
"""

import time
import requests
import lxml.html

class facebookParser:
#    получение больше инфо
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
        path=".//div[@class='_1dwg _1w_m']"
        last_offer = html_tree.xpath(path)[0]
        print(last_offer.text_content())
        
        name = last_offer.xpath('.//div/div/div/div/div/div/div/h5')
        print(name)
    
    def run(self):
        pass
if __name__ == "__main__":
    
    parser = facebookParser('https://www.facebook.com/pg/elephantodessa/posts/')
    page = parser.get_page()
    parser.parser(page)
