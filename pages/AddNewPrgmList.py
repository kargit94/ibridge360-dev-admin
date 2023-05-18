import time

from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseFunc


class AddNewPrgrmlist(BaseFunc):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Element locators:
    ADD_NEW_PRGM_BTN ="//span[text()='Add New Program']"
    PROGRAM_PROFILE_IMG = '//div/input[@id="profiileImage"]'
    PROGRAM_CONTENT_IMG = '//div/input[@id="contentImage"]'
    PROGRAM_NAME_ELE='programName'
    PROGRAM_PATH_ELE='//textarea[@id="addProgramPath"]'
    P_ADD_BTN='//button/span[text()="Add"]'
    PRGM_PATH_VALUE="(//input[@type='text'])[10]"
    PP_DONE_BTN='//button/span[text()="Done"]'
    TOTAL_HR_ELE='//div/textarea[@id="totalHours"]'
    SELECT_COURSE_ELE='//*[@name="selectCourses"]'
    LEARNER_PATH="addProgramLearningPath"
    LADD_BTN='(//span[normalize-space()="Add"])[1]'
    LVALUE_ELE='(//input[@type="text"])[10]'
    LDONE_BTN='//button/span[text()="Done"]'
    SELECT_CAP_ELE='//div/input[@name="capabilityTopics"]'
    PRGM_DURATION_ELE='//div/input[@name="programDuration"]'
    SERVICE_PROVIDER_ELE='//div/input[@name="serviceProvider"]'
    PRGM_START_DATE_ELE='//button[@aria-label="change date"]'
    S_DATE_PICKER_ELE='//p[text()="23"]'
    POK_ELE='//button/span[text()="OK"]'
    PRGM_END_DATE="(//*[name()='svg'][@class='MuiSvgIcon-root'])[16]"
    NEXT_BTN="(//button[@type='button'])[11]"
    YEAR_MONTH_ELE='MuiPickersCalendarHeader-switchHeader'
    E_DATE_PICKER='//p[text()="31"]'
    MENTOR_ELE="(//input[@name='programMentor'])[1]"
    PROGRAM_PRICE_ELE='//div/input[@name="programPrice"]'
    PROGRAM_DESC_ELE= '//textarea[@id="programDescription"]'
    SUBMIT_BTN='//button/span[text()="Submit"]'

    def get_click_addNewPrgm(self):
        # return self.driver.find_element(By.XPATH,self.ADD_NEW_PRGM_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.ADD_NEW_PRGM_BTN)))
    def clickAddNewProgram(self):
        self.get_click_addNewPrgm().click()
        time.sleep(2)

    #input values
    def get_pp_img(self):
        # return self.driver.find_element(By.XPATH,self.PROGRAM_PROFILE_IMG)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PROGRAM_PROFILE_IMG)))
    def PP_img(self):
        return self.get_pp_img().send_keys('C:/Users/91733/Desktop/py1.jpeg')


    def get_PC_img(self):
        # return self.driver.find_element(By.XPATH,self.PROGRAM_CONTENT_IMG)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PROGRAM_CONTENT_IMG)))
    def PC_img(self):
        self.get_PC_img().send_keys('C:/Users/91733/Desktop/py1.jpeg')
        time.sleep(2)

    def get_prgm_name(self):
        # return self.driver.find_element(By.NAME,self.PROGRAM_NAME_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME,self.PROGRAM_NAME_ELE)))
    def AddNewProgram(self, Program_name):
        for x in Program_name:
            self.get_prgm_name().send_keys(x)
        time.sleep(2)

    def get_prgm_path(self):
        # return self.driver.find_element(By.XPATH,self.PROGRAM_PATH_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PROGRAM_PATH_ELE)))
    def PrgmPath(self):
        self.get_prgm_path().click()
        time.sleep(2)

    def get_padd_ele(self):
        # return self.driver.find_element(By.XPATH,self.P_ADD_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.P_ADD_BTN)))
    def PPadd(self):
        self.get_padd_ele().click()
        time.sleep(2)

    def get_pp_value(self):
        # return self.driver.find_element(By.XPATH,self.PRGM_PATH_VALUE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PRGM_PATH_VALUE)))
    def PP(self,valuePP):
        for x in valuePP:
            self.get_pp_value().send_keys(x)
        time.sleep(2)

    def get_ppdone(self):
        # return self.driver.find_element(By.XPATH,self.PP_DONE_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PP_DONE_BTN)))
    def PPdone(self):
        self.get_ppdone().click()
        time.sleep(2)

    def get_totalhr(self):
        # return self.driver.find_element(By.XPATH,self.TOTAL_HR_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.TOTAL_HR_ELE)))
    def Totalhr(self,Total_hours):
        for x in Total_hours:
            self.get_totalhr().send_keys(x)
        time.sleep(2)

    def get_Slcourse(self):
        # return self.driver.find_element(By.XPATH,self.SELECT_COURSE_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SELECT_COURSE_ELE)))
    def Slcourses(self,Courses):
        for i in Courses:
            self.get_Slcourse().send_keys(i)
            self.get_Slcourse().send_keys(Keys.ARROW_DOWN)
            self.get_Slcourse().send_keys(Keys.ENTER)
        time.sleep(2)
    def get_Lpath(self):
        # return self.driver.find_element(By.NAME,self.LEARNER_PATH)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME,self.LEARNER_PATH)))
    def LPath(self):
        self.get_Lpath().click()
        time.sleep(2)

    def get_Ladd_btn(self):
        # return self.driver.find_element(By.XPATH,self.LADD_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.LADD_BTN)))
    def Ladd(self):
        self.get_Ladd_btn().click()
        time.sleep(2)

    def get_lvalue_ele(self):
        # return self.driver.find_element(By.XPATH,self.LVALUE_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.LVALUE_ELE)))
    def Lvalue(self,Lval):
        for x in Lval:
            self.get_lvalue_ele().send_keys(x)
        time.sleep(2)

    def get_ldone_btn(self):
        # return self.driver.find_element(By.XPATH,self.LDONE_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.LDONE_BTN)))
    def Ldone(self):
        self.get_ldone_btn().click()
        time.sleep(2)

    def get_cap_ele(self):
        # return self.driver.find_element(By.XPATH,self.SELECT_CAP_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SELECT_CAP_ELE)))
    def cap(self,SCT_value):
        for x in SCT_value:
            self.get_cap_ele().send_keys(x)
            self.get_cap_ele().send_keys(Keys.ARROW_DOWN)
            self.get_cap_ele().send_keys(Keys.ENTER)
        time.sleep(2)

    def get_prgm_duration_ele(self):
        # return self.driver.find_element(By.XPATH,self.PRGM_DURATION_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PRGM_DURATION_ELE)))
    def Pdur(self,p_duration):
        for x in p_duration:
            self.get_prgm_duration_ele().send_keys(x)
            self.get_prgm_duration_ele().send_keys(Keys.ARROW_DOWN)
            self.get_prgm_duration_ele().send_keys(Keys.ENTER)
        time.sleep(2)

    def get_service_provider_ele(self):
        # return self.driver.find_element(By.XPATH,self.SERVICE_PROVIDER_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SERVICE_PROVIDER_ELE)))
    def Service(self,Prov):
        for x in Prov:
            self.get_service_provider_ele().send_keys(x)
            self.get_service_provider_ele().send_keys(Keys.ARROW_DOWN)
            self.get_service_provider_ele().send_keys(Keys.ENTER)
        time.sleep(2)

    def get_Prgm_start_date(self):
        # return self.driver.find_element(By.XPATH,self.PRGM_START_DATE_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.PRGM_START_DATE_ELE)))
    def Prgrmdate(self,Program_start_date):
        self.get_Prgm_start_date().click()
        time.sleep(2)

    def get_Pdate_picker(self):
        # return self.driver.find_element(By.XPATH,self.S_DATE_PICKER_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.S_DATE_PICKER_ELE)))
    def Pdate_picker(self):
        self.get_Pdate_picker().click()
        time.sleep(2)

    def get_Sok(self):
        # return self.driver.find_element(By.XPATH,self.POK_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.POK_ELE)))
    def sok(self):
        self.get_Sok().click()
        time.sleep(2)

    def get_prgm_end_date(self):
        # return self.driver.find_element(By.XPATH,self.PRGM_END_DATE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.PRGM_END_DATE)))
    def prgm_end_date(self,Program_start_date):
        self.get_prgm_end_date().click()
        time.sleep(2)

    def get_pnext_btn(self):
        # return self.driver.find_element(By.XPATH,self.NEXT_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.NEXT_BTN)))
    def pnxt_btn(self):
        self.get_pnext_btn().click()

    def get_year_month(self):
        # return self.driver.find_elements(By.CLASS_NAME,self.YEAR_MONTH_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,self.YEAR_MONTH_ELE)))
    def year_month(self):
        time.sleep(2)
        while self.get_year_month() != 'May 2023':
            self.get_pnext_btn().click()
            break
        time.sleep(2)

    def get_edate_picker(self):
        # return self.driver.find_element(By.XPATH,self.E_DATE_PICKER)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.E_DATE_PICKER)))
    def Edate_picker(self):
        self.get_edate_picker().click()
        time.sleep(2)

    def get_Eok(self):
       # return self.driver.find_element(By.XPATH,self.EOK)
       return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.POK_ELE)))
    def Eok(self):
       self.get_Eok().click()
       time.sleep(2)

    def get_mentor_ele(self):
        # return self.driver.find_element(By.XPATH,self.MENTOR_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.MENTOR_ELE)))
    def mentor(self,ment):
        for j in ment:
            self.get_mentor_ele().send_keys(j)
            self.get_mentor_ele().send_keys(Keys.ARROW_DOWN)
            self.get_mentor_ele().send_keys(Keys.ENTER)
        time.sleep(2)

    def get_prgm_price(self):
        #return self.driver.find_element(By.XPATH,self.PROGRAM_PRICE_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PROGRAM_PRICE_ELE)))
    def PricePrgm(self,Price):
        for x in Price:
            self.get_prgm_price().send_keys(x)
        time.sleep(2)

    def get_prgm_desc(self):
        # return self.driver.find_element(By.XPATH,self.PROGRAM_DESC_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PROGRAM_DESC_ELE)))
    def prgm_desc(self,desc):
        for y in desc:
            self.get_prgm_desc().send_keys(y)
            time.sleep(2)

    def get_submit_btn(self):
        # return self.driver.find_element(By.XPATH,self.SUBMIT_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SUBMIT_BTN)))
    def submit(self):
       self.get_submit_btn().click()
       time.sleep(2)