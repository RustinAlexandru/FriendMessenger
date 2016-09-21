from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
import time
import random


messages = ["Ce mai faci?", "Ma plictisesc, tu ce faci?", "Mesaj random", "Hahaha", "Lalalalalalala"]

def send_message_to_mihai():

    browser = webdriver.Firefox()

    browser.get("http://www.facebook.com")

    input_email = browser.find_element_by_id("email")
    input_password = browser.find_element_by_id("pass")

    input_email.send_keys("*************")
    input_password.send_keys("************")

    login_button = browser.find_element_by_id("u_0_10")
    login_button.submit()

    browser.get("https://www.facebook.com/messages/sandu.mihai")

    textarea  = browser.find_element_by_css_selector("textarea[class*='uiTextareaAutogrow _1rv']")
    textarea.send_keys(random.choice(messages))

    time.sleep(2)

    reply_btn = browser.find_element_by_id("u_0_x")
    reply_btn.click()

    time.sleep(2)

    browser.quit()

if __name__ == '__main__':
    send_message_to_mihai()
