# SPOJ-Crawler-using-Scrapy

# What is it? 
A script written using Scrapy, a Python framework to extract data from websites. It automates the task of signing in to my SPOJ account and download my accepted solutions to various algorithmic problems. </br>
http://www.spoj.com/users/codegagu/

# How to use
1) Install Scrapy </br>

   https://docs.scrapy.org/en/latest/intro/install.html </br>
   Tip: Installation using Anaconda is easier since pip might have dependency issues. 

2) Understand the File Structure 

tutorial/</br>
?ts=4scrapy.cfg                  # deploy configuration file</br>
?ts=4tutorial/                   # project's Python module, we'll import our code from here</br>
?ts=4?ts=4__init__.py</br>
?ts=4?ts=4items.py                # project items definition file</br>
?ts=4?ts=4pipelines.py            # project pipelines file</br>
?ts=4?ts=4settings.py             # project settings file</br>
?ts=4?ts=4spiders/                # a directory where we put our spiders</br>
?ts=4?ts=4?ts=4__pycache__</br>
?ts=4?ts=4?ts=4__init__.py</br>
?ts=4?ts=4?ts=4login_spider.py     # My python script which contains all the code.</br>
?ts=4?ts=4?ts=4output.txt          # Text file for illustration purpose. It will store details about each solved problem.</br>
?ts=4?ts=4?ts=4codes               # A directory not initially present, but is created after the login spider is executed. It will store all the downloaded solutions.</br>
                                
