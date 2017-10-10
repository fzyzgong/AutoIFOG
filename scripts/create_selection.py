#coding=utf-8
import os
import sys


'''
function:select all script ,get execute path for file_path.
'''
def create_selection():

    path =  sys.path[0]

    # print path

    selection = []

    for i in os.walk(os.path.join(path,'scripts')):
        # print i

        for fileName in i[2:3][0]:

            # print ("i[2:3]"+str(i[2:3]))
            filePath = os.path.join(i[0],fileName)

            if(check_if_python(fileName)):

                selection.append(filePath)
                # print (filePath)
                # print (fileName)

    return selection

    '''
    tips:other methon
    '''
    # for root,dirs,file_name in os.walk(os.path.join(path,'scripts')):
    #
    #     for file in file_name:
    #
    #         if(check_if_python(file)):
    #
    #             selection.append(os.path.join(root,file))
    #
    # print (selection)
    #
    # return selection

'''
function:check all file,select about end with '.py' file.
'''
def check_if_python(fileName):

    if(fileName.endswith('.py')):

        return True


'''
function:create a file_path file,record all excute path about the scripts111;
'''
def create_selection_file(selection):

    filePath = os.path.join(sys.path[0],'all_scripts_selection.txt')

    theFile = open(filePath,'w')

    for scriptPath in selection:
        theFile.write(scriptPath+'\n')

if __name__ == "__main__":
    selection = create_selection()
    create_selection_file(selection)

