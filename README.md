# SPOJ Crawler using Scrapy

# What is it? 
A script written using Scrapy, a Python framework to extract data from websites. It automates the task of signing in to my SPOJ account and download my accepted solutions to various algorithmic problems. </br>
[See my profile on SPOJ](http://www.spoj.com/users/codegagu/)

# How to use
1) Install Scrapy </br>

   https://docs.scrapy.org/en/latest/intro/install.html </br>
   Tip: Installation using Anaconda is easier since pip might have dependency issues. 
   
2) Fork this repository and clone to dekstop.

3) Understand the File Structure 

   - tutorial/
      - scrapy.cfg 
      - tutorial/  
         - __init__.py
         - items.py
         - pipelines.py
         - settings.py 
         - spiders/    
            - __pycache__
            - __init__.py
            - login_spider.py
            - output.txt     
            - codes          

4) How to run:
   
   Open command prompt and navigate to the spiders folder and run the following command</br>
   ```
   scrapy crawl spoj
   ```
   Provide your username and password when asked for. This might take few seconds. </br>
   
   When the process is complete, you'll see a newly created folder named ```codes```. This folder will contain all the downloaded files.
                                

NOTE: This spider will not download problem solutions which are in ```TEXT``` format. Presently it supports C, C++, Java, CPP14, PYTHON, PYTHON3. I will add more later.

That's all folks!
