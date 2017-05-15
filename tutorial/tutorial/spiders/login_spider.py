import os
import os.path
import scrapy
import urllib.request

import random
import string

from scrapy.shell import inspect_response
from scrapy.http import Request
from bs4 import BeautifulSoup

class LoginSpider(scrapy.Spider):
    name = 'spoj'
    start_urls = ['http://www.spoj.com/login']
    outputFile = open('output.txt' , 'w')

    ################# CREATED NEW DIRECTORY: CODES ########################

    current_path = os.getcwd()
    directory_path = os.path.join(current_path,'codes\\')
    directory_name = os.path.dirname(directory_path)

    if not os.path.exists(directory_name):
        print('creating codes folder')
        os.makedirs(directory_name)

    ########################################################################


    def parse(self, response):

        username = input('Enter username\n')
        password = input('Enter password\n')
        return scrapy.FormRequest.from_response(
            response,
            formdata={'login_user': username, 'password': password},
            callback=self.after_login
        )



    def after_login(self, response):

        if str.encode('Authentication failed!') in response.body:
            self.logger.error("Login failed")
            print ('Incorrect credentials')
            return    
        
        return scrapy.Request(url = "http://www.spoj.com/myaccount/" , callback = self.get_submission_links ) 



    def get_submission_links(self, response):

        href = response.css('table.table-condensed td a::attr(href)').extract() 
        # list comprehension is awesomeeeeee!
        href = [x for x in href if x!='/status/,codegagu/']
        href = [urllib.parse.urljoin('http://www.spoj.com',x) for x in href]

        for link in href:
            yield scrapy.Request(url = link, callback = self.filter_ACsubmissions)



    def filter_ACsubmissions(self,response):
        
        title = response.css('tr.kol1 > td.sproblem > a::attr(title)').extract_first() 
        lang = response.css('tr.kol1 > td.slang > span::text').extract_first()
        if lang != 'TEXT':
            file_url = response.css('tr.kol1 > td > a::attr(data-url)').extract_first()
            file_url = urllib.parse.urljoin('http://www.spoj.com',file_url)

            return scrapy.Request(url = file_url, callback = self.get_download_url,
                                meta={'language': lang , 'title':title , 'file_url':file_url})



    def get_download_url(self,response):

        file_url = response.meta['file_url']
        lang = response.meta['language']
        title = response.meta['title']

        # If lang = TEXT was allowed then following download_url will be None
        download_url = response.css('div.head a::attr(href)').extract_first()
        download_url = urllib.parse.urljoin('http://www.spoj.com',download_url)
        
        self.outputFile.write("File url: \t\t" + str(file_url) + "\n" +
                              "Download url: \t" + str(download_url) + "\n" + 
                              "Language: \t\t" + str(lang) + "\n" +
                              "Problem name: \t" + str(title) +
                              "\n\n\n")

        return scrapy.Request(url = download_url , callback = self.save_file,
                                                   meta={'language': lang , 'title':title})



    def save_file(self,response):

        lang = response.meta['language']
        
        # need to addmore languages here
        if lang == 'JAVA':
            lang = 'java'
        elif lang == 'C++' or lang == 'CPP14':
            lang = 'cpp'
        elif lang == 'C':
            lang = 'c'
        elif lang == 'PYTHON' or lang == 'PYTHON3':
            lang = 'py'
        
        title = response.meta['title']
        
        with open("codes\\"+title+"."+lang , 'wb') as f:
            f.write(response.body)

        return scrapy.Request(url = "http://www.spoj.com/myaccount/" , callback = self.after_login)


# file url :        link that shows the code.

# download_url :    link that downloads the code.

# href :            a list of links. links which shows 
#                   all submissions (AC/WA/TLE ..) made for a 
#                   particular problem. 
