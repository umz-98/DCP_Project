import unittest
from selenium.webdriver.common.by import By

from scraper.scraper import Scraper
class testScraper(unittest.TestCase):
    def setUp(self):
        self.bot = Scraper()
        return super().setUp()
    def test_accept_cookies(self):
        self.bot.accept_cookies(xpath = '//button[@class="btn btn-level1 accept-all-cookies"]')
        self.bot.driver.find_element(By.XPATH, '//a[@class="logo"]' )
    # def tearDown(self) -> None:
    #     return super().tearDown()    
    # def test_init(self):
    #     pass



if __name__ == '__main__':
    unittest.main()    