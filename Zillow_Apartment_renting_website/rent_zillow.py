import requests
import bs4
import lxml

FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSeKNin7vhXBK6V1Ud0geCWjQ2rd8NxwxeXF3g6Z9uTVtTPoxQ/viewform?usp=sf_link"

res = requests.get(
    "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56302207889088%2C%22east%22%3A-122.29317039432057%2C%22south%22%3A37.69315679452771%2C%22north%22%3A37.862756115769535%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D",
    headers={"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,mr;q=0.7",
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"})
print(res.text)
data = res.text
soup = bs4.BeautifulSoup(data, "html.parser")

property_data = soup.select(".List-c11n-8-81-1__sc-1smrmqp-0 a")

print()
all_links = []
for link in property_data:
    href = link['href']
    if "http" not in link:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)
print()
print(all_links)

property_info = soup.select(".List-c11n-8-81-1__sc-1smrmqp-0 address")
all_addresses = [address.get_text().split(" | ")[-1] for address in property_info]
print()
print(all_addresses)
print()

property_prices = soup.select(".StyledPropertyCardDataArea-c11n-8-81-1__sc-yipmu-0 span")
all_prices = [price.get_text() for price in property_prices]
print()
print(all_prices)

print()
print(len(all_links))
print(len(all_addresses))
print(len(all_prices))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "D:\DEVELOPMENT\chromedriver.exe"
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
ser = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(options=chrome_option, service=ser)
FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSeKNin7vhXBK6V1Ud0geCWjQ2rd8NxwxeXF3g6Z9uTVtTPoxQ/viewform?usp=sf_link"

for n in range(len(all_prices)):
    driver.get(FORM_LINK)
    addresss = driver.find_element(By.XPATH,
                                   value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    addresss.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    time.sleep(2)
    submit_button.click()
driver.quit()
