import csv
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from csv import writer
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from a_general import createCsvFile
from selenium.webdriver.remote.webelement import WebElement


import time

if __name__ == '__main__':
    pyLinks = []
    file = open('links.csv')
    csvreader = csv.reader(file)

    options = webdriver.ChromeOptions()
    # options.add_argument('proxy-server=')

    driver = uc.Chrome(options=options)

    numOfEr = 0

    noResults = []

    def findSitemap(url, stri: WebElement):
        texti = stri.text
        x = texti.split()
        res = []
        res.append(url)
        i = 0
        while (i < len(x)):
            if x[i].find("Sitemap:") == 0 or x[i].find("sitemap:") == 0:  # outcome = array

                res.append(x[i+1])  # links is in next position in array
            i = i+1

        if (len(res) == 0):
            noResults.append(url)

        createCsvFile('robotstxt3', res)

    for row in csvreader:
        url = row[0]+"robots.txt"
        try:
            driver.get(url)
        except WebDriverException:
            numOfEr = numOfEr+1
            print("page down")
            continue
        time.sleep(2.5)
        el1 = driver.find_element(By.TAG_NAME, 'body')
        # print("el1------------> neu" + el1.text)
        findSitemap(url, el1)
       # finalFunct(el1.text, numOfEr)

    print("numOfEr " + str(len(noResults)) + "        " + str(noResults))
