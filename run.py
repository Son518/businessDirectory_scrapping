import os
from logging import NullHandler
from selenium import webdriver
import csv
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()

prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('headless')

driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

with open('./company_urls', 'w') as f:
    print("opened a file")
    spamwriter = csv.writer(f)

    driver.get("https://businessdirectory.cc/")
    
    parent_links = []
    # Canada Directory URLs
    parent_anchor_tags = driver.find_elements_by_css_selector("#canada h4 a")
    for child in parent_anchor_tags:
        parent_links.append(child.get_attribute('href')+"ads")
        
    parent_anchor_tags = driver.find_elements_by_css_selector('#canada ul li a')
    for child in parent_anchor_tags:
        parent_links.append(child.get_attribute('href')+"ads")

    # US Directory URLs
    parent_anchor_tags = driver.find_elements_by_css_selector('#usa h4 a')
    for child in parent_anchor_tags:
        parent_links.append(child.get_attribute('href')+"ads")
        
    parent_anchor_tags = driver.find_elements_by_css_selector('#usa ul li a')
    for child in parent_anchor_tags:
        parent_links.append(child.get_attribute('href')+"ads")
        
    print(len(parent_links), parent_links)
    # driver.close()

    def get_company_info(company_url):
        try:
            driver.get(company_url)
            company_name = driver.find_element_by_css_selector(".entry-header .entry-title").text
            company_email = driver.find_element_by_css_selector("#cp_email .listing-custom-field-value a").text
            print(f"company information: {company_name} {company_email}")
            spamwriter.writerow([company_name, company_email])
        except BaseException:
            pass

    company_links = []
    for parent_link in parent_links:
        try:
            driver.get(parent_link)
            current_page_number = int(driver.find_element_by_css_selector('.pagination li.current a span').text)
            last_page_number = int(driver.find_element_by_css_selector('.pagination li:nth-last-of-type(2)').text)
            print(f"page numbers: {current_page_number}, {last_page_number}")
            parent_anchor_tags = driver.find_elements_by_css_selector("h2 a")
            for child in parent_anchor_tags:
                # company_links.append(child.get_attribute("href"))
                # print(f"company_link (first): {child.get_attribute('href')}")
                spamwriter.writerow([child.get_attribute("href")])
                # get_company_info(child.get_attribute("href"))
                
            print(f"Last page number: {last_page_number}")
            if last_page_number > 1:
                for page_num in range(2, last_page_number+1):
                    print(f"pagination: {page_num}")
                    driver.get(parent_link+f"/page/{page_num}/")
                    parent_anchor_tags = driver.find_elements_by_css_selector("h2 a")
                    for child in parent_anchor_tags:
                        # print(f"company_link: {child.get_attribute('href')}")
                        # get_company_info(child.get_attribute('href'))
                        spamwriter.writerow([child.get_attribute("href")])
        except BaseException:
            pass
        
        

    print(company_links)
    driver.quit()
    f.close()
    
