from importlib.resources import path
from lib2to3.pgen2 import driver
from logging import exception
from time import time
from typing_extensions import Self
# from typing_extensions import Self
from urllib import request
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
from typing import Union, Optional
import urllib.request


class Scraper:
    '''
    This class defines a scraper that can be used to browse and navigate websites

    parameters
    ----------
    url: str
        The webpage that we are trying to visit
    
    Attribute
    ---------  
    driver:
        This driver is the webdriver object
    '''
    def __init__(self, url: str = 'https://www.jdsports.co.uk'):
        self.driver = Chrome(ChromeDriverManager().install())
        self.driver.get(url)
        # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    def accept_cookies(self, xpath: str = '//button[@class="btn btn-level1 accept-all-cookies"]'):
        '''
        This method allows the 'accept cookies' button to be pressed
        
        parameters
        ----------
        xpath: str
            The xpath of locating the accept cookies button
        '''
        try:
            (WebDriverWait(self.driver, 12)
                .until(EC.presence_of_all_elements_located((By.XPATH,xpath))))
            self.driver.find_element(By.XPATH,xpath).click()
        except TimeoutException:
            print ('No cookies found')
    def find_search(self, xpath: str = '//input[@type="text"]'): 
         # -> Union[webdriver.element, None]
        '''
        This method locates the search bar
        
        parameters
        ----------
        xpath: str
             The xpath of locating the search bar

        Returns
        -------
        Union[webdriver.element, None]

        '''
        try:
            find_bar = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH,xpath)))
            find_bar.click()
            return find_bar
        except TimeoutException:
            print ('No search found')
            return None
    def keys_search(self, text:str) -> None:
        '''
        This method searches the webpage using whatevever keys

        parameters
        ----------
        text: str
             The text that is going to be searched for and also scrolls the page
  
        '''
        find_bar = self.find_search()
        if find_bar:
            time.sleep(1)
            find_bar.send_keys(text)
            find_bar.send_keys(Keys.ENTER)
            find_bar = True
        if find_bar == True:
           self.driver.execute_script("window.scrollTo(0,1000)")     
        else:
             raise Exception('Not working')
    def product_container(self, xpath: str = '//div[@id="productListRightContainer"]'):
        return self.driver.find_element(By.XPATH,xpath)

    def next_button(self, xpath: str = '//a[@rel="next"]'):
        # -> Optional[webdriver.element]
        '''
        This method goes to the next page of a product list

        parameters
        ----------
        xpath: str
            The xpath of locating the next button

        Returns    
        -------
        Optional[webdriver.element]

        '''
        try:
            find_next_button = WebDriverWait(self.driver, 12).until(EC.presence_of_element_located((By.XPATH,xpath)))
            find_next_button.click()
            return find_next_button
        except TimeoutException:
            print ('No next button found')

    def image_download(self, url, file_name, file_path):
        '''
        This method downloads and individual image

        parameters
        ----------
        xpath: str
            The xpath of locating the link to an image

        Returns    
        -------
        Image: png
            Represents downloaded image

        '''
        self.driver.get(url)
        time.sleep(1)
        try:
            imageLinks = self.driver.find_element(By.XPATH, '//div[@class="owl-item active"]')
            lol_links = imageLinks.find_element(By.TAG_NAME, 'img')
            final_links = lol_links.get_attribute('src')
            time.sleep(1)
            self.driver.get(final_links)
            path_L = file_path + file_name + '.png'
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(
            final_links, path_L)
        except NotImplementedError:
            pass 
    
    
    def image_download_2(self, file_name, file_path, url):
        '''
        This method is only used together with mutiple_image_2 method

        parameters
        ----------
        Image: png
            Represents downloaded images
        '''
        try:
            path_L = file_path + file_name + '.png'
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(
            url, path_L)
        except NotImplementedError:
            pass 
    
    def multiple_image_2(self, list, file_path):
        '''
        This method downloads multiple images

        parameters
        ----------
        xpath: str
            
        Returns    
        -------
        Image: png
            Represents downloaded images
        '''
        for i in range(0, len(list)):
            name = str(i)
            path_k = file_path + name
            url_name = list[i]
            self.image_download_2(url=url_name, file_name=name, file_path=path_k)
     
   
    def filter_m(self, xpath: str = '//a[@class="filterlink"]'):
        # -> Union[webdriver.element, None]
        '''
        This method filters for 'medium' size

        parameters
        ----------
        xpath: str
            The xpath of filtering for medium size

        Returns    
        -------
        Union[webdriver.element, None]

        '''
        try:
            time.sleep(1)
            filter_search = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH,xpath)))
            filter_search.click()
            return filter_search
        except TimeoutException:
            print ('no filted added')
            return None

    def clicker(self, xpath: str = '//i[@class="fa fa-angle-down"]'):
        # -> Union[webdriver.element, None]
        '''
        This method extends the product information

        parameters
        ----------
        xpath: str
            The xpath of extending product information

        Returns    
        -------
        Union[webdriver.element, None]

        '''
        try:
            clicker = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH,xpath)))
            clicker.click()
            return clicker
        except TimeoutException:
            print ('no filted added')
            return None
    
    def product_click(self, url):
        '''
        This method goes to any url added

        parameters
        ----------
        url: str
            The url of any given link
        '''
        self.driver.get(url)

if __name__ == '__main__':
    bot = Scraper()
    bot.accept_cookies()
    bot.next_button()
    bot.find_search()
    bot.product_container()
    bot.image_download()
    bot.multiple_image_2()    
    bot.clicker()  