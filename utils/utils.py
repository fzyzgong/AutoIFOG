#coding=utf-8

import time
import os
import datetime


def str_2_tuple(*args):

    return args

#get format time
def get_local_time():

    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


def get_specific_time():

    return datetime.datetime.now()


def tylan_assert(actual,expected):

    if actual != expected:

        result = 'failed'
        print (result)
    else:
        result = 'passed'
        print (result)
    return result


def tylan_assert_include(actual,expected):
    if expected not in actual:

        result = 'failed'
        print (result)
    else:
        result = 'passed'
        print (result)
    return result


# if __name__ == "__main__":
#     get_local_time()