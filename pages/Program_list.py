import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import BaseFunc


class Programlist(BaseFunc):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Element locators:
    PROGRAM_LIST_BTN = "//div/span[text()='Program List']"
    SEARCH_ELE = "//div/input[@placeholder='Search']"
    PROGRAM_INFO_BTN = '//button/span[text()="Program Info"]'
    EDIT_BTN= '//button/span[text()="Edit"]'
    PROGRAM_PROFILE_IMG = '//div/input[@id="profiileImage"]'
    PROGRAM_CONTENT_IMG = '//div/input[@id="contentImage"]'
    SUBMIT_BTN = '//button/span[text()="Submit"]'
    LSEARCH_ELE = "//input[@placeholder = 'Search']"
    ADD_LEARNER_BTN = '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[6]/button'
    ADD_USER_ELE = '//div/input[@name="selectUser"]'
    SELECT_BATCH_ELE = '//div/input[@name="selectBatch"]'
    LSUBMIT_BTN = '//button/span[text()="Submit"]'

    def get_program_btn(self):
        # return self.driver.find_element(By.XPATH,self.PROGRAM_LIST_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PROGRAM_LIST_BTN)))

    def clickProgramlist(self):
        self.get_program_btn().click()
        time.sleep(2)

        # Search

    def get_search_ele(self):
        # return self.driver.find_element(By.XPATH, self.SEARCH_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.SEARCH_ELE)))

    def searchPrgmList(self, Plname):
        for x in Plname:
            self.get_search_ele().send_keys(x)
        self.get_search_ele().send_keys(Keys.ENTER)
        time.sleep(2)

        # Program Info
    def get_program_info(self):
        # return self.driver.find_element(By.XPATH,self.PROGRAM_INFO_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PROGRAM_INFO_BTN)))
    def clickPrgmInfo(self):
        self.get_program_info().click()
        time.sleep(2)

    def get_edit_btn(self):
        # return self.driver.find_element(By.XPATH,self. EDIT_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self. EDIT_BTN)))
    def clickPIEdit(self):
        self.get_edit_btn().click()
        time.sleep(2)

    def get_add_programProfile_img(self):
        # return self.driver.find_element(By.XPATH,self.PROGRAM_PROFILE_IMG)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PROGRAM_PROFILE_IMG)))
    def clickChooseFile(self):
        # Upload file
        AddProgramProfileImage = self.get_add_programProfile_img().send_keys('C:/Users/91733/Desktop/py1.jpeg')
        time.sleep(2)

    def get_add_content_img(self):
        # return self.driver.find_element(By.XPATH,self.PROGRAM_CONTENT_IMG)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PROGRAM_CONTENT_IMG)))
    def uploadProgramContentImag(self):
        AddProgramContentImage =self.get_add_content_img().send_keys('C:/Users/91733/Desktop/py1.jpeg')
        time.sleep(2)

    def get_submit_btn(self):
        # return self.driver.find_element(By.XPATH,self.SUBMIT_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SUBMIT_BTN)))
    def submit(self):
        Submit =self.get_submit_btn() .click()
        time.sleep(2)

    # Add Learners
    def get_search_lname(self):
        # return self.driver.find_element(By.XPATH,self.LSEARCH_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.LSEARCH_ELE)))
    def SearchLname(self, lname):
        for x in lname:
            self.get_search_lname().send_keys(x)
        self.get_search_lname().send_keys(Keys.ENTER)
        time.sleep(2)

    def get_addlearner_btn(self):
        # return self.driver.find_element(By.XPATH,self.ADD_LEARNER_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.ADD_LEARNER_BTN)))
    def ClickAddLearner(self):
        self.get_addlearner_btn().click()
        time.sleep(2)

    def get_adduser_ele(self):
        # return self.driver.find_element(By.XPATH,self.ADD_USER_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.ADD_USER_ELE)))
    def addUser(self, user):
        for x in user:
            self.get_adduser_ele().send_keys(x)
            self.get_adduser_ele().send_keys(Keys.ARROW_DOWN)
            self.get_adduser_ele().send_keys(Keys.ENTER)
        time.sleep(2)
    def get_select_batch_ele(self):
        # return self.driver.find_element(By.XPATH,self.SELECT_BATCH_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SELECT_BATCH_ELE)))
    def Select_batch(self,bat):
        for y in bat:
            self.get_select_batch_ele().send_keys(y)
            self.get_select_batch_ele().send_keys(Keys.ARROW_DOWN)
            self.get_select_batch_ele().send_keys(Keys.ENTER)
        time.sleep(2)

    def get_lsubmit_btn(self):
        # return self.driver.find_element(By.XPATH,self.LSUBMIT_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.LSUBMIT_BTN)))
    def lsubmit(self):
        submit = self.get_lsubmit_btn().click()
        time.sleep(2)
