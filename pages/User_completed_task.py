import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseFunc

class UserCompletedTask(BaseFunc):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #ELEMENT LOCATORS:
    USER_COMPLETED_TASK_BTN='//div/span[text()="User Completed Tasks"]'
    SEARCH_ELE='//div/input[@placeholder="Search"]'

    def get_UCT(self):
      #return self.driver.find_element(By.XPATH,self.USER_COMPLETED_TASK_BTN)
      return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.USER_COMPLETED_TASK_BTN)))
    def clickUCT(self):
        self.get_UCT().click()
        time.sleep(2)

    def get_search_ele(self):
        #return self.driver.find_element(By.XPATH,self.SEARCH_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SEARCH_ELE)))
    def searchUCT(self,UCTval):
        for x in UCTval:
            self.get_search_ele().send_keys(x)
            self.get_search_ele().send_keys(Keys.ENTER)
        time.sleep(2)