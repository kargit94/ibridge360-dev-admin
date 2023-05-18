import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseFunc


class CreateBatch(BaseFunc):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ELEMENT LOCATORS
    CREATE_BATCH_BTN='//*[@id="root"]/div/div/div[2]/div/div/div/div[1]/div/div[1]/button'
    BATCH_TITLE_ELE='//div/input[@name="batchTitle"]'
    SELECT_PROGM_ELE='//div/input[@name="selectPrograms"]'
    BATCH_START_DATE_ELE='(//button[@aria-label="change date"])[1]'
    B_DATE_PICKER_ELE='//p[text()="2"]'
    OK_BTN='//button/span[text()="OK"]'
    BATCH_END_DATE_ELE='(//button[@aria-label="change date"])[2]'
    NEXT_BTN="(//button[@type='button'])[11]"
    YEAR_MONTH_ELE='MuiPickersCalendarHeader-switchHeader'
    E_DATE_PICKER='//p[text()="30"]'
    SUBMIT_BTN='//button/span[text()="Submit"]'


    def get_create_batch_btn(self):
        # return self.driver.find_element(By.XPATH,self.CREATE_BATCH_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.CREATE_BATCH_BTN)))
    def clickCreateBatch(self):
        self.get_create_batch_btn().click()
        time.sleep(2)

    def get_batch_title_ele(self):
        # return self.driver.find_element(By.XPATH,self.BATCH_TITLE_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.BATCH_TITLE_ELE)))
    def inputBatch(self,B_title):
        for x in B_title:
            self.get_batch_title_ele().send_keys(x)
        time.sleep(2)

    def get_select_prgm_ele(self):
        # return self.driver.find_element(By.XPATH,self.SELECT_PROGM_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SELECT_PROGM_ELE)))
    def SDD(self,program):
        for x in program:
            self.get_select_prgm_ele().send_keys(x)
            time.sleep(2)
            self.get_select_prgm_ele().send_keys(Keys.ARROW_DOWN)
            self.get_select_prgm_ele().send_keys(Keys.ENTER)
        time.sleep(2)

    def batch_start_date_ele(self):
        # return self.driver.find_element(By.XPATH,self.BATCH_START_DATE_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.BATCH_START_DATE_ELE)))
    def batch_date(self,Batch_start_date):
        self.batch_start_date_ele().click()
        time.sleep(2)
    def get_Bdate_picker_ele(self):
        # return self.driver.find_element(By.XPATH,self.B_DATE_PICKER_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.B_DATE_PICKER_ELE)))
    def B_date_picker(self):
        self.get_Bdate_picker_ele().click()
        time.sleep(2)

    def get_Bok(self):
        # return self.driver.find_element(By.XPATH,self.BOK_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.OK_BTN)))
    def bok(self):
        self.get_Bok().click()
        time.sleep(2)

    def get_batch_end_date(self):
        # return  self.driver.find_element(By.XPATH,self.BATCH_END_DATE_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.BATCH_END_DATE_ELE)))
    def batch_end_date(self,Batch_end_date):
        self.get_batch_end_date().click()
        time.sleep(2)

    def get_nxt_btn(self):
        # return self.driver.find_element(By.XPATH,self.NEXT_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.NEXT_BTN)))
    def nxt_btn(self):
        self.get_nxt_btn().click()

    def get_year_month_ele(self):
        # return self.driver.find_elements(By.CLASS_NAME,self.YEAR_MONTH_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,self.YEAR_MONTH_ELE)))
    def year_month(self):
        while self.get_year_month_ele() != 'June 2023':
            self.get_nxt_btn().click()
            break
        time.sleep(2)

    def get_E_date_picker(self):
        # return self.driver.find_element(By.XPATH,self.E_DATE_PICKER)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.E_DATE_PICKER)))
    def E_date_picker(self):
        self.get_E_date_picker().click()
        time.sleep(2)

    def get_EOK(self):
        # return self.driver.find_element(By.XPATH,self.EOK)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.OK_BTN)))
    def EOK_ele(self):
        self.get_EOK().click()
        time.sleep(2)

    def get_submit_btn(self):
        # return self.driver.find_element(By.XPATH,self.SUBMIT_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SUBMIT_BTN)))
    def submit(self):
        self.get_submit_btn().click()
        time.sleep(2)