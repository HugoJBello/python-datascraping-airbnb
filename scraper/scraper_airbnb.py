from selenium import webdriver
import sys

from utils_app.util_summary_builder import UtilsSummaryBuilder
from dto.airbnb_entry_dto import AirbnbEntryDTO
from dto.summary_scrapped_dto import SummaryScrappedDTO
import time
import random

#https://www.seleniumhq.org/download/
#14393
#https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

class ScraperAirbnb:

    def __init__(self, urls, checkin, checkout):
        self.urls = urls
        #self.driver = webdriver.Edge()
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Firefox()
        self.data ={}
        self.summaries = {}
        self.checkin = checkin
        self.checkout = checkout
    
    def get_data(self):
        for url in self.urls:
            driver = self.driver
            url = self.update_dates_in_url(url, self.checkin, self.checkout)
            driver.get(url)
            #driver.set_window_position(-4000,0)

            self.get_data_from_page(driver,url)
        driver.close()
       

    def get_data_from_page(self,driver,url_from_db):
        print("obtaining data from " + driver.current_url)
        search_result = self.driver.find_elements_by_xpath("//a[starts-with(@href,'/rooms/')]")
        print(search_result)

        random_int =8573 + random.randint(-3, 3)
        driver.execute_script("window.scrollTo(0, "+str(random_int) +");")
        time.sleep(random.uniform(0.5,0.9))
        self.parse_search_result_item_and_update_data(search_result,url_from_db)

        # print("obtained " + str(len(self.data)) + " entries")
        # time.sleep(random.uniform(0.5,1))

        #if (self.is_next_page()):
        #   print("moving to next page in search")
        #   url=self.driver.find_element_by_xpath("//*[text()='>']").get_attribute("href")
        #   driver.get(url)
        #    self.get_data_from_page(driver,url_from_db)
        #else:
        #   self.get_summary(driver,url_from_db)
            

    def is_next_page(self):
        try:
            controls=self.driver.find_element_by_xpath("//*[text()='>']")
        except:
            return False
        return not controls==None

    def parse_search_result_item_and_update_data(self, search_result_array, url_from_db):
            if(self.data==None): self.data = {}
            if(not url_from_db in self.data.keys()): self.data[url_from_db]=[]

            for result in search_result_array:
                title_small =result.find_element_by_xpath("//span[@class='_1etkxf1']").text.strip()
                title_big = result.find_element_by_xpath("//div[@class='_2izxxhr']").text.strip()
                print("---")
                print(title_small)
                print(title_big)

                #dto=AirbnbEntryDTO(title,prize,meters,rooms,self.driver.current_url,url_element,url_from_db)
                #self.data[url_from_db]=self.data[url_from_db] + [dto]


    def get_summary(self,driver,url_from_db):
        util_summary_builder=UtilsSummaryBuilder(self.data[url_from_db],url_from_db,"")
        util_summary_builder.obtain_summary()
        summary = util_summary_builder.summary
        self.summaries[url_from_db] = summary

    def update_dates_in_url(self, url, checkin, checkout):
        print(url)
        old_checkin = url.split("checkin=")[1].split("&")[0]
        old_checkout = url.split("checkout=")[1].split("&")[0]
        replaced_url = url.replace("checkin=" +old_checkin, "checkin=" + checkin).replace("checkout=" +old_checkout, "checkout=" + checkout)
        print (replaced_url)
        return replaced_url