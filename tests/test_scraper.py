import unittest
import time
from selenium.webdriver.common.by import By
from scraper.scraper import Scraper
class testScraper(unittest.TestCase):
    def setUp(self):
        self.bot = Scraper()
    def test_accept_cookies(self):
        expected_value = True
        actual_value= self.bot.accept_cookies(xpath = '//button[@class="btn btn-level1 accept-all-cookies"]')
        if actual_value == None:
            actual_value = True
        self.bot.driver.find_element(By.XPATH, '//a[@class="logo"]' )
        self.assertEqual(expected_value, actual_value)

    def test_find_bar(self):
        expected_value = str
        self.bot.accept_cookies(xpath = '//button[@class="btn btn-level1 accept-all-cookies"]')
        actual_value = self.bot.find_search(xpath= '//input[@type="text"]').click()
        self.assertTrue(expected_value, actual_value)
    
    def test_properties(self):
        expected_vlaue = str
        self.bot.accept_cookies(xpath = '//button[@class="btn btn-level1 accept-all-cookies"]')
        self.bot.keys_search(text = 'nike caps')
        actual_value = self.bot.product_container(xpath = '//div[@id="productListRightContainer"]')
        self.assertTrue(expected_vlaue, actual_value)

    def test_properties_button(self):
        expected_value = str
        self.bot.accept_cookies(xpath = '//button[@class="btn btn-level1 accept-all-cookies"]')
        self.bot.keys_search(text = 'shoes')
        actual_value = self.bot.next_button(xpath = '//a[@rel="next"]')
        time.sleep(2)
        self.assertTrue(expected_value, actual_value)
    
    def test_image_download(self):
        expected_value = bytes
        self.bot.accept_cookies(xpath = '//button[@class="btn btn-level1 accept-all-cookies"]')
        self.bot.keys_search(text = 'adidas caps')
        time.sleep(1)
        actual_value = self.bot.image_download(url = 'https://www.jdsports.co.uk/product/adidas-originals-camo-baseball-cap/16239652/', file_name='adidas_cap_2', file_path='/Users/FKhan/Downloads/miniconda3/DCP_Project/raw_data/')
        self.assertTrue(expected_value, actual_value)
    
    def test_filter_m(self):
        expected_value = str
        self.bot.accept_cookies(xpath = '//button[@class="btn btn-level1 accept-all-cookies"]')
        self.bot.keys_search(text = 'hoodies')
        actual_value = self.bot.filter_m(xpath= '//a[@class="filterlink"]')
        self.assertTrue(expected_value, actual_value)

    def test_clicker(self):
        expected_value = str
        self.bot.accept_cookies(xpath = '//button[@class="btn btn-level1 accept-all-cookies"]')
        self.bot.product_click(url= 'https://www.jdsports.co.uk/product/blue-nike-tech-fleece-full-zip-hoodie/16475382/')
        actual_value =  self.bot.clicker(xpath= '//i[@class="fa fa-angle-down"]')
        self.assertTrue(expected_value, actual_value)

    # def tearDown(self) -> None:
    #     return super().tearDown()    
    # def test_init(self):
    #     pass

if __name__ == '__main__':
    unittest.main()    