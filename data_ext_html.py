"""
this python file is used to extract data_set from url
"AQI" data set is extracted from online
SAMPLE_url = https://en.tutiempo.net/climate/08-2021/ws-421820.html
      where '421820' Delhi/ Sarfdarjung
"""

""" IMPORTING MANDATORY LIBRARIES """
import os
import time
import requests
import sys

""" writing function for retrieving data from url """
def retrieve_html():
    for year in range(2013,2019):
        for month in range(1, 13):
            if (month < 10):
                url = 'http://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month, year)
            else:
                url = 'http://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month, year)
            texts = requests.get(url)
            text_utf = texts.text.encode('utf=8')

            """ creating directory for particular data_set """
            if not os.path.exists("Data_set/Html_Data/{}".format(year)):
                os.makedirs("Data_set/Html_Data/{}".format(year))
            with open("Data_set/Html_Data/{}/{}.Html".format(year, month), "wb") as output:
                output.write(text_utf)

        sys.stdout.flush()



if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print("Time taken {}".format(stop_time-start_time))