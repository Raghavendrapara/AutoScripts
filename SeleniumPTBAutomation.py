from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
chrome = webdriver.Chrome('/usr/bin/chromedriver')
chrome.maximize_window()
chrome.get('https://archive.physionet.org/cgi-bin/atm/ATM')
select = Select(chrome.find_element_by_name('database'))
select.select_by_value('ptbdb')
chrome.find_element_by_xpath("//input[@value='e']").click()
select = Select(chrome.find_element_by_name('tool'))
select.select_by_value('samples_to_mat')

for i in range(538):
	rec = chrome.find_element_by_xpath("//input[@value='Next record']")
	rec.click()
	elems = chrome.find_elements_by_xpath("//a[@href]")
	elems[133].click()
	time.sleep(5)
	


