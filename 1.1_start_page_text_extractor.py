import csv
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from a_general import extractText
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

    for row in csvreader:
        url = row[0]
        try:
            driver.get(url)
        except WebDriverException:
            numOfEr = numOfEr+1
            print("page down")
            continue
        time.sleep(2.5)
        el1 = driver.find_element(By.TAG_NAME, 'body')
        # print("el1------------> neu" + el1.text)
        extractText(url, el1, "start_crawl_test/")
       # finalFunct(el1.text, numOfEr)

    print("numOfEr " + str(len(noResults)) + "        " + str(noResults))
