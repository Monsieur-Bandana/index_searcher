import csv
import undetected_chromedriver as uc
from selenium import webdriver

import csv
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from csv import writer
import xml.etree.ElementTree as ET

import time

pyLinks = []
file = open('robotstxttest3.csv', "r")
csvreader = csv.reader(file)

lineToRead = next(csvreader)

if __name__ == '__main__':

    options = webdriver.ChromeOptions()

    driver = uc.Chrome(options=options)

    elemnts = []

    for address in lineToRead[1:]:
        driver.get(address)

        time.sleep(2.5)
        elemnts = driver.find_element(By.TAG_NAME, 'body')

        str_arr = elemnts.text.split()

        links = []
        links.append(address)
        for str_el in str_arr:
            if str_el.startswith("<loc>"):
                str_el = str_el[5:-6]
                links.append(str_el)

        filename = lineToRead[0]

        original_string = filename
        characters_to_remove = [':', '/', '.']

        # Using a loop to remove characters
        resulting_string = ''.join(
            char for char in original_string if char not in characters_to_remove)

        print(resulting_string)

        filename = resulting_string + ".csv"

        with open(filename, 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(links)
        time.sleep(2.5)

        f_object.close()
