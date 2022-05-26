from importlib.resources import path
from lib2to3.pgen2 import driver
from logging import exception
from time import time
from urllib import request
from requests import options
# from click import option
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import time
from typing import Union, Optional
import urllib.request
from scraper import Scraper
from sqlalchemy import create_engine
import pandas as pd
import json
import boto3
import glob
from uuid import UUID
import uuid

# class ec2_scraper:
options = Options()
options.add_argument('--user-agent=chrome:headless:userAgent=Mozilla/5.0 (X11\\; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36')
options.add_argument('--window-size=1920,1080')
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options=options
# def __init__(self, ):
bot = Scraper()
bot.accept_cookies()
time.sleep(3)
bot.keys_search('Nike football boots men')
container = bot.product_container()
time.sleep(1)


# def list_links():
list_properties = container.find_elements(By.XPATH, './ul/li')
imageLinks = container.find_elements(By.XPATH, "./ul/li/span/a/picture")
link_list = []
for property in list_properties:
        link_list.append(property.find_element(By.TAG_NAME, 'a').get_attribute('href'))
imageNames = []
for element in imageLinks:
        imageNames.append(element.find_element(By.TAG_NAME, 'img').get_attribute("src")) 
        # return link_list, imageNames 
time.sleep(2)
# def scraping(link_list, imageNames):
    # z = list_links()
    # if z:
        # try:
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
ENDPOINT = 'dcp1.ckiqoi4xq1wx.eu-west-2.rds.amazonaws.com' 
USER = 'postgres'
PASSWORD = 'Hamburg98'
PORT = 5432
DATABASE = 'postgres'
engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
df = pd.read_sql('EA7_shoes', engine)
id_scraper = list(df['id'])
image_scraper = list(df['imagelinks_1'])

property_dict = {'link':[],
            'price':[],
            'name':[],
            'id' :[],
            'UUID':[],
            'imagelinks_1':[],
            }

for link in link_list[0:27]:
    bot.driver.get(link)
    bot.driver.execute_script("window.scrollTo(0,1100)")  
    time.sleep(4)
    bot.clicker()
    time.sleep(1)
    id = bot.driver.find_element(By.XPATH, '//span[@class="product-code"]') 
    x2 = id.text   
    if x2 in id_scraper:
        continue
    else:
        property_dict['id'].append(id.text)  
        property_dict['link'].append(link)
        # price = bot.driver.find_element(By.XPATH, '//span[@class="pri"]')
        price = bot.driver.find_element(By.XPATH, '//span[@data-e2e="product-price"]')
        property_dict['price'].append(price.text)
        name = bot.driver.find_element(By.XPATH, '//h1[@itemprop="name"]')
        property_dict['name'].append(name.text) 
        property_dict['UUID'].append(uuid.uuid4())

for image in imageNames[0:27]:
    bot.driver.get(image)
    time.sleep(2)
    k = image
    if k in image_scraper:
        continue
    else:
        property_dict['imagelinks_1'].append(image)
time.sleep(1)         
property_dict    
            # return property_dict
        # except TimeoutException:
        #         print ('No next button found')
        # except NoSuchElementException:
        #         print('no such element error')
        # except WebDriverException:
        #         print ('webdriverexception') 
x = pd.DataFrame(property_dict)
x.to_sql('N_Football_B', con= engine, if_exists='append', index=False )

# def image_downloader(imageNames):
#     try:
bot.multiple_image_2(list=imageNames[0:27], file_path='/Users/FKhan/Downloads/miniconda3/DCP_Project/raw_data/')
time.sleep(2)
    # except TimeoutException:
    #         print ('No next button found')
    # except NoSuchElementException:
    #         print('no such element error')
    # except WebDriverException:
    #         print ('webdriverexception') 

# def boto_png():
#     y = image_downloader()
#     if y:
        # try:
s3_client = boto3.client('s3')
png_files = glob.glob('/Users/FKhan/Downloads/miniconda3/DCP_Project/raw_data/*.png')
for filename in png_files:
    s3_client.upload_file(filename, 'dcp1', filename)
        # except TimeoutException:
        #         print ('No next button found')
        # except NoSuchElementException:
        #         print('no such element error')
        # except WebDriverException:
        #         print ('webdriverexception')                       

# def json_upload(property_dict):
#     try:    
class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return obj.hex
        return json.JSONEncoder.default(self, obj)
j = json.dumps(property_dict, cls=UUIDEncoder, indent=4)
f = open('N_Football_B.json', 'w')
print(j, file=f)
f.close()
time.sleep(1)    
    # except TimeoutException:
    #         print ('No next button found')
    # except NoSuchElementException:
    #         print('no such element error')
    # except WebDriverException:
    #         print ('webdriverexception') 

# def boto_json():
#     x = json_upload()
#     if x:
        # try:
s3_client = boto3.client('s3')
response = s3_client.upload_file('/Users/FKhan/Downloads/miniconda3/DCP_Project/scraper/N_Football_B.json', 'dcp1', 'N_Football_B.json')
        #     return response 
        # except TimeoutException:
        #         print ('No next button found')
        # except NoSuchElementException:
        #         print('no such element error')
        # except WebDriverException:
        #         print ('webdriverexception')