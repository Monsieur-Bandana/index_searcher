import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from csv import writer
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options


import time

pyLinks = []
file = open('links.csv')
csvreader = csv.reader(file)

file2 = open('sitemap_links.csv')
csvreader2 = csv.reader(file2)

newCsvList = []

numOfEr = 0


def finalFunct(stri, numOfEr):
    els = driver.find_elements(By.TAG_NAME, "a")
    if (len(els) > 0):
        if ("itemap" in stri or "XML" in stri):
            print("#########################found sth")
            for el in els:
                row.append(el.text)
            with open('newCSVfile.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(row)
                f_object.close()

        else:
            numOfEr += 1


def getRightUrl(stro):
    for row in csvreader2:
        url = stro + row[0]
        try:
            driver.get(url)
          #  el1 = driver.find_element(By.TAG_NAME, 'body')
          #  if ("orry" in el1.text or "not found" in el1.text or "404" in el1.text):
           #     continue
            print("URL "+url+" is correct")
            return url
        except WebDriverException:
            print("page down")
            continue


options = Options()
options.add_argument("start-maximized")
# options.binary_location(
#        "C:\\Users\\nicol\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")
driver = webdriver.Chrome()

for row in csvreader:
    url = row[0] + "sitemap_index.xml"
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
