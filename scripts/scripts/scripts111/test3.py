import sys
from AutoIFOG.lib.write_log import write_log
sys.path.append("../../../")
# sys.path.append("/home/fzyzgong/project/AutoIFOG")
from AutoIFOG.lib.exe_deco import exe_deco

@exe_deco
def test3():
    try:
        a = 10
        b = 0
        c = a/b
    except Exception,e:
        write_log('Exception in [' + test3.__name__+'] '+e.message)
        return 'failed'
    else:
        return 'pass'+c

if __name__ == '__main__':
    test3()