#!/usr/bin/python
#coding:utf-8
#author:m4ster
#date:2014/12/17

from requests import get,post
from optparse import OptionParser
#from bs4 import BeautifulSoup
from urllib2 import urlopen
#from sys import exit
from time import time
import re,urllib

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

    if options.mode:
    	url = 'http://www.mnsfz.com/h/%s/index.html' % (options.mode)
    	try:
    		returnreq = urlopen(url)
    	except:
    		print '错误，错误原因：网络异常'
    	if returnreq.code == 403:
    		print '错误，错误原因：可能频率过高,此站有安全狗'
    	elif returnreq.code == 200:
    		content = returnreq.read()
    		imglist = re.findall(r'src="(http://.*?)"',content)
    		x=0
    		for imgurl in imglist:
    			urllib.urlretrieve(imgurl,'./%s/%s_%s.jpg' % (options.output,options.mode,x))
    			print "Download:%s" % imgurl
    			x += 1
    		if re.search(r'<div\sclass="spage">(.*)>></a></div>',content):
    			print "存在下一页"
    	else:
    		print '错误,错误原因:不正常的返回状态码'

#==============================================================
    if options.mode == 'tuijian':
    	url = 'http://www.mnsfz.com/h/top/rec.html'
    	try:
    		returnreq = urlopen(url)
    	except:
    		print '错误，错误原因：网络异常'
    	if returnreq.code == 403:
    		print '错误，错误原因：可能频率过高,此站有安全狗'
    	elif returnreq.code == 200:
    		content = returnreq.read()
    		imglist = re.findall(r'src="(http://.*?)"',content)
    		x=0
    		for imgurl in imglist:
    			urllib.urlretrieve(imgurl,'./%s/%s_%s.jpg' % (options.output,options.mode,x))
    			print "Download:%s" % imgurl
    			x += 1
    	else:
    		print '错误,错误原因:不正常的返回状态码'