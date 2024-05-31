from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from faker import Faker

from config import browser_driver, names_lang


class NoButton(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)

class NoInputName(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)



class browser:
	faker = Faker(names_lang)
	def __init__(self) -> None:
		
		opt = Options()
		opt.add_argument('--headless')
		self.browser = webdriver.Firefox(options=opt, executable_path=browser_driver) if browser_driver is not None else webdriver.Firefox(options=opt)
		self.browser.implicitly_wait(0.7) 

	def start_test(self, link, nick):
		self.browser.get(link)
		try:
			button = self.browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/div/div/div[2]/form/div/div[2]/div[2]/button")
			#button = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/div/div/div/div[2]/form/div/div[2]/div[2]/button")))
			if button.is_displayed() and button.is_enabled():
				button.click()
		except (TimeoutException, NoSuchElementException):
			pass
		try:
			name_field = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="testdesignersettings-full_name"]')))
			name_field.send_keys(nick if nick else self.faker.name())
		except:raise NoInputName
		try:
			button = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/button")))
			button.click()
		except:raise NoButton