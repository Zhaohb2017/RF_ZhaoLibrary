#coding=utf-8
import logging

__version__='0.1'

class Zhaobat(object):
	def log_wanning(self,str):
		logging.info(u':返回结果：%s'%str)

	def log_info(self):
		print 'Hello,world'