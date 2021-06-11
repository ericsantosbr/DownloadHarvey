from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('https://redecanais.cloud/harvey-o-advogado-dublado-lista-de-episodios_8838ff667.html')

downloadDriver = webdriver.Firefox()

try:
	element = WebDriverWait(driver, 10)

finally:
	# for i in range(1, 50):
	watch_episode_button = driver.find_element_by_xpath(f'/html/body/div[2]/div[5]/div[1]/div/div[1]/div[3]/p/a[{1}]')
	new_page = watch_episode_button.click()
	# new_page.then()

	print(driver.window_handles)

	WebDriverWait(driver, 30)
	driver.quit()
	downloadDriver.quit()