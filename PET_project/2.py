# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 18:09:28 2017

@author: Tanichka
"""


import time
import requests
import lxml.html

class facebookParser:
#    получили корневой елемент Html дерева - <Element html at 0x2321ff0b098>
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
        print(html_tree)
    
    def run(self):
        pass
if __name__ == "__main__":
    
    parser = facebookParser('https://www.facebook.com/elephantodessa')
    page = parser.get_page()
    parser.parser(page)
