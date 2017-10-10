


from AutoIFOG.lib.exe_deco import exe_deco

@exe_deco
def test2():
    a = 1
    return 'pass'


if __name__ == '__main__':
    test2()