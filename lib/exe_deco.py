# -*- coding: utf-8 -*-
import traceback
from write_log import write_log
from AutoIFOG.utils.utils import str_2_tuple


def exe_deco(func):
    def _deco(*args, **kwargs):
        result = ()
        ret = None
        try:
            ret = func(*args, **kwargs)
            print (ret)
        except Exception, e:
            log = 'Exception in [' + func.__name__ + '] method: ' + str(e)
            write_log(log)
            result = str_2_tuple(log)
        else:
            log = 'No exception in ' + func.__name__ + ' method.'
            write_log(log)
            result = str_2_tuple(log)
        finally:
            return ret,result
    return _deco


@exe_deco
def test2():
    print ('hello test2.py')
    return 'test2.py pass'


