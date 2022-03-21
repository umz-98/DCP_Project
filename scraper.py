from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager


class Scraper:
    def __init__(self, url: str = 'https://www.jdsports.co.uk'):
        self.driver = Chrome(ChromeDriverManager().install())
        self.driver.get(url)
    
    def accept_cookies(self, xpath: str = '//button[@class="btn btn-level1 accept-all-cookies"]'):
        try:
            WebDriverWait(self.driver, 12).until(EC.presence_of_all_elements_located((By.XPATH,xpath)))
            self.driver.find_element(By.XPATH,xpath).click()
        except TimeoutException:
            print ('No cookies found')
    def find_search(self, xpath: str = '//input[@id="text"]'):
        try:
            WebDriverWait(self.driver, 12).until(EC.presence_of_all_elements_located((By.XPATH,xpath)))
            self.driver.find_element(By.XPATH,xpath).click()
        except TimeoutException:
            print ('No search found')


if __name__ == '__main__':
    bot = Scraper()
    bot.accept_cookies()        