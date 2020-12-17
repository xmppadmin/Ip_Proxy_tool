#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:  Analyst1981@gmail.com
# @date:    2019-3-16

import time
from multiprocessing import Process
from api import app
from getter import Getter
from tester import Tester
from db import MysqlClient
from setting import *


class Scheduler():
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        Timed test agent
        """
        tester = Tester()
        while True:
            print('Tester starts running')
            logger.log('INFOR', 'Tester starts running...')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        Get the agent regularly
        """
        getter = Getter()
        while True:
            print('Start to grab the proxy')
            logger.log('INFOR', 'Start to Grab the proxy...')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        """
        Open API
        """
        logger.log('INFOR', 'Activate API...')
        app.run(API_HOST, API_PORT)
 
    def run(self):
        print('Agent pool starts running')
        logger.log('INFOR', 'Scheduler starts running...')
        mysql=MysqlClient()
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()
        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()
        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()
    

if __name__ == '__main__':
    s=Scheduler()
    s.run()
