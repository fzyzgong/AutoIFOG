#coding=utf-8
import csv,os


def write_csv_to_html(csv_path, save_path):

    # print os.getcwd()

    csvFile = file(csv_path,'rb')

    reader = csv.reader(csvFile)

    html = open(save_path, 'w')

    html.write(
        """
        <html>
        <head>
            <titile>AutoIFOG test result</titile>
            <h1>AutoIFOG test result</h1>
            <h3>Restult file path:"""+csv_path+"""</h3>
            <style>img{float:left;margin:5px;}</style>
        </head>
        <body>
        
        </body>
            <table border="1">
        """)
    for line in reader:
        sig =True

        for each in line:
            if(('failed' in each) or ('Exception in' in each)):
                sig = False

        if sig ==False:

            html.write('<tr bgcolor="#8B2323">')

        else:

            html.write('<tr bgcolor="#00FF7F">')

        for each in line:

            html.write('<td>'+each+'</td>')

        html.write('</td>')

    html.write("""
    
    </table>
    </body>

    """)