<<<<<<< HEAD
# -*- coding: cp936 -*-
#执行另外一个脚本
import sys,os,subprocess,commands
from subprocess import Popen,PIPE

def test():
	path = '/home/fzyzgong/project/AutoIFOG/scripts/scripts'
	p = Popen('python test2.py',shell=True, stdout=PIPE, stderr=PIPE,cwd=path)

	p.wait()

	if(p.returncode == 0):
		print "stdout111:%s" %p.stdout.read()

if __name__ == '__main__':

	test()


# def use_logging(func):
# 	def _deco(*args, **kwargs):
# 		result = ()
# 		ret = None
# 		try:
# 			ret = func(*args, **kwargs)
# 			print (ret)
# 		except Exception, e:
# 			log = 'Exception in ' + func.__name__ + ' method: ' + str(e)
# 			result = log
# 		else:
# 			log = 'No exception in ' + func.__name__ + ' method.'
# 			result = log
# 		finally:
# 			return ret, result
#
# 	return _deco
#
#
#
# @use_logging
# def foo():
# 	print ('i am foo')
# 	return 'pass'
#
#
# @use_logging
# def foo1():
# 	print ('i am foo1')
# 	return 'failed'
#
#
# if(__name__ == '__main__'):
# 	foo()
# 	foo1()
=======
def sayHello:
	print 'hello world'

sayHello()
>>>>>>> 602fd5b6b01e09d348a271f68c8b0b5edf6986e8
