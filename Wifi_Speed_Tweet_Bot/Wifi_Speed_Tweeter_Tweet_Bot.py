from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "Enter Chrome Driver Path"
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
ser = Service(executable_path=chrome_driver_path)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_option, service=ser)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.wrong = self.driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button')
        self.wrong.click()
        self.web = self.driver.find_element(By.XPATH,
                                            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        self.web.click()

        time.sleep(120)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        print(self.down.text)
        print(self.up.text)
        time.sleep(2)


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(10)
        self.login = self.driver.find_element(By.XPATH,
                                              '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        self.login.click()
        time.sleep(3)
        self.login.send_keys("Enter your Email Id")
        time.sleep(3)
        self.next = self.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        self.next.click()
        time.sleep(2)
        self.password = self.driver.find_element(By.XPATH,
                                                 '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        self.password.send_keys("Enter Your Password")
        self.enter = self.driver.find_element(By.XPATH,
                                              '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        self.enter.click()
        time.sleep(4)

        self.text_tweet = self.driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        self.text_tweet.click()
        message=f"Hi everyone check my internet speed {self.down}down/{self.up} up this is just python automated code."
        self.text_tweet.send_keys(message)
        time.sleep(2)

        self.tweet = self.driver.find_element(By.XPATH,
                                              '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div')
        self.tweet.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
time.sleep(2)
bot.tweet_at_provider()
