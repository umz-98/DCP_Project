import unittest
import time
from selenium.webdriver.common.by import By
from scraper.scraper import Scraper
class testScraper(unittest.TestCase):
    def setUp(self):
        self.bot = Scraper()
        # return super().setUp()
    def test_accept_cookies(self):
        self.bot.accept_cookies(xpath = '//button[@class="btn btn-level1 accept-all-cookies"]')
        self.bot.driver.find_element(By.XPATH, '//a[@class="logo"]' )
    
    def test_properties(self):
        self.bot.accept_cookies(xpath = '//button[@class="btn btn-level1 accept-all-cookies"]')
        self.bot.keys_search(text = 'nike caps')
        self.bot.product_container(xpath = '//div[@id="productListRightContainer"]')

    def test_properties_button(self):
        self.bot.accept_cookies(xpath = '//button[@class="btn btn-level1 accept-all-cookies"]')
        self.bot.keys_search(text = 'shoes')
        self.bot.next_button(xpath = '//a[@rel="next"]')
        time.sleep(2)
    
    # def tearDown(self) -> None:
    #     return super().tearDown()    
    # def test_init(self):
    #     pass



if __name__ == '__main__':
    unittest.main()    