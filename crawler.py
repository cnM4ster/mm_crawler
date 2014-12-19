#!/usr/bin/python
#coding:utf-8
#author:m4ster
#date:2014/12/17

from requests import get,post
from optparse import OptionParser
from bs4 import BeautifulSoup
from sys import exit
from time import time
import re

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-m','--mode',dest='mode',type='string',help='Select Mode',default='qingchun')
    parser.add_option('-p','--page',dest='page',type='int',help='start page',default='1')
    parser.add_option('-t','--thread',dest='thread',type='int',help='threads',default='10')
    parser.add_option('-l','--length',dest='length',type='int',help='length',default='50')
    parser.add_option('-o','--output',dest='output',type='string',help='output files',default='pics')
    (options, args) = parser.parse_args()

    thread = options.thread # 线程数
    useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.102 Safari/537.36'

    if options.mode == 'qingchun':
    	#清纯私房
    	url = 'http://www.mnsfz.com/h/qingchun/index.html'
    	try:
    		returnreq = get(url)
    	except:
    		print '[x] 错误，错误原因：网络异常'
    	if returnreq.status_code == 403:
    		print '[x] 错误，错误原因：频率过高,此站有狗'
    	elif returnreq.status_code == 200:
    		soup = BeautifulSoup(returnreq.text)
    		returnsoup = soup.find_all("img")
    		imglist =[]
    		for i in returnsoup:
    			imglist.append(i)
    		for i in range(len(imglist)):
    			print imglist[i]
    			#print re.findall('<img\ssrc="(http://.*)">',)
    		#print soup

    	else:
    		print '[x] 错误,错误原因:不正常的返回状态码'