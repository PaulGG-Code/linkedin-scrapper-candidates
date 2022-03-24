#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script.py

import parameters
import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# function to ensure all key data fields have a value
def validate_field(field):
    if field == 'None':
        field = 'No results'
        return field
    else:
        return field
    
# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('./chromedriver.exe')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/login')

# locate email form by element_by_id
username = driver.find_element_by_id('username')
# use data from Parameters file imported vars
username.send_keys(parameters.linkedin_username)

# locate email form by element_by_id
password = driver.find_element_by_id('password')
# use data from Parameters file imported vars
password.send_keys(parameters.linkedin_password)

# locate submit button by_class_name
#log_in_button = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button")

# locate submit button by_xpath (Necessary?)
log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
log_in_button.click()
sleep(0.5)

driver.get('https://www.google.com')
sleep(2)

search_query = driver.find_element(By.NAME, "q")
search_query.send_keys(parameters.search_query)
sleep(0.5)

search_query.send_keys(Keys.RETURN)
sleep(3)

# Get list of all linkeding profile URLs
linkedin_urls = driver.find_elements(By.CLASS_NAME, "yuRUbf")
profiles = []
links = [url.find_element(By.CSS_SELECTOR, 'a').text for url in linkedin_urls]
profile = [url.find_element(By.CSS_SELECTOR, 'a').get_attribute('href') for url in linkedin_urls]
profile

'''
for elem in elems:
    if not 'google' in elem.get_attribute("href"):
        linkedin_urls.append(elem.get_attribute("href"))
linkedin_urls
'''
sleep(0.5)

# Create the CSV hader row
header = ['Name', 'Job Title', 'Location', 'Link']
with open(parameters.file_name, 'a') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header) # write header

# For loop to iterate over each URL in the list
    for linkedin_url in profile:
        # open profile URL
        driver.get(linkedin_url)

        # add a 3 second pause loading each URL
        sleep(3)

        # assigning the source code for the webpage to variable sel
        sel = Selector(text=driver.page_source)

        name = sel.xpath('//*[starts-with(@class, "text-heading-xlarge inline t-24 v-align-middle break-words")]/text()').extract_first()
        if name:
            name = name.strip()
            # print(name)

        job_title = sel.xpath('//*[starts-with(@class, "text-body-medium break-words")]/text()').extract_first()
        if job_title:
            job_title = job_title.strip()
            # print(jobtitle)

        location = sel.xpath('//*[starts-with(@class, "text-body-small inline t-black--light break-words")]/text()').extract_first()
        if location:
            location = location.strip()
            # print(location)

        currentJob = sel.xpath('//h3/text()').extract_first()

        linkedin_url = driver.current_url

        # validating if the fields exist on the profile
        name = validate_field(name)
        job_title = validate_field(job_title)
        location = validate_field(location)
        linkedin_url = validate_field(linkedin_url)

        # Print what information is being write to the CSV file
        rows = [name,job_title,location,linkedin_url]
        print('Writing to CSV:', rows)

        # Write ROW content to the CSV file
        csv_writer.writerow([name,job_title,location,linkedin_url])
