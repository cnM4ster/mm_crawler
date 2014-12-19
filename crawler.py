#!/usr/bin/python
#coding:utf-8
#author:m4ster
#date:2014/12/17

from optparse import OptionParser
from sys import exit
from time import time

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-m','--mode',dest='mode',type='string',help='Select Mode',default='1')
    parser.add_option('-t','--thread',dest='thread',type='int',help='threads',default='10')
    parser.add_option('-l','--length',dest='length',type='int',help='length',default='50')
    parser.add_option('-o','--output',dest='output',type='string',help='output files',default='pics')
    (options, args) = parser.parse_args()

    thread = options.thread # 线程数
    useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.102 Safari/537.36'