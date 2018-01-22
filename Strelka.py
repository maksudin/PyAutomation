#Balans strelka
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonStrelka(unittest.TestCase):
	"""docstring for PythonStrelka"""
	def setUp(self):
		self.driver = webdriver.Chrome()
		
	def test_search_in_strelkacard_ru(self):
		driver = self.driver
		#WebDriver will wait until the page has fully loaded 
		driver.get("http://strelkacard.ru/")
		elem = driver.find_element_by_name("cardnum").send_keys("03334260045")
		xpath = "/html/body/div[2]/section[1]/div[1]/div[3]/div[3]/div[2]/div/form/a[1]/img"

		driver.find_element_by_xpath(xpath).click()

	def tearDown(self):
		self.driver.close()


if __name__ == '__main__':
	unittest.main()
