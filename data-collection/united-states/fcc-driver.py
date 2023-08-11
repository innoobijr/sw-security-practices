import undetected_chromedriver as uc
import time
#monkey patch
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from helpers import read_yaml_conf




options = uc.ChromeOptions()
#options.headless=True
#options.add_argument('--headless')
options.add_experimental_option("prefs", {"download.default_directory" : "~/Downloads"})

def main():
    configs = read_yaml_conf("/Users/innocentobijr/dev/sw-security-practices/data-collection/united-states/conf.yaml")
    print(configs)
    driver = uc.Chrome(options=options, use_subprocess=False)
    driver.get("{}?version={}".format(configs['us']['base'], configs['us']['date']))
    #wait = WebDriverWait(driver, timeout=10)
    select_element = driver.find_element(By.ID, 'state')
    select = Select(select_element)
    select.select_by_visible_text('California')

    #table_element = driver.find_element(By.CLASS, "table")
    table_rows = driver.find_elements(By.XPATH,'//*[@id="content"]/app-nationwide-data/div/div[5]/div[1]/div/table/tbody/tr')
    for row in table_rows:
        button = row.find_element(By.TAG_NAME, 'button')
        print(button)
        button.click_safe()
        
        #span_element_st = button.find_element(By.TAG_NAME, 'span')
        #wait = WebDriverWait(driver, timeout=10)
        #span_element = button.find_element(By.XPATH, "//span[@class='fas fa-cloud-download-alt']")
        time.sleep(200)
        

    #print("The number of rows is {}".format(num_rows))




    #option_list = select.options
    #print(option_list)
    time.sleep(100)


if __name__ == "__main__":
    main()