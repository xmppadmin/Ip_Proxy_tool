#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:  Analyst1981@gmail.com
# @date:    2019-3-16

import asyncio
import aiohttp
import time
import sys
try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError
from db import MysqlClient
from setting import *


class Tester(object):
    def __init__(self):
        self.Mysql = MysqlClient()
    
    async def test_single_proxy(self, proxy):
        """
        :Test a single agent
        :param proxy:
        :return:
        """
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                #print(proxy)
                #logger.log('DEBUG', f' Proxy : {proxy} ')                
                # print("============ Test Single Proxy ==",proxy[0],proxy[1],proxy[2])
                # logger.log('DEBUG', f' Test Single Proxy : {proxy[0]} - {proxy[1]} - {proxy[2]}  ====')
                # real proxy = ip : port
                real_proxy ="http://{0}:{1}".format(proxy[0],proxy[1])
                print(real_proxy)
                # print('Testing', proxy)
                # logger.log('DEBUG', f' Testing proxy : {real_proxy} ')
                async with session.get(TEST_URL, proxy=real_proxy, timeout=15, allow_redirects=False) as response:
                    if response.status in VALID_STATUS_CODES:
                        self.Mysql.max_(proxy)
                        print('Proxy is available', proxy)
                    else:
                        self.Mysql.decrease(proxy)
                        print('Request response code is invalid', response.status, 'IP', proxy)
            except (ClientError, aiohttp.client_exceptions.ClientConnectorError, asyncio.TimeoutError, AttributeError):
                self.Mysql.decrease(proxy)
                print('Proxy request failed', proxy)

    def run(self):
        """
        Test the main function
        :return:
        """
        print('Tester starts running')
        try:
            count = self.Mysql.count()
            print('Currently remaining', count, 'Agent')
            logger.log('DEBUG', f' Currently remaining : {count}  Agent')
            for i in range(0, count, BATCH_TEST_SIZE):
                start = i
                stop = min(i + BATCH_TEST_SIZE, count)
                print('Testing the first', start + 1, '-', stop, 'agent')
                logger.log('DEBUG', f' Testing the first : {start+1} - {stop} Agent ')
                # get all proxies from start to stop from the DB
                test_proxies =list(self.Mysql.batch(start,stop))
                #print(test_proxies,type(test_proxies))
                loop = asyncio.get_event_loop()
                # test each proxy in test_proxies
                tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                sys.stdout.flush()
                time.sleep(5)
        except Exception as e:
            print('An error occurred in the tester', e.args)
