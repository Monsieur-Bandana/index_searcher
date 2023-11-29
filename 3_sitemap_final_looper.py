import csv
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import csv
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from csv import writer
import xml.etree.ElementTree as ET
from a_general import name_creator, progress_definer

import time

pyLinks = []
file = open('okxcomrobotstxt.csv', "r")
csvreader = csv.reader(file)

lineToRead = next(csvreader)

if __name__ == '__main__':

    options = webdriver.ChromeOptions()

    driver = uc.Chrome(options=options)

    elemnts = []

    address = lineToRead[1]
    driver.get(address)

    time.sleep(2.5)
    elemnts = driver.find_element(By.TAG_NAME, 'body')

    str_arr = elemnts.text.split()

    links = []
    for str_el in str_arr:
        if str_el.startswith("<loc>"):
            str_el = str_el[5:-6]
            links.append(str_el)

    for link in links:
        driver.get(link)
        tag_names = ['div', 'a', 'p', 'span', 'body']
        els = []
        for tag_name in tag_names:
            try:
                elements = driver.find_elements(By.TAG_NAME, tag_name)
            except NoSuchElementException:
                print("Element not found. NoSuchElementException occurred.")
                continue
            for el in elements:
                els.append(el.text)

        filename = name_creator(link, "txt", "crwl_test/")

        with open(filename, 'w') as file:
            # Write some text to the file
            file.write(str(els))
        i = progress_definer(i, links)

        time.sleep(2.5)
