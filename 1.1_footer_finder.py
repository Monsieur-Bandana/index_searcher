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
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
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

    def selectElType(typeAsString: str):

        el1 = driver.find_element(By.TAG_NAME, typeAsString)
        findLinksInEl(url, el1, typeAsString)

    def findLinksInEl(url: str, stri: WebElement, typeAsString: str):
        res = []
        try:
            res = stri.find_elements(By.TAG_NAME, 'a')
        except:
            print("no links on page " + url)
        res_links = [url, typeAsString]
        try:
            for el in res:
                link = el.get_attribute("href")
                res_links.extend([link])
        except:
            print("################## iterabel exception in "+url)
        createCsvFile('el_links', res_links)

    for row in csvreader:
        url = row[0]
        try:
            driver.get(url)
        except WebDriverException:
            numOfEr = numOfEr+1
            print("page down")
            continue
        time.sleep(2.5)
        # elToLookInto = ["footer", "header", "body"]
        elToLookInto = ["body"]
        for el in elToLookInto:
            try:
                selectElType(el)

            except NoSuchElementException:
                print(
                    el+"-Element not found. NoSuchElementException occurred on page: " + url)
                continue

        # print("el1------------> neu" + el1.text)
       # finalFunct(el1.text, numOfEr)

    print("numOfEr " + str(len(noResults)) + "        " + str(noResults))
