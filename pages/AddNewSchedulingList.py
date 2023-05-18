import time
from lib2to3.pgen2 import driver

from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseFunc



class AddNewSchedulingList(BaseFunc):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ELEMENT LOCATORS
    CREATE_SCHEDULE_BTN='//*[@id="root"]/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/button'
    SCHEDULE_TITLE_ELE='//div/input[@name="scheduleTitle"]'
    SCHEDULE_BATCH_ELE='//input[@name="programBatch"]'
    TASK_TYPE_ELE='//div/input[@name="taskType"]'
    SCHEDULE_DESC_ELE='//textarea[@name="scheduleDescription"]'
    SUBMIT_BTN= "//button//child::span[text()='Submit']"
    CALENDAR_DATE_ELE= '//div/input[@name="scheduleStartDate"]'
    START_DATE_PICKER_ELE='//p[text()="2"]'
    SOURCE_ELE='MuiPickersClock-pin'
    TARGET_ELE='//div/span[text()="3"]'
    SOURCE_ELE_HR='MuiPickersClock-pin'
    TARGET_ELEMENT_HR= '//div/span[text()="15"]'
    OK_BTN='//span[@class="MuiButton-label" and text()="OK"]'
    SCHEDULE_END_DATE='//input[@name="scheduleEndDate"]'
    NEXT_BTN="(//*[name()='svg'][@class='MuiSvgIcon-root'])[26]"
    YEAR_MONTH_ELE='MuiPickersBasePicker-container'
    END_DATE_PICKER='//p[text()="23"]'
    ESOURCE_ELE='MuiPickersClock-pin'
    ETARGET_ELE='//div/span[text()="3"]'
    HSOURCE_ELE='MuiPickersClock-pin'
    HTARGET_ELE='//div/span[text()="15"]'


    # Create schedule
    def get_create_schedule_btn(self):
        #return self.driver.find_element(By.XPATH,self.CREATE_SCHEDULE_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.CREATE_SCHEDULE_BTN)))
    def clickCreateSchedule(self):
        self.get_create_schedule_btn().click()
        time.sleep(2)

    def get_schedule_title(self):
        # return self.driver.find_element(By.XPATH,self.SCHEDULE_TITLE_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SCHEDULE_TITLE_ELE)))
    def inputSL(self,title):
        for x in title:
            self.get_schedule_title().send_keys(x)
        time.sleep(2)

    def get_schedule_batch(self):
        # return self.driver.find_element(By.XPATH,self.SCHEDULE_BATCH_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SCHEDULE_BATCH_ELE)))
    def Sbtch(self,bvalue):
        for x in bvalue:
            self.get_schedule_batch().send_keys(x)
            self.get_schedule_batch().send_keys(Keys.ARROW_DOWN)
            self.get_schedule_batch().send_keys(Keys.ENTER)
        time.sleep(2)

    def get_task_type(self):
        # return self.driver.find_element(By.XPATH,self.TASK_TYPE_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.TASK_TYPE_ELE)))
    def task_type(self,t_value):
        for x in t_value:
            self.get_task_type().send_keys(x)
            self.get_task_type().send_keys(Keys.ARROW_DOWN)
            self.get_task_type().send_keys(Keys.ENTER)
            time.sleep(2)

    def get_s_desc(self):
        # return self.driver.find_element(By.XPATH,self.SCHEDULE_DESC_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SCHEDULE_DESC_ELE)))
    def s_desc(self, s_d):
        for x in s_d:
            self.get_s_desc().send_keys(x)
            time.sleep(2)

    def get_submit_ele(self):
        # return self.driver.find_element(By.XPATH,self.SUBMIT_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SUBMIT_BTN)))
    def submit(self):
        self.get_submit_ele().click()
        time.sleep(2)

    def get_schedule_date(self):
        return self.driver.find_element(By.XPATH,self.CALENDAR_DATE_ELE)
    def Schedule_date(self,Schedule_start_date,Schedule_end_date):
        self.get_schedule_date().click()

    def get_start_date_picker(self):
        return self.driver.find_element(By.XPATH,self.START_DATE_PICKER_ELE)
    def start_date_picker(self):
        self.get_start_date_picker().click()
        time.sleep(2)

    def get_source_ele(self):
        return self.driver.find_element(By.CLASS_NAME,self.SOURCE_ELE)
    def source_ele_min(self):
        self.get_source_ele()
    def get_target_ele_min(self):
        return self.driver.find_element(By.XPATH,self.TARGET_ELE)
    def target_ele_min(self):
        time.sleep(2)
        action = ActionChains(self.driver)
        action.drag_and_drop(self.SOURCE_ELE, self.TARGET_ELE).click().perform()
        time.sleep(2)
        source_ele_hr = self.driver.find_element(By.CLASS_NAME,self.SOURCE_ELE_HR)
        target_ele_hr = self.driver.find_element(By.XPATH,self.TARGET_ELEMENT_HR)
        time.sleep(2)
        action = ActionChains(self.driver)
        action.drag_and_drop(self.SOURCE_ELE_HR, self.TARGET_ELEMENT_HR).click().perform()
        time.sleep(2)
        OK = self.driver.find_element(By.XPATH,self.OK_BTN).click()
        time.sleep(2)
    def get_scheduel_edate(self):
        return self.driver.find_element(By.XPATH,self.SCHEDULE_END_DATE).click()
    def scheduel_edate(self):
       self.get_scheduel_edate()
       time.sleep(2)
    def get_nxt_btn(self):
        return self.driver.find_element(By.XPATH,self.NEXT_BTN)
    def nxt_btn(self):
        self.get_nxt_btn().click()
        year_month = self.driver.find_elements(By.CLASS_NAME,self.YEAR_MONTH_ELE)
        time.sleep(5)
        while self.YEAR_MONTH_ELE != 'March 2023':
            self.NEXT_BTN.click()
            break
        time.sleep(2)
        End_date_picker = self.driver.find_element(By.XPATH,self.END_DATE_PICKER).click()
        time.sleep(5)
        Esource_ele_min = self.driver.find_element(By.CLASS_NAME,self.ESOURCE_ELE)
        Etarget_ele_min = self.driver.find_element(By.XPATH,self. ETARGET_ELE)
        time.sleep(2)
        action = ActionChains(self.driver)
        action.drag_and_drop(Esource_ele_min, Etarget_ele_min).click().perform()
        time.sleep(2)
        Hsource_ele_hr = self.driver.find_element(By.CLASS_NAME,self.HSOURCE_ELE)
        Htarget_ele_hr = self.driver.find_element(By.XPATH,self.HTARGET_ELE)
        time.sleep(2)
        action = ActionChains(self.driver)
        action.drag_and_drop(self.HSOURCE_ELE, self.HTARGET_ELE).click().perform()
        time.sleep(2)
        E_OK = self.driver.find_element(By.XPATH,self.OK_BTN).click()
        time.sleep(2)

