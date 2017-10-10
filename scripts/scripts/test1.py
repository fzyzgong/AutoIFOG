from AutoIFOG.lib.exe_deco import exe_deco

@exe_deco
def test1():
    a = 11
    return 'pass'


if __name__ == '__main__':
    test1()