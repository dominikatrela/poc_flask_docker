import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# driver = webdriver.Remote(
#     command_executor='XXX:4444/wd/hub',
#     desired_capabilities=DesiredCapabilities.CHROME)


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        service_log_path = "{}/chromedriver.log".format('/home/jenkins')
        service_args = ['--verbose']
        self.driver = webdriver.Chrome(service_args=service_args, service_log_path=service_log_path)

        
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
