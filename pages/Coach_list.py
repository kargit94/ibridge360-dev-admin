import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseFunc


class coachList(BaseFunc):
    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)
        self.driver = driver
    # Element locators:
    COACH_LIST_BTN='//div/span[text()="Coach List"]'
    SEARCH_ELE="//*[@id='root']/div/div/div[2]/div/div/div/div[1]/div/div[3]/div/input"
    TABLE_ELE='//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[1]'
    EDIT_BTN="//button/span[text()='Edit']"
    IMG_ELE='//*[@id="contained-button-file"]'
    SUBMIT_BTN='//button/span[text()="Submit"]'

    def get_coachlist_btn(self):
        # return self.driver.find_element(By.XPATH,self.COACH_LIST_BTN)
        return WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.COACH_LIST_BTN)))
    def clickOnCoachList(self):
        self.get_coachlist_btn().click()
        time.sleep(2)

    def get_search_ele(self):
        # return self.driver.find_element(By.XPATH, self.SEARCH_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.SEARCH_ELE)))
    def SearchCoachList(self,sname):
        for x in sname:
            self.get_search_ele().send_keys(x)
        self.get_search_ele().send_keys(Keys.ENTER)
        time.sleep(2)

    def get_table_ele(self):
        # return self.driver.find_element(By.XPATH,self.TABLE_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.TABLE_ELE)))
    def clicktable(self):
        self.get_table_ele().click()
        time.sleep(2)

    # Edit the coach list
    def get_edit_btn(self):
        # return self.driver.find_element(By.XPATH,self.EDIT_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.EDIT_BTN)))
    def EditCoachList(self):
        self.get_edit_btn().click()
        time.sleep(2)

    def get_img_ele(self):
        # return self.driver.find_element(By.XPATH,self.IMG_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.IMG_ELE)))
    def uploadCL(self):
        #upload files
        self.get_img_ele().send_keys('C:/Users/91733/Desktop/py1.jpeg')
        time.sleep(2)

    def get_submit_ele(self):
        # return self.driver.find_element(By.XPATH,self.SUBMIT_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SUBMIT_BTN)))
    def SubmitEditedCoachList(self):
        self.get_submit_ele().click()
        time.sleep(2)






