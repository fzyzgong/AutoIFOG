# import traceback
from AutoIFOG.lib.write_log import write_log
#
# def deco(func):
#     def _deco(*args,**kwargs):
#         try:
#             ret = func(*args,**kwargs)
#         except Exception, e:
#             write_log(e.message+'------------------')
#         else:
#             write_log('pass----------')
#         finally:
#             print (ret)
#     return _deco
#
#
# @deco
# def func1():
#     a = 10
#     b = 0
#     c = a + b
#     print (c)
#     return 'pass'+str(c)
#
from AutoIFOG.lib.exe_deco import exe_deco

@exe_deco
def func2():
    try:
        a = 10
        b = 0
        c = a/b
    except Exception,e:
        write_log('Exception in [' + func2.__name__+'] '+e.message)
        return 'failed'
    else:
        return 'pass'
#
if __name__ == '__main__':
    # func1()
    func2()