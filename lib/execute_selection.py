# -*- coding: utf-8 -*-

from exe_deco import exe_deco
from read_selection import read_selection
from write_log import write_log
import os
import subprocess
from AutoIFOG.utils.utils import *

from generate_result import generate_result



def execute_selection():

    selection = read_selection()

    genTime = get_local_time()

    resultFileName = genTime + ' test_result.csv'

    autoIFOG = os.getcwd()

    # print (autoIFOG)

    resultFilePath = os.path.join(autoIFOG,'results',resultFileName)

    # print (genTime)
    generate_result(resultFileName,('scriptPath','detail','startTime','endTime','duration'))


    for scriptPath in selection:
        result = str_2_tuple(scriptPath)

        startTime = get_specific_time()

        # ret,result2 = execute_script(scriptPath)
        ret = execute_script(scriptPath)

        # print ('result2:'+str(result2))
        print ('ret:'+str(ret))


        endTime = get_specific_time()

        duration = (endTime-startTime).microseconds*0.000001
        # print duration
        result = result+str_2_tuple(ret)+str_2_tuple(startTime)+str_2_tuple(endTime)+str_2_tuple(duration)

        generate_result(resultFileName,result)


#some problem
# @exe_deco
def execute_script(scriptPath):

    write_log('execute_script: '+scriptPath)

    # os.system('python '+scriptPath)

    stdout, stderr = subprocess.Popen(['python', scriptPath], stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE).communicate()

    r = stdout + stderr

    return r


if __name__ == '__main__':

    execute_selection()