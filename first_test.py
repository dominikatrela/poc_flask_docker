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


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=options)

        
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
