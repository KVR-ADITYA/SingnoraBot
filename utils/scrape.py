from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

def set_viewport_size(driver, width, height):
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)

class scroll_class:
    '''
    custom class to use __call__ function for explicit webdriver wait until page scrolls to give y value
    '''
    def __init__(self,y):
        self.y = y
    def __call__(self, driver):
        posA = 0
        posB = 1
        scrollPos = 0
        while posA < self.y+600:
            posA = driver.execute_script("return window.scrollY;")
            scrollPos += 300
            driver.execute_script("window.scrollTo(0, {});".format(scrollPos))
            posB = driver.execute_script("return window.scrollY;")

        #driver.execute_script("window.scrollTo(0, 0);")# driver.execute_script("window.scrollTo(0,0)")
        return True

def scrollpage( driver,y):
    posA = 0
    posB = 1
    scrollPos = 0
    while posA < y+600:
        posA = driver.execute_script("return window.scrollY;")
        scrollPos += 300
        driver.execute_script("window.scrollTo(0, {});".format(scrollPos))
        posB = driver.execute_script("return window.scrollY;")

    #driver.execute_script("window.scrollTo(0, 0);")# driver.execute_script("window.scrollTo(0,0)")
    return True


def get_as_infographic(char_name):

    #initiate selenium chrome webdriver driver
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
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
                    #table = skilldmgwrappers.find_element_by_class_name("add_stat_table")
                except NoSuchElementException as exception:
                    print("live_data Table not found")
                else:
                    print("table found")
                    rect = skilldmgwrappers.rect
                    set_viewport_size(driver, rect['width'] + 1200, rect['height'] + 1200)
                    #scrollpage(driver,rect['y'])
                    #time.sleep(3)
                    wait = WebDriverWait(driver, timeout=3)
                    wait.until(scroll_class(rect['y']))
                    png = skilldmgwrappers.screenshot_as_png
                    driver.close()
                    return png
    driver.close()
    print("never found the char and href element")
    return False
    


