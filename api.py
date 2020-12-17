#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:  Analyst1981@gmail.com
# @date:    2019-3-16
from flask import Flask
import random
from  db import MysqlClient
import geoip2.database
import os.path
from setting import *

root = os.path.dirname(os.path.abspath(__file__))  
_dir_ = os.path.join(root, "GeoLite2-City")
__all__ = ['app']

app = Flask(__name__)


def get_conn():
    g_Mysql= MysqlClient()
    return g_Mysql


@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/proxydata')
def get_proxy():
    """
    Get a proxy
    :return: random agent
    """
    conn = get_conn()
    for fpathe,dirs,fs in os.walk(_dir_):
        reader = geoip2.database.Reader(os.path.join(fpathe,"GeoLite2-City.mmdb"))
        logger.log('DEBUG', f'api - Geolite2-City reader :  {reader}  ------')

    #return conn.random()
    test_proxies =conn.random()
    jsonData=[]
    for row in test_proxies:  
        result = {} 
        result['IP'] = row[0]  
        result['PORT'] = row[1]  
        result['TYPE'] = row[2]
        try:
           data = reader.city(row[0])
           result['Country']= data.country.name
           result['Subdivisions']=data.subdivisions.most_specific.name
           result['City']=data.city.name
           result['Latitude']=data.location.latitude
           result['Longitude']= data.location.longitude
        except:
           # IP does not exist in .mdb
           result['Country']= 'Not Found'
           result['Subdivisions']= 'Not Found'
           result['City']= 'Not Found'
           result['Latitude']= 'Not Found'
           result['Longitude']= 'Not Found'
           jsonData.append(result)
    i=random.randint(0,len(jsonData))
    respoen='<html><body><div id="container"><div><div id="list" style="margin-top:20px;"><table class="table table-bordered table-striped"><thead><tr><th>IP</th><th>PORT</th><th>protocol</th><th>country</th><th>Subdivisions</th><th>city</th><th>longitude</th><th>latitude</th></tr></thead><tbody><tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr></tbody></table></div></div></div><style>.tag_area { margin:10px 0 0px 0; }.tag_area .label { background-color:#c1c1bf;text-decoration:none; font-size:13px; padding:3px 5px 3px 5px;}.tag_area .label.active, .tag_area .label.active:hover { background-color:#468847; }.tag_area .label:hover { background-color:#aaa; }tbody a { color:#777; }tbody a:hover { text-decoration:none; }</style></body></html>'%(jsonData[i]['IP'],jsonData[i]['PORT'],jsonData[i]['TYPE'],jsonData[i]['Country'],jsonData[i]['Subdivisions'],jsonData[i]['City'],jsonData[i]['Latitude'],jsonData[i]['Longitude'])
    return respoen
    #"<br> %s://%s:%s <br /> <br>country:%s  city:%s <br /><br> Dimension:%s  longitude:%s<br />" % (jsonData[i]['TYPE'],jsonData[i]['IP'],jsonData[i]['PORT'],jsonData[i]['Country'],jsonData[i]['City'],jsonData[i]['Latitude'],jsonData[i]['Longitude'])


@app.route('/random')
def get_proxy_():
    """
    Get a proxy
    :return: random agent
    """
    conn = get_conn()
    for fpathe,dirs,fs in os.walk(_dir_):
        reader = geoip2.database.Reader(os.path.join(fpathe,"GeoLite2-City.mmdb"))    
    #return conn.random()
    test_proxies =conn.random()
    jsonData=[]
    for row in test_proxies:  
        result = {} 
        result['IP'] = row[0]  
        result['PORT'] = row[1]  
        result['TYPE'] = row[2]    
        jsonData.append(result)
    i=random.randint(0,len(jsonData))
    respoen='<html><body><div id="container"><div><div id="list" style="margin-top:20px;"><table class="table table-bordered table-striped"><thead><tr><th>IP</th><th>PORT</th><th>Protocol</th></tr></thead><tbody><tr><td>%s</td><td>%s</td><td>%s</td></tr></tbody></table></div></div></div><style>.tag_area { margin:10px 0 0px 0; }.tag_area .label { background-color:#c1c1bf;text-decoration:none; font-size:13px; padding:3px 5px 3px 5px;}.tag_area .label.active, .tag_area .label.active:hover { background-color:#468847; }.tag_area .label:hover { background-color:#aaa; }tbody a { color:#777; }tbody a:hover { text-decoration:none; }</style></body></html>'%(jsonData[i]['IP'],jsonData[i]['PORT'],jsonData[i]['TYPE'])
    return respoen

@app.route('/count')
def get_counts():
    """
    Get the count of proxies
    :return:  total agent pool
    """
    conn = get_conn()
    return "Number of agents：%s" % str(conn.count())
    


if __name__ == '__main__':
    app.run()
