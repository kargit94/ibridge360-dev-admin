import time

from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver

from base.base_class import BaseFunc


class learnerPage(BaseFunc):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Element locators:
    LEARNER_BTN="//div[@class='MuiListItemText-root']//child::span[text()='Learners']"
    SEARCH_ELE='//*[@id="root"]/div/div/div[2]/div/div/div/div[1]/div/div[3]/div/input'

    def get_learner_btn(self):
        # return self.driver.find_element(By.XPATH,self.LEARNER_BTN)
        return WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.LEARNER_BTN)))

    def clickOnLearners(self):
        self.get_learner_btn().click()
        time.sleep(2)

    def get_search_ele(self):
        # return self.driver.find_element(By.XPATH,self.SEARCH_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SEARCH_ELE)))
    def searchLname(self,lname):
        for x in lname:
            self.get_search_ele().send_keys(x)
            self.get_search_ele().send_keys(Keys.ENTER)
            time.sleep(2)


