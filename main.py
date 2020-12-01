""" this file is main bot file the base of this bot is on selenium """

from time import sleep
from selenium import webdriver
from info import INFO
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get("https://www.instagram.com/")

sleep(2)

browser.find_element_by_xpath("//input[@name='username']").send_keys(INFO['usr_name'])
browser.find_element_by_xpath("//input[@name='password']").send_keys(INFO['passwd'])
browser.find_element_by_xpath("//button[@type='submit']").click()

print("I do it")
