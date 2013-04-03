#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os,sys
import chardet

cncode = ['GB18030', 'GBK', 'GB2312']

if len(sys.argv) != 2 :
	print "Usage:"+sys.argv[0]+" filename"

try:
	fileName = sys.argv[1]
	fileDesc = open(fileName, 'r+')
except Exception, e:
	raise e

data = fileDesc.read()
encoding=chardet.detect(data)['encoding']
if encoding in cncode:
	contextUTF8=unicode(data, encoding).encode("UTF-8")
	fileDesc.write(contextUTF8)
else:
	print fileName+" not Chinese encode!\n"

fileDesc.close()