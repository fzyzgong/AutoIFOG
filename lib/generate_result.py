#coding=utf-8

import os
import csv
import time
from generate_html import write_csv_to_html


def generate_result(resultFileName,result):

    filePath = os.path.abspath(os.path.dirname(__file__))
    # print (filePath)
    resultFilePath = os.path.join(os.path.dirname(filePath),'results/',resultFileName)
    # print (resultFilePath)
    csvFile = open(resultFilePath,'a+')
    # csvFile = file(resultFilePath, 'a+')
    writer = csv.writer(csvFile)

    data = [result]

    writer.writerows(data)

    csvFile.close()

#gai hou zui ming
    html_result_path = resultFilePath.split('.')
    html_result_path = html_result_path[0] + '.html'
    write_csv_to_html(resultFilePath,html_result_path)


# if __name__ == "__main__":
#     generate_result('test1.txt','result test1..... pass')