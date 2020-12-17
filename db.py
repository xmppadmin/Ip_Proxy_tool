#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:  Analyst1981@gmail.com
# @date:    2019-3-16

from setting import MYSQL_HOST, MYSQL_PORT, MYSQL_PASSWORD, MYSQL_USER,MYSQL_DB,MYSQL_TABLE
from setting import MAX_SCORE, MIN_SCORE, INITIAL_SCORE
from random import choice
import re
import pymysql
class MysqlClient(object):
    def __init__(self ):
        """
        Initialize the database MYSQL_HOST,MYSQL_USER,MYSQL_PORT, MYSQL_PASSWORD,MYSQL_DB
        """
        self.conn = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER,port=MYSQL_PORT, password=MYSQL_PASSWORD,database=MYSQL_DB,charset='utf8mb4')
        self.cursor = self.conn.cursor()

    def add(self,proxy,score=INITIAL_SCORE):
        """
        Add an agent, set the score to the highest
        :param proxy: proxy PROXY_IP,PROXY_PORT,PROXY_TYPE
        :param score: fraction
        :return: add results
        """

        sql='INSERT INTO ProxyComment(IP,PORT,TYPE,SCORE) VALUES (%s,%s,%s,%s)'
        try:
            #print(type(proxy))
            #print(proxy)
            self.cursor.execute(sql,(proxy[0],proxy[1],proxy[2],score))
            self.conn.commit()
        except Exception as e :
            print(e.args)
            print('Failed')
            self.conn.rollback() 

    def random(self):
        """
        Get a valid agent randomly, first try to get the highest score agent, if it does not exist, get it according to the ranking, otherwise abnormal
        :return: Random agent
        """
        sql='SELECT * FROM  ProxyComment WHERE SCORE ="100"'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            sql='SELECT * FROM ProxyComment ORDER BY SCORE DESC'
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if result:
                return result
            else:
                self.conn.rollback() 
                #raise PoolEmptyError
    def decrease(self,proxy):
        """
        Proxy value minus one point, delete if it is less than the minimum
        :param proxy: proxy proxy 
        :return: Modified proxy score
        """
        sql='SELECT SCORE FROM  ProxyComment WHERE IP=%s'
       
        self.cursor.execute(sql,(proxy[0]))
        score = self.cursor.fetchone()
#        if (score[0] == None and score[0]==0):
# ======================================
        # remove all proxies with scopre < MIN_SCORE
        if score[0] < MIN_SCORE:
            print('proxy', proxy, 'Previous score', score, 'Remove')
            sql='DELETE FROM ProxyComment WHERE IP=%s'
            self.cursor.execute(sql,(proxy[0]))
            self.conn.commit()
            return 
        elif score[0] > MIN_SCORE:
            print('proxy', proxy, 'Current score', score, 'Minus 1')
            sql='update ProxyComment set SCORE=SCORE-1 where IP=%s'
            self.cursor.execute(sql,(proxy[0]))
            self.conn.commit()
            return 

    def exists(self,proxy):
        """
        Determine if it exists
        :param proxy: proxy
        :return: does it exist
        """
        sql='SELECT * FROM ProxyComment where IP=%s'
        self.cursor.execute(sql,(proxy[0]))
        result = self.cursor.fetchall()
        if result:
           return  True
        else:
           return  False

    def max_(self,proxy):
        """
        Set proxy to MAX_SCORE
        :param proxy: proxy
        :return: Set result
        """
        print('proxy', proxy, 'Available, set to', MAX_SCORE)
        sql='update ProxyComment set SCORE= %s where IP=%s'
        #print(sql)
        self.cursor.execute(sql,(MAX_SCORE,proxy[0]))
        self.conn.commit()
        return 

    def count(self):
        """
        Acquired quantity
        :return: Quantity
        """
        sql='SELECT * FROM  ProxyComment'
        self.cursor.execute(sql)
        return  len(self.cursor.fetchall())
    
    def all(self):
        """
        Get all agents
        :return: List of all agents
        """
        sql='SELECT * FROM  ProxyComment'
        
        self.cursor.execute(sql)
        return self.cursor.fetchall()
       
    
    def batch(self,start,stop):
        """
        Batch acquisition
        select * from employee limit 3, 7; // Return lines 4-11
        :param start: Start index
        :param stop: End index
        :return: Proxy list
        """
        sql='SELECT * FROM  ProxyComment LIMIT %s,%s'
        #print(sql)
        self.cursor.execute(sql,(start,stop))
        #print(self.cursor.fetchall())
        #return len(self.cursor.fetchall())
        return self.cursor.fetchall()



    """
    def __del__(self):
        
        self.conn.close()
        self.cursor.close()
    """
"""
Create mysql object：

mysql_test = Mysql('192.168.232.128','3306','root','123456','iceny')
      Create table t1：

mysql_test.exec('create table t1 (id int auto_increment primary key,timestamp TIMESTAMP)')
      image.png

      Insert a piece of data into t1：
       
        if not re.match('\d+\.\d+\.\d+\.\d+\:\d+', proxy):
            print('The agent does not meet the specifications', proxy, 'throw away')
            return
    

mysql_test.exec('insert into t1 (id,timestamp) value (NULL,CURRENT_TIMESTAMP)')
"""
 

if __name__ == '__main__':
    conn = MysqlClient()
    result = conn.batch(680,688)
    print(result)
