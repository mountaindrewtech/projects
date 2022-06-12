# Mountain
# Bestbuy on Google Chrome Scalping Bot
# 5/15/21

import time
import linecache
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
# For using Chrome
driver = webdriver.Chrome('chromedriver.exe')

# Bestbuy: Change url_link
driver.get("url_link")

#Variables
first_name = linecache.getline('variables.txt', 1).strip()
last_name = linecache.getline('variables.txt', 2).strip()
email = linecache.getline('variables.txt', 3).strip()
password = linecache.getline('variables.txt', 4).strip()
phone = linecache.getline('variables.txt', 5).strip()
street_address = linecache.getline('variables.txt', 6).strip()
city = linecache.getline('variables.txt', 7).strip()
state = linecache.getline('variables.txt', 8).strip()
zipcode = linecache.getline('variables.txt', 9).strip()
card_number = linecache.getline('variables.txt', 10).strip()
month = linecache.getline('variables.txt', 11).strip()
year = linecache.getline('variables.txt', 12).strip()
civ = linecache.getline('variables.txt', 13).strip()

# Click add to cart button if it does not exist refresh
foundButton = False

while not foundButton:

    btnAddToCart = driver.find_element_by_class_name("add-to-cart-button")

    if ("btn-disabled" in btnAddToCart.get_attribute("class")):
        # delay
        time.sleep(3)

        # refresh
        driver.refresh()

    else:
        foundButton = True

        btnAddToCart.click()

        # Click go to cart button
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[8]/div/div[1]/div/div/div/div/div[1]/div[3]/a"))).click()

# Click or ignore shipping option: not needed for online only products
       # WebDriverWait(driver, 20,).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[1]/div[4]/ul/li/section/div[2]/div[2]/form/div[2]/fieldset/div[2]/div[1]/div/div/div/input"))).click()

# Click checkout button
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button"))).click()

# Click contintue as guest
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/main/div[2]/div[4]/div/div[2]/button"))).click()

# Enter shipping information
    # Shipping information
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[1]/label/div/input"))).send_keys(first_name)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[2]/label/div/input"))).send_keys(last_name)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[3]/label/div[2]/div/div/input"))).send_keys(street_address)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[6]/div/div[1]/label/div/input"))).send_keys(zipcode)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[5]/div/div[1]/label/div/input"))).send_keys(city) # In this order to avoid autocomplete window from address

    # Contact information
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[2]/label/div/input"))).send_keys(email)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[3]/label/div/input"))).send_keys(phone)

    # State dropdown
        drpState = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME,"state")))
        state_box=Select(drpState)
        state_box.select_by_value(state)

    # Continue
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button"))).click()

# Enter credit card info
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[1]/div/input"))).send_keys(card_number)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[2]/div[2]/div/div[2]/div/input"))).send_keys(civ)
    
        drpMonth = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[2]/div[1]/div/div[1]/label/div/div/select")))
        month_box=Select(drpMonth)
        month_box.select_by_value(month)

        drpYear = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[2]/div[1]/div/div[2]/label/div/div/select")))
        year_box=Select(drpYear)
        year_box.select_by_value(year)

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[3]/section/div[2]/form/label/input"))).send_keys(password)

    # Place order
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[4]/button"))).click()
        time.sleep(10)
        driver.quit()
        
