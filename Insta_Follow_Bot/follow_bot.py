from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "ENTER DRIVER PATH"
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
ser = Service(executable_path=chrome_driver_path)

USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"
TARGET_ACCOUNT = "ENTER ACCOUNT NAME"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_option, service=ser)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        log_in = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        email.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        time.sleep(2)
        log_in.click()
        time.sleep(10)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}")
        time.sleep(5)
        followers = self.driver.find_element(By.XPATH,
                                             '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[3]/a')
        followers.click()
        time.sleep(5)
        # to_scroll = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        # i = 0
        # while i<10:
        #     time.sleep(2)
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", to_scroll)
        #     i +=1

    def follow(self):
        to_follow = self.driver.find_elements(By.CLASS_NAME, value="_aano button")
        for button in to_follow:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_elements(By.CLASS_NAME, value='_a9-z button')
                cancel_button[1].click()
                time.sleep(2)



bot = InstaFollower()
bot.login()
time.sleep(2)
bot.find_followers()
bot.follow()
