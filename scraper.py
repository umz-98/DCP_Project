from lib2to3.pgen2 import driver
from logging import exception
from time import time
from typing_extensions import Self
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time



class Scraper:
    def __init__(self, url: str = 'https://www.jdsports.co.uk'):
        self.driver = Chrome(ChromeDriverManager().install())
        self.driver.get(url)
        # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    def accept_cookies(self, xpath: str = '//button[@class="btn btn-level1 accept-all-cookies"]'):
        try:
            WebDriverWait(self.driver, 12).until(EC.presence_of_all_elements_located((By.XPATH,xpath)))
            self.driver.find_element(By.XPATH,xpath).click()
        except TimeoutException:
            print ('No cookies found')
    def find_search(self, xpath: str = '//input[@type="text"]'):
        try:
            find_bar = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH,xpath)))
            find_bar.click()
            return find_bar
        except TimeoutException:
            print ('No search found')
            return None
    def keys_search(self, text):
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
                

    
    # bellow next button code
    def next_button(self, xpath: str = '//a[@rel="next"]'):
        try:
            find_next_button = WebDriverWait(self.driver, 12).until(EC.presence_of_element_located((By.XPATH,xpath)))
            find_next_button.click()
            return find_next_button
        except TimeoutException:
            print ('No next button found')
    #  bellow working on 'gender' filter but only the link is different
    # def filter_men(self, xpath):
    
    
    # bellow is for filterting by size 'm' but probabaly has the same issue as above
    def filter_m(self, xpath: str = '//a[@class="filterlink"]'):
        try:
            time.sleep(1)
            filter_search = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH,xpath)))
            filter_search.click()
            return filter_search
        except TimeoutException:
            print ('no filted added')
            return None
     


if __name__ == '__main__':
    bot = Scraper()
    bot.accept_cookies()
    bot.next_button()
    bot.find_search()
    bot.product_container()        