#coding=utf-8
import os
import sys


'''
function:把AutoIFOG/scripts/all_scripts_selection.txt文件中的可执行脚本列表读取并返回
'''
def read_selection():

    path = os.path.abspath(os.path.dirname(__file__))
    # print (path)

    parentPath = os.path.dirname(path)
    # print (parentPath)

    selectionFilePath = os.path.join(parentPath,'scripts','all_scripts_selection.txt')
    # print (selectionFilePath)

    selection = []

    for line in open(selectionFilePath):
        selection.append(line.replace('\n',''))
    # print (selection)
    return selection

if __name__ == '__main__':

    read_selection()