import csv
import sys
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_experimental_option( "prefs", {'protocol_handler.excluded_schemes.tel': False})
# driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)


# def setUpChrome():
#     global driver
#     # Using Chrome
#     chrome_options = webdriver.ChromeOptions()
#     prefs = {"profile.managed_default_content_settings.images": 2}
#     chrome_options.add_experimental_option("prefs", prefs)
#     chrome_options.add_argument('--ignore-certificate-errors')
#     chrome_options.add_argument('--ignore-ssl-errors')
#     #chrome_options.add_argument('headless')

#     scriptpath = os.path.realpath(__file__)
#     foldername = os.path.basename(scriptpath)
#     scriptpath = scriptpath[:scriptpath.find(foldername)]

#     scriptpath += 'chromedriver'

#     driver = webdriver.Chrome(scriptpath, chrome_options=chrome_options)
#     return driver


# driver = setUpChrome() #webdriver.Chrome('./chromedriver')
# driver = webdriver.Chrome('./chromedriver')

# driver.get("https://businessdirectory.cc/ontario/ads/sure-hair-international/")

# company_name = driver.find_element_by_css_selector(".entry-header .entry-title").text
# print(company_name)
# company_email = driver.find_element_by_css_selector("#cp_email .listing-custom-field-value a").text
# print(company_email)

# driver.quit()

with open('./csv_file', 'w') as f:
    print("opened a file")
    spamwriter = csv.writer(f, delimiter=',',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# count = 0

# while True:
    # try:
    #     delay = 3 # seconds
    #     myElem = WebDriverWait(browser, delay).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'adsbygoogle')))
    #     print("Page is ready!")
    #     # google_ADs = driver.find_element_by_css_selector("ins.adsbygoogle.adsbygoogle-noablate")
    #     driver.execute_script("""
    #         document.querySelector('ins').remove();
    #     """)
    #     print("---------------- script hitted ---------------------")
    # except:
    #     pass
    # all_iframes = driver.find_elements_by_tag_name("iframe")
    
    # print(f"ads pages {len(all_iframes)}")
    # if len(all_iframes) > 0:
    #     print("Ad Found\n")
    #     driver.execute_script("""
    #         var elems = document.getElementsByTagName("iframe"); 
    #         for(var i = 0, max = elems.length; i < max; i++)
    #         {
    #             elems[i].hidden=true;
    #         }
    #     """)
    #     print('Total Ads: ' + str(len(all_iframes)))
    # else:
    #     print('No frames found')
        
#     current_page_number = int(driver.find_element_by_css_selector('.pagination li.current a span').text)
#     last_page_number = int(driver.find_element_by_css_selector('.pagination li:nth-last-of-type(2)').text)
#     print(f"Processing page {current_page_number}..{last_page_number}")
#     if count == 17:
#         break
#     try:
#         next_page_link = driver.find_element_by_xpath(f'.//li[a = "{current_page_number + 1}"]')
#         next_page_link.click()
#         count += 1
#     except:
#         print(f"Exiting. Last page: {current_page_number}.")
#         break

# driver.quit()



# for child in parent_anchor_tags:
#     parent_links.append(child.get_attribute('href'))
# print(parent_links)