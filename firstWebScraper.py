from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import math


origin = input("What is your origin? ")
destination = input("What is your destination? ")
departureMonth = input("What is your departure month? (give a #, ex: March = 3) ")
departureDay = input("What is you departure day? ")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

#bookARide
driver.get("https://www.bookaride.ca/")
driver.implicitly_wait(5)

bookARide_buttons = driver.find_elements(By.CLASS_NAME, "btn")
bookARide_buttons[0].click()
bookARide_origin = driver.find_element(By.CLASS_NAME, "form-control")
bookARide_origin.send_keys(origin)
driver.find_element(By.CLASS_NAME, "dropdown-item").click()

bookARide_buttons[1].click()
bookARide_destination = driver.find_elements(By.CLASS_NAME, "form-control")[1]
bookARide_destination.send_keys(destination)
button = driver.find_elements(By.CLASS_NAME, "dropdown-menu")[2]
button = button.find_element(By.TAG_NAME, "li")

button.find_element(By.CLASS_NAME, "text").click()
driver.find_element(By.CLASS_NAME, "nxtbtn").click()

driver.implicitly_wait(10)

pricesDiv = driver.find_elements(By.CLASS_NAME, "trip-price")
pricesTags = []
prices = []
tripItems = driver.find_elements(By.CLASS_NAME, "trip-item")
times = []
departureLocation = []
tripsInfo = []

for p in pricesDiv:
    pricesTags.append(p.find_element(By.TAG_NAME, "b"))

for trips in tripItems:
    times.append(trips.find_element(By.CLASS_NAME, "departure-time").get_attribute("innerHTML").strip())
    departureLocation.append(trips.find_element(By.CLASS_NAME, "departure-location").get_attribute("innerHTML").strip())

for p in pricesTags:
    prices.append(p.get_attribute("innerHTML"))

for i in range(len(prices)):
    tripsInfo.append("$" + prices[i] + ": " + times[i] + ", " + departureLocation[i])

tripsInfo.sort()

for i in range(min(5, len(tripsInfo))):
    print(tripsInfo[i])

"""
user input for origin, destination, date

unique one for each site (flix, bookaride, greyhound, megabus):
input the information into the site then store in requests.get("link")
find the prices based on how each site stores the info
sort based on cheapest --> output top 3 prices + time of departure and arrival
**time is a final touch, focus on functionality

**another final touch
ask if want to 
"""
"""
asdiasdijaspd
"""