import csv
from selenium import webdriver
from a_general import name_creator, progress_definer, createCsvFile
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
import csv
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

import time


# lineToRead = next(csvreader)


if __name__ == '__main__':
    file = open('robotstxt2.csv')
    csvreader = csv.reader(file)
    pyLinks = []
    file_length = sum(1 for row in csvreader)

    driver = uc.Chrome()

    i = 1
    for row in csvreader:
        print("--------------------------"+str(row))
        if len(row) > 1:
            for address in row[1:]:
                driver.get(address)

                time.sleep(2.5)
                try:
                    elemnt = driver.find_element(By.TAG_NAME, 'body')
                except NoSuchElementException:
                    print("couldnt find elements in page " + row[0])
                    continue
                str_arr = elemnt.text.split()

                links = [address]
                for str_el in str_arr:
                    if str_el.startswith("<loc>"):
                        str_el = str_el[5:-6]
                        links.extend([str_el])

                filename = name_creator(
                    link=row[0], prfx="sitemaps_first_loop/")

                createCsvFile(filename, links)
                time.sleep(2.5)
        print("step no " + str(i) + ", of " +
              file_length + " total steps completed")
        i = i+1

    driver.quit()
