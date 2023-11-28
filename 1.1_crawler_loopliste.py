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


import time

if __name__ == '__main__':
    pyLinks = []
    file = open('links.csv')
    csvreader = csv.reader(file)

    options = webdriver.ChromeOptions()
    # options.add_argument('proxy-server=')

    driver = uc.Chrome(options=options)

    file2 = open('sitemap_links.csv')
    csvreader2 = csv.reader(file2)
    allAdresses = []
    for row in csvreader2:
        allAdresses.append(row)

    newCsvList = []

    numOfEr = 0

    def finalFunct(stri, numOfEr):
        els = driver.find_elements(By.TAG_NAME, "a")
        els2 = driver.find_elements(By.TAG_NAME, "sitemap")
        els3 = driver.find_elements(By.TAG_NAME, "loc")
        if (len(els) > 0 or len(els2) > 0):
            if ("itemap" in stri or "XML" in stri or len(els2) > 0):
                print("#########################found sth")
                for el in els:
                    row.append(el.text)

                for el in els3:
                    tag = BeautifulSoup(el, 'html.parser')
                    print(str(tag['innerHTML']))
                    row.append(str(tag['innerHTML']))
                with open('newCSVfile2.csv', 'a') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow(row)
                    f_object.close()

            else:
                numOfEr += 1

    def getRightUrl(stro):
        i = 0
        while i < len(allAdresses):
            stri = str(allAdresses[i])
            stri = stri[2:-2]
            url = stro + stri
            try:
                driver.get(url)
                print(url)
                el1 = driver.find_element(By.TAG_NAME, 'body')
                if ("orry" in el1.text or "not found" in el1.text or "404" in el1.text):
                    time.sleep(2.5)
                    i = i+1
                    continue
                print("URL "+url+" is correct")
                return url
            except WebDriverException:
                print("page down")
        return ""

    options = Options()
    options.add_argument("start-maximized")
    # options.binary_location(
    #        "C:\\Users\\nicol\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")

    for row in csvreader:
        url = getRightUrl(row[0])
        try:
            driver.get(url)
        except WebDriverException:
            print("page down")
            continue
        print("_________________________________>"+row[0])
        time.sleep(2.5)
        el1 = driver.find_element(By.TAG_NAME, 'body')
        # print("el1------------> neu" + el1.text)
        finalFunct(el1.text, numOfEr)

    print("numOfEr " + str(numOfEr))
