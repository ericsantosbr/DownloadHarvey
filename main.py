from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('https://redecanais.cloud/browse-1-temporada-harvey-o-advogado-videos-1-date.html')

downloadDriver = webdriver.Firefox()

try:
	element = WebDriverWait(driver, 10)

finally:
	elementos = driver.find_elements_by_class_name('caption')
	paginas = driver.find_element_by_class_name('pagination pagination-sm pagination-arrows')
	aElement = elementos[0].find_elements_by_tag_name('a')
	for element in elementos:
		print(element.find_element_by_tag_name('a').get_attribute('href'))
		WebDriverWait(driver, 5)
		downloadDriver.get(element.find_element_by_tag_name('a').get_attribute('href'))
	driver.quit()
	downloadDriver.quit()