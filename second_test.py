import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os

# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# driver = webdriver.Remote(
#     command_executor='XXX:4444/wd/hub',
#     desired_capabilities=DesiredCapabilities.CHROME)


class SearchTextOnPage(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=options)

        
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://10.10.45.20:5000/")
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//body[contains(text(),'costam costam :)')]")
        assert "costam costam :)" in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
