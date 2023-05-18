import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseFunc


class ProgramBatchList(BaseFunc):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ELEMENT LOCATORS
    PROGRAM_BATCH_LIST_BTN='//div/span[text()="Program Batch List"]'
    SEARCH_ELE='//div/input[@placeholder="Search"]'
    TABLE_ELE='//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[1]'
    SEARCH_BATCH_ELE='//div/input[@placeholder="Search"]'
    REMOVE_BTN='//div/input[@placeholder="Search"]'
    ADD_USER_BTN="//button/span[text()='Add User to Batch']"
    USER_DD="//div/input[@name='selectUser']"
    SUBMIT_BTN="//button/span[text()='Submit']"

    def get_PBL_btn(self):
        # return self.driver.find_element(By.XPATH,self.PROGRAM_BATCH_LIST_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PROGRAM_BATCH_LIST_BTN)))
    def clickonPBL(self):
       self.get_PBL_btn().click()
       time.sleep(2)

    def get_search_ele(self):
        # return self.driver.find_element(By.XPATH,self.SEARCH_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SEARCH_ELE)))
    def SearchPB(self,PBl_value):
        for x in PBl_value:
            self.get_search_ele().send_keys(x)
            self.get_search_ele().send_keys(Keys.ENTER)
        time.sleep(2)

    def get_table_ele(self):
        # return self.driver.find_element(By.XPATH,self.TABLE_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.TABLE_ELE)))
    def clicktablerow(self):
        self.get_table_ele().click()
        time.sleep(2)

    def get_search_batch(self):
        # return self.driver.find_element(By.XPATH,self.SEARCH_BATCH_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SEARCH_BATCH_ELE)))
    def serchBU(self,BUV):
        for x in BUV:
            self.get_search_batch().send_keys(x)
            self.get_search_batch().send_keys(Keys.ENTER)
        time.sleep(2)

    def get_remove_btn(self):
        # return self.driver.find_element(By.XPATH,self.REMOVE_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.REMOVE_BTN)))
    def clickRemove(self):
        self.get_remove_btn().click()
        time.sleep(2)

    def get_UBL_btn(self):
       # return self.driver.find_element(By.XPATH,self.ADD_USER_BTN)
       return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.ADD_USER_BTN)))
    def clickABlist(self):
        self.get_UBL_btn().click()
        time.sleep(2)

    def get_User_ele(self):
       # return self.driver.find_element(By.XPATH,self.USER_DD)
       return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.USER_DD)))
    def Adduser(self,users):
        for x in users:
            self.get_User_ele().send_keys(x)
            self.get_User_ele().send_keys(Keys.ARROW_DOWN)
            self.get_User_ele().send_keys(Keys.ENTER)
            time.sleep(2)

    def get_submit_ele(self):
        # return self.driver.find_element(By.XPATH,self.SUBMIT_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SUBMIT_BTN)))
    def AUsubmit(self):
        self.get_submit_ele().click()
        time.sleep(2)



