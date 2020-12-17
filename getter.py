#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:  Analyst1981@gmail.com
# @date:    2019-3-16

from tester import Tester
from db import MysqlClient
from crawler import Crawler
from setting import *
import sys

class Getter():
    def __init__(self):
        self.Mysql = MysqlClient()
        self.crawler = Crawler()
    
    def is_over_threshold(self):
        """
        Determine whether the agent pool limit has been reached
        """
        if self.Mysql.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False
    
    def run(self):
        print('Get the execution')
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                # Get an agent
                proxies = self.crawler.get_proxies(callback)
                sys.stdout.flush()
                for proxy in proxies:
                    if (self.Mysql.exists(proxy)):
                        pass
                    else:
                        print(proxy)
                        self.Mysql.add(proxy)
