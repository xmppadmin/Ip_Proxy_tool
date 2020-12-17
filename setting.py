#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:  Analyst1981@gmail.com
# @date:    2019-3-16

from loguru import logger

# # Database address
MYSQL_HOST = '127.0.0.1'

# Port
MYSQL_PORT = 3306
MYSQL_PASSWORD = 'toor'
MYSQL_USER='root'

MYSQL_DB='spiders'
MYSQL_TABLE='ProxyComment'

# Proxy score
MAX_SCORE = 100
MIN_SCORE = 5
INITIAL_SCORE = 10

VALID_STATUS_CODES = [200, 302]

# Proxy pool number limit
POOL_UPPER_THRESHOLD = 10000

# inspection cycle
TESTER_CYCLE = 20
# Get cycle
GETTER_CYCLE = 300

# Test API, which website is recommended to test which
TEST_URL = 'https://www.google.com'

# API configuration
API_HOST = '127.0.0.1'
API_PORT = 5555

# Scheduler Switch
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# Maximum batch test volume
BATCH_TEST_SIZE = 50

yellow = '\033[01;33m'
white = '\033[01;37m'
green = '\033[01;32m'
blue = '\033[01;34m'
red = '\033[1;31m'
end = '\033[0m'

#log path
log_path = 'ip_proxy_tool.log'  #  log save path

# Log file record format
logfile_fmt = '<light-green>{time:YYYY-MM-DD HH:mm:ss,SSS}</light-green> ' \
              '[<level>{level: <5}</level>] ' \
              '<cyan>{process.name}({process.id})</cyan>:' \
              '<cyan>{thread.name: <18}({thread.id: <5})</cyan> | ' \
              '<blue>{module}</blue>.<blue>{function}</blue>:' \
              '<blue>{line}</blue> - <level>{message}</level>'

# define Log levels
logger.remove()
logger.level(name='TRACE', color='<cyan><bold>', icon='✏️')
logger.level(name='DEBUG', color='<blue><bold>', icon='🐞 ')
logger.level(name='INFOR', no=20, color='<green><bold>', icon='ℹ️')
logger.level(name='QUITE', no=25, color='<green><bold>', icon='🤫 ')
logger.level(name='ALERT', no=30, color='<yellow><bold>', icon='⚠️')
logger.level(name='ERROR', color='<red><bold>', icon='❌')
logger.level(name='FATAL', no=50, color='<RED><bold>', icon='☠️')
