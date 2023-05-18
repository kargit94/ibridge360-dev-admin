import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseFunc


class Counsellingrequest(BaseFunc):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #ELEMENT LOCATORS
    COUNSELLING_REQUEST_BTN='//div/span[text()="Counselling Request"]'
    SEARCH_ELE='//div/input[@placeholder="Search"]'

    def get_counselling_req_btn(self):
        # return self.driver.find_element(By.XPATH,self.COUNSELLING_REQUEST_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.COUNSELLING_REQUEST_BTN)))
    def clickonConsellingrequest(self):
        self.get_counselling_req_btn().click()
        time.sleep(2)

    def get_search_ele(self):
        # return self.driver.find_element(By.XPATH,self.SEARCH_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SEARCH_ELE)))
    def SearchCounsellingreq(self,CRV):
        for x in CRV:
            self.get_search_ele().send_keys(x)
            self.get_search_ele().send_keys(Keys.ENTER)
        time.sleep(2)