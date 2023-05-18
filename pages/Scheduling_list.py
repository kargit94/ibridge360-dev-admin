import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseFunc


class SchedulingList(BaseFunc):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ELEMENT LOCATORS:
    SCHEDULING_LIST_BTN='//div/span[text()="Scheduling List"]'
    SEARCH_ELE='//div/input[@placeholder="Search"]'
    CALENDAR_ICON_BTN="((//*[name()='path'])[23]"
    CROSS_ICON='//*[@id="customized-dialog-title"]/button'
    EDIT_BTN='//button/span[text()="Edit"]'
    SUBMIT_BTN='//div/button[@type="submit"]'


    def get_SL_btn(self):
        # return self.driver.find_element(By.XPATH,self.SCHEDULING_LIST_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SCHEDULING_LIST_BTN)))
    def clickSchedulinglist(self):
        self.get_SL_btn().click()
        time.sleep(2)

    def get_search_ele(self):
        #return self.driver.find_element(By.XPATH,self.SEARCH_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SEARCH_ELE)))
    def searchSL(self,SSL):
        for x in SSL:
            self.get_search_ele().send_keys(x)
            self.get_search_ele().send_keys(Keys.ENTER)
        time.sleep(2)

    def get_calendar_icon(self):
        # return self.driver.find_element(By.XPATH,self.CALENDAR_ICON_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.CALENDAR_ICON_BTN)))
    def calendaricon(self):
        self.get_calendar_icon().click()
        time.sleep(2)

    def get_cross_ele(self):
        # return self.driver.find_element(By.XPATH,self.CROSS_ICON)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.CROSS_ICON)))
    def cross(self):
        self.get_cross_ele().click()
        time.sleep(2)

    def get_edit_btn(self):
        # return self.driver.find_element(By.XPATH,self.EDIT_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.EDIT_BTN)))
    def clickeditSL(self):
        self.get_edit_btn().click()
        time.sleep(2)

    def get_submit_btn(self):
        # return self.driver.find_element(By.XPATH,self.SUBMIT_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SUBMIT_BTN)))
    def submit(self):
        self.get_submit_btn().click()
        time.sleep(2)


