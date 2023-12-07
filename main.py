from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
edge_options.add_argument("--start-maximized")
driver = webdriver.Edge(options=edge_options)

forms_url = "https://forms.gle/6WCUvVqtSZdHUuqa8"
rentals = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(rentals)
response.raise_for_status()

webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

link_listings = soup.find_all(name="a", class_="property-card-link")

links = [url.get("href") for url in link_listings]

price_listings = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")

prices = [entry.getText().split("/")[0].split("+")[0] for entry in price_listings]

apart_listings = soup.find_all(name="address")

addresses = [apartment.getText().strip().replace("|", "") for apartment in apart_listings]

driver.get(forms_url)

time.sleep(5)

input_a = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
input_b = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
input_c = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

input_a.send_keys("test")
input_b.send_keys("money")
input_c.send_keys("url")

time.sleep(5)

submit = driver.find_element(By.CSS_SELECTOR, value="div div span span")
submit.click()

time.sleep(5)
new_response = driver.find_element(By.CSS_SELECTOR, value="a")
new_response.click()
