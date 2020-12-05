""" this file is main bot file the base of this bot is on selenium """
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from info import INFO


browser = webdriver.Firefox()

def login():
    browser.get("https://www.instagram.com/")
    sleep(1)
    try:
        browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
    except:
        pass

    browser.find_element_by_xpath("//input[@name='username']").send_keys(INFO['usr_name'])
    browser.find_element_by_xpath("//input[@name='password']").send_keys(INFO['passwd'])
    browser.find_element_by_xpath("//button[@type='submit']").click()

login()

def count_of_post(user_addr):
    f""" find how many post is in account """
    sleep(2)
    browser.get(f'https://www.instagram.com/{user_addr}/')
    count = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span")
    count = int(count.get_attribute('innerHTML'))
    return count


account = ['bny1485']
def like_comment():
    """ like & commet all post in predefine account """

    for user_addr in account:
        sleep(2)
        count_post = count_of_post(user_addr)
        counter = 0
        while counter < count_post:
            if counter == 0:
                browser.find_element_by_xpath('//div[@class="v1Nh3 kIKUG  _bz0w"]').click()
            sleep(5)
            browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
            sleep(4)
            ADDR = "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea"
            browser.find_element_by_xpath(ADDR).click()
            browser.find_element_by_xpath(ADDR).clear()
            message = "test message"
            browser.find_element_by_xpath(ADDR).send_keys(message)
            browser.find_element_by_xpath(ADDR).send_keys(Keys.RETURN)
            sleep(1)
            if counter != (count_post - 1):
                browser.find_element_by_xpath('//a[@class=" _65Bje  coreSpriteRightPaginationArrow"]').click()

            if counter == (count_post - 1):
                browser.find_element_by_xpath('/html/body/div[5]/div[3]/button').click()
            
            counter += 1
sleep(3)
like_comment()
