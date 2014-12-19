#!/usr/bin/python
#coding:utf-8
#author:m4ster
#date:2014/12/17

from optparse import OptionParser
from urllib2 import urlopen
from time import time
import re,urllib,os
import threading


COUNT = 0 # 下载个数
PAGE = 1 # 页数
CATEGORY = None # 分类
THREAD = 0 # 线程数
OUTPUT = None # 输出文件夹
LENGTH = 0 #抓取个数
LOCK = threading.Lock() # 线程锁


def reqeuest():
	global COUNT,CATEGORY,OUTPUT,PAGE,LENGTH,LOCK
	if PAGE == 1:
		url = 'http://www.mnsfz.com/h/top/rec.html' if CATEGORY == 'tuijian' else 'http://www.mnsfz.com/h/%s/index.html' % (CATEGORY)
	else:
		url = 'http://www.mnsfz.com/h/top/rec_%s.html' % (PAGE) if CATEGORY == 'tuijian' else 'http://www.mnsfz.com/h/%s/index_%s.html' % (CATEGORY,PAGE)
	try:
		returnreq = urlopen(url)
	except  Exception as e:
		print e
		return False

	if returnreq.code == 403:
		print '错误，错误原因：可能频率过高,此站有安全狗'
		return False
	elif returnreq.code == 404:
		print '错误，错误原因: 页面不存在3'
		return False
	elif returnreq.code == 200:
		content = returnreq.read()
		# 安全狗404页面
		if("404.safedog.cn" in content):
			return False
		imglist = re.findall(r'src="(http://.*?)"',content)
		for imgurl in imglist:
			if(LENGTH != 0 and COUNT >= LENGTH):
				return False
			LOCK.acquire()
			COUNT += 1
			LOCK.release()
			try:
				urllib.urlretrieve(imgurl,'./%s/%s_%s.jpg' % (OUTPUT,CATEGORY,COUNT))
			except Exception as e:
				print e
				COUNT -=1
				return False
			LOCK.acquire()
			print "Download:%s" % imgurl
			LOCK.release()
		if re.search(r'<div\sclass="spage">(.*)>></a></div>',content):
			return True
		else:
			return False
	else:
		print '错误,错误原因:不正常的返回状态码4'
		return False

def runWork():
	global PAGE
	while True:
		PAGE += 1
		if(reqeuest() == False):
			break
		
if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option('-c','--category',dest='category',type='string',help='Select Category')
	parser.add_option('-t','--thread',dest='thread',type='int',help='threads',default='10')
	parser.add_option('-l','--length',dest='length',type='int',help='length',default='0')
	parser.add_option('-o','--output',dest='output',type='string',help='output files',default='pics')
	(options, args) = parser.parse_args()
	THREAD = options.thread
	CATEGORY = options.category 
	OUTPUT = options.output
	LENGTH = options.length
	# 目录不存在则创建
	if(not os.path.exists(OUTPUT)):
		os.mkdir(OUTPUT)
	threadlist = []
	for i in range(THREAD):
		t1 = threading.Thread(target=runWork)
		threadlist.append(t1)
	for t in threadlist:
		t.start()
	for t in threadlist:
		t.join()
	print 'Spider complete COUNT:%s' % (COUNT) 