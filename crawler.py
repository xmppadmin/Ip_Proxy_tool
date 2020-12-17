#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:  Analyst1981@gmail.com
# @date:    2019-3-16

import json
import re
from utils import get_page
from bs4 import BeautifulSoup
from setting import *
from lxml.html import fromstring
import requests


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            logger.log('DEBUG', f' In proxyMetaclass k : {k}  v: {v} ====')
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        logger.log('INFOR', 'Start Crawler======')
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('Successfully obtained proxy', proxy)
            proxies.append(proxy)
        return proxies


    def crawl_free_proxy_list(self):
        print("===================== get free proxy list ==============")
        logger.log('INFOR', 'Start collecting proxies from https://free-proxy-list.net/')
        proxy=[]
        start_url = 'https://free-proxy-list.net/'
        html = get_page(start_url)
        soup = BeautifulSoup(html, 'lxml')
        trs=soup.find("tbody").find_all("tr")
        for tr in trs:
               IP= tr.find_all("td")[0].get_text()
               PORT = tr.find_all("td")[1].get_text()
               proxy_type = tr.find_all("td")[6].get_text()
               if proxy_type == "yes":
                  TYPE = "https"
               else:
                  TYPE = "http"
               proxy.append([IP,PORT,TYPE])
        logger.log('DEBUG', f'Total of {len(proxy)}  proxies collected')
        return proxy


    def crawl_hidemy_name_list(self):
        # select hppts supported proxies with high Anonymity level
        print("===================== get hidemy.name proxy list ==============")
        logger.log('INFOR', 'Start collecting proxies from https://hidemy.name/en/proxy-list/?type=s&anon=4#list')
        proxy=[]
        start_url = 'https://hidemy.name/en/proxy-list/?type=s&anon=4#list'
        html = get_page(start_url)
        soup = BeautifulSoup(html, 'lxml')
        trs=soup.find("tbody").find_all("tr")
        for tr in trs:
               IP= tr.find_all("td")[0].get_text()
               PORT = tr.find_all("td")[1].get_text()
               TYPE = "https"
               proxy.append([IP,PORT,TYPE])
        logger.log('DEBUG', f'Total of {len(proxy)}  proxies collected')
        return proxy

    def crawl_daili66(self, page_count=34):
        print("=============== Get www.66ip.cn ===========")
        logger.log('INFOR', 'Start collecting proxies from http://www.66ip.cn/')
        proxy=[]
        start_url = "http://www.66ip.cn/areaindex_{}/1.html"
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                soup = BeautifulSoup(html.decode("gbk"), 'lxml')
                trs=soup.find("div",class_="containerbox boxindex").find_all("tr")
                for tr in trs[1:]:
                    IP= tr.find_all("td")[0].get_text()
                    PORT = tr.find_all("td")[1].get_text()
                    TYPE = "http"
                    proxy.append([IP,PORT,TYPE])
        logger.log('DEBUG', f'Total of {len(proxy)}  proxies collected')
        return proxy

    def crawl_kuaidaili(self):
        print("=============== Get www.kuaidaili.com  ===========")
        logger.log('INFOR', 'Start collecting proxies from http://www.kuaidaili.com/')
        proxy=[]
        for i in range(1, 4):
            start_url = 'http://www.kuaidaili.com/free/inha/{}/'.format(i)
            html = get_page(start_url)
            if html:
                soup = BeautifulSoup(html, 'lxml')
                trs=soup.find("div",class_="con-body").find_all("tr")
                for tr in trs[1:]:
                    IP = tr.find_all("td")[0].get_text()
                    PORT = tr.find_all("td")[1].get_text()
                    iptype =tr.find_all("td")[3].get_text().lower()
                    proxy.append([IP,PORT,iptype])
        logger.log('DEBUG', f'Total of {len(proxy)}  proxies collected')
        return proxy

    def crawl_xicidaili(self):
        print("=============== Get www.xicidaili.com  ===========")
        logger.log('INFOR', 'Start collecting proxies from http://www.xicidaili.com/')
        proxy=[]
        for i in range(1, 3):
            start_url = 'http://www.xicidaili.com/nn/{}'.format(i)
            headers = {
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Cookie':'_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWRjYzc5MmM1MTBiMDMzYTUzNTZjNzA4NjBhNWRjZjliBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUp6S2tXT3g5a0FCT01ndzlmWWZqRVJNek1WanRuUDBCbTJUN21GMTBKd3M9BjsARg%3D%3D--2a69429cb2115c6a0cc9a86e0ebe2800c0d471b3',
                'Host':'www.xicidaili.com',
                'Referer':'http://www.xicidaili.com/nn/3',
                'Upgrade-Insecure-Requests':'1',
            }
            html = get_page(start_url, options=headers)
            if html:
                soup = BeautifulSoup(html, 'lxml')
                trs=soup.find("table",id="ip_list").find_all("tr")
                for tr in trs[1:]:
                    IP = tr.find_all("td")[1].get_text()
                    PORT = tr.find_all("td")[2].get_text()
                    iptype =tr.find_all("td")[5].get_text().lower()
                    proxy.append([IP,PORT,iptype])
        logger.log('DEBUG', f'Total of {len(proxy)}  proxies collected')
        return proxy
 
    def crawl_ip3366(self):
        print("=============== Get www.ip3366.net  ===========")
        logger.log('INFOR', 'Start collecting proxies from http://www.ip3366.net/')
        proxy=[]
        for i in range(1, 4):
            start_url = 'http://www.ip3366.net/?stype=1&page={}'.format(i)
            html = get_page(start_url)
            if html:
                soup = BeautifulSoup(html, 'lxml')
                trs=soup.find("div",id="container").find_all("tr")
                for tr in trs[1:]:
                    IP = tr.find_all("td")[0].get_text()
                    PORT= tr.find_all("td")[1].get_text()
                    iptype =tr.find_all("td")[3].get_text()
                    proxy.append([IP,PORT,iptype])
        logger.log('DEBUG', f'Total of {len(proxy)}  proxies collected')
        return proxy

    def crawl_iphai(self):
        print("=============== Get www.iphai.com  ===========")
        logger.log('INFOR', 'Start collecting proxies from http://www.iphai.com /')
        proxy=[]
        for start_url in ['http://www.iphai.com/free/wg','http://www.iphai.com/free/ng','http://www.iphai.com/free/np','http://www.iphai.com/free/wp']:
            html = get_page(start_url)
            if html:
                soup = BeautifulSoup(html, 'lxml')
                trs=soup.find("div",class_="container main-container").find_all("tr")
                for tr in trs[1:]:
                    IP = tr.find_all("td")[0].get_text().replace(' ','').replace('\n','').replace('\r','')
                    PORT = tr.find_all("td")[1].get_text().replace(' ','').replace('\n','').replace('\r','')
                    iptype =tr.find_all("td")[3].get_text().replace(' ','').replace('\n','').replace('\r','').lower()
                    proxy.append([IP,PORT,iptype])
        logger.log('DEBUG', f'Total of {len(proxy)}  proxies collected')
        return proxy
    
    def crawl_ippastebin(self):
        print("=============== Get pastebin.com/u/spys1  ===========")
        logger.log('INFOR', 'Start collecting proxies from http://pastebin.com/u/spys1')
        proxy=[]
        proxy_=[]
        start_url='https://pastebin.com/u/spys1'
        html = get_page(start_url)
        page_soup = []
        page_soup.append(BeautifulSoup(html, 'lxml'))
        for i in page_soup:
            link = (i.td.a['href'])
            pastebin_url = 'https://pastebin.com'+link
            page_s = []
            r = get_page(pastebin_url)
            page_s.append(BeautifulSoup(r,'lxml'))
            for s in page_s:
                for i in s.find_all('div',class_='de1'):
                    proxies = i.text
                    proxy_.append(proxies)
            for p in proxy_[1:]:
                proxies = p.rsplit(' ',-1)[0].replace(' ','')
                IP=proxies.split(':')[0]
                PORT=proxies.split(':')[1]
                proxy.append([IP,PORT,'http'])
        logger.log('DEBUG', f'Total of {len(proxy)}  proxies collected')
        return proxy

