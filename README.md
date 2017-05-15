# SPOJ-Crawler-using-Scrapy

# What is it? 
A script written using Scrapy, a Python framework to extract data from websites, to automate the task of signing in to my SPOJ account and download my accepted solutions to various algorithmic problems. </br>
http://www.spoj.com/users/codegagu/

# How to use
1) Install Scrapy </br>

   https://docs.scrapy.org/en/latest/intro/install.html </br>
   Tip: Installation using Anaconda is easier since pip might have dependency issues. 

2) Understand the File Structure 

tutorial/
    scrapy.cfg                  # deploy configuration file
    tutorial/                   # project's Python module, we'll import our code from here
        __init__.py
        items.py                # project items definition file
        pipelines.py            # project pipelines file
        settings.py             # project settings file
        spiders/                # a directory where we put our spiders
            __pycache__
            __init__.py
            login_spider.py     # My python script which contains all the code.
            output.txt          # Text file for illustration purpose. It will store details about each solved problem.
            codes               # A directory not initially present, but is created after the login spider is executed. It will store all the downloaded solutions.
                                
