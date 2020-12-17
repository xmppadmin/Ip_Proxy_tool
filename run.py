#!/usr/bin/python
# -*- coding: utf-8 -*-
from scheduler import Scheduler
import sys
import io
from setting import *
from loguru import logger
from datetime import datetime


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') 

def main():
    try:
        # The default log file level is DEBUG
        logger.add(log_path, level='DEBUG', format=logfile_fmt, enqueue=True, encoding='utf-8', rotation="20 MB")
        logger.log('INFOR', 'Starting ip_proxy_tool')
        s = Scheduler()
        s.run()
    except:
        main()


if __name__ == '__main__':
    main()
