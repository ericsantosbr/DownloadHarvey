from os import truncate
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import StaleElementReferenceException

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", '/home/eric/Downloads/Harvey')
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "video/mp4")

driver = webdriver.Firefox(firefox_profile=profile)

try:
	element = WebDriverWait(driver, 10)

finally:
	current_window_handle = driver.current_window_handle
	worked = False
	for i in range(1, 40):
		worked = False
		while(not worked):
			try:
				# Opens the list main page
				driver.get('https://redecanais.cloud/harvey-o-advogado-dublado-lista-de-episodios_8838ff667.html')
				watch_episode_button_xpath = f'/html/body/div[2]/div[5]/div[1]/div/div[1]/div[3]/p/a[{i}]'
				WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, watch_episode_button_xpath)))

				# Gets the episode page link
				watch_episode_button = driver.find_element_by_xpath(watch_episode_button_xpath)
				access_video_page_link = watch_episode_button.get_attribute('href')
				driver.get(access_video_page_link)

				sleep(10)

				driver.get(access_video_page_link)
				pageFound = False
				frame_xpath = '/html/body/div[2]/div[4]/div/div/div/div[2]/div/div/iframe'
				start_episode_button_xpath = '/html/body/div/h2/a'
				# Finds the link to have easier access to the "Assistir" button
				videoPage = driver.find_element_by_xpath(frame_xpath).get_attribute("src")

				# Access the link
				driver.get(videoPage)

				# Clicks in the "Assistir" button
				driver.find_element_by_xpath(start_episode_button_xpath).click()

				sleep(15)
				# Changes to the Player frame
				driver.switch_to.frame("Player")

				# Finds the div containting the download link and access it
				rede_canais_player_id = driver.find_element_by_id("RedeCanaisPlayer")
				video_download_link = rede_canais_player_id.get_attribute("baixar")

				# Switches to Download Link
				print(f'Downloading ep {i}')
				driver.get(video_download_link)

				worked = True

				sleep(15)

			# Ignores exception for trying again			
			except NoSuchElementException as inst:
				print('NoSuchElement raised.')
				print(inst.with_traceback)
				print(f'Episode {i} not found. Trying again')
				pass



	sleep(20)

	# Get element by id RedeCanaisPlayer,  read the baixar property property, open it in new tab and download the given file

	driver.quit()