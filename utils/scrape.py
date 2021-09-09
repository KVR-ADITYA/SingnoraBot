from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time
import os

def set_viewport_size(driver, width, height):
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)

def scrollpage(driver, y):
    posA = 0
    posB = 1
    scrollPos = 0
    while posA < y+600:
        posA = driver.execute_script("return window.scrollY;")
        scrollPos += 300
        driver.execute_script("window.scrollTo(0, {});".format(scrollPos))
        posB = driver.execute_script("return window.scrollY;")

    #driver.execute_script("window.scrollTo(0, 0);")# driver.execute_script("window.scrollTo(0,0)")



def get_as_infographic(char_name):
    #save web driver manager's webdriver exectuables locally by overriding default location setting
    #os.environ['WDM_LOCAL'] = '1'
    #initiate selenium chrome webdriver driver
    driver = webdriver.Chrome()
    #get the page
    driver.get("https://genshin.honeyhunterworld.com/db/char/characters/?lang=EN")
    chars = driver.find_elements_by_class_name("char_sea_cont")
    for char in chars:
        try:
            link = char.find_element_by_tag_name("a")
            link = link.get_attribute("href")
            name = char.find_element_by_class_name("sea_charname")
            name = name.text
        except NoSuchElementException as exception:
            print("Element not found and find element failed")
        else:

            if char_name.lower() in name.lower():      
                print("found element") 
                driver.get(link)

                try:
                    element = driver.find_element_by_id("live_data")
                    skilldmgwrappers = element.find_element_by_class_name("skilldmgwrapper")
                    table = skilldmgwrappers.find_element_by_class_name("add_stat_table")
                except NoSuchElementException as exception:
                    print("live_data Table not found")
                else:
                    print("table found")
                    rect = table.rect
                    set_viewport_size(driver, rect['width'] + 600, rect['height'] + 600)
                    scrollpage(driver,rect['y'])
                    time.sleep(3)
                    png = skilldmgwrappers.screenshot_as_png
                    driver.close()
                    return png
    driver.close()
    print("never found the char and href element")
    return False
    


