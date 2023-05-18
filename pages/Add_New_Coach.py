import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseFunc


class AddnewCoach(BaseFunc):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Element locators:
    ADD_NEW_COACH_BTN="//button/span[text()='Add New Coach']"
    CHOOSE_FILE_BTN='//*[@id="contained-button-file"]'
    FIRST_NAME_ELE='firstName'
    LAST_NAME_ELE='lastName'
    EMAIL_ELE='email'
    PASSWORD_ELE='password'
    EXPERT_IN_DROP_DOWN='expertIn'
    INDUSTRY_DROP_DOWN="industry"
    SKILLS_ELE="skills"
    EXPERIENCE_ELE='experience'
    LOCATION_ELE='location'
    WEEKLY_ELE='weekelyAvailableHours'
    PREFFERED_DAYS_ELE='//*[@id="root"]/div/div/div[2]/div[2]/form/div/div[12]'
    SELECT_ALL_VAL='//ul[@class="MuiList-root MuiMenu-list MuiList-padding" and @role="listbox"]/li//div/span[text()="Select All"]'
    PREFFERED_TIME_ELE="//input[@placeholder='Preffered Time *']"
    P_T_VAL='//*[@id="menu-"]/div[3]/ul/li[2]/div[1]/span/span[1]/input'
    TIMEZONE_ELE='timezone'
    DESCRITPTION_ELE='//textarea[@name="description"]'
    SUBMIT_BTN='//button[@type="submit"]'

    def get_addnewcoach(self):
        # return self.driver.find_element(By.XPATH,self.ADD_NEW_COACH_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.ADD_NEW_COACH_BTN)))
    def clickOnAddNewCoach(self):
        self.get_addnewcoach().click()
        time.sleep(2)

    def get_choose_file(self):
        # return self.driver.find_element(By.XPATH, self.CHOOSE_FILE_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.CHOOSE_FILE_BTN)))
    def clickChooseFile(self):
        self.get_choose_file().send_keys('C:/Users/91733/Desktop/py1.jpeg')
        time.sleep(2)

    def get_first_name(self):
        # return self.driver.find_element(By.NAME, self.FIRST_NAME_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, self.FIRST_NAME_ELE)))
    def fn(self,fname):
        for x in fname:
            self.get_first_name().send_keys(x)
        time.sleep(2)

    def get_last_name(self):
        # return self.driver.find_element(By.NAME, self.LAST_NAME_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, self.LAST_NAME_ELE)))
    def ln(self,lname):
        for x in lname:
            self.get_last_name().send_keys(x)
        time.sleep(2)

    def get_email(self):
        # return self.driver.find_element(By.NAME, self.EMAIL_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, self.EMAIL_ELE)))
    def email(self,mail):
        for x in mail:
            self.get_email().send_keys(x)
        time.sleep(2)

    def get_pwd(self):
        # return self.driver.find_element(By.NAME,self.PASSWORD_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME,self.PASSWORD_ELE)))
    def password(self,pwd):
        for x in pwd:
            self.get_pwd().send_keys(x)
        time.sleep(2)

    def get_expert_in(self):
        # return self.driver.find_element(By.NAME, self.EXPERT_IN_DROP_DOWN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, self.EXPERT_IN_DROP_DOWN)))
    def expert(self,ex):
        for x in ex:
            self.get_expert_in().send_keys(x)
        time.sleep(2)

    def get_industry_ele(self):
        # return self.driver.find_element(By.NAME,self.INDUSTRY_DROP_DOWN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME,self.INDUSTRY_DROP_DOWN)))
    def industry(self,ind):
        for x in ind:
            self.get_industry_ele().send_keys(x)
        self.get_industry_ele().send_keys(Keys.ARROW_DOWN)
        self.get_industry_ele().send_keys(Keys.ENTER)
        time.sleep(2)

    def get_skills(self):
        # return self.driver.find_element(By.NAME,self.SKILLS_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME,self.SKILLS_ELE)))
    def skills(self,sk):
        for x in sk:
            self.get_skills().send_keys(x)
        self.get_skills().send_keys(Keys.ARROW_DOWN)
        self.get_skills().send_keys(Keys.ENTER)
        time.sleep(2)

    def get_experience(self):
        # return self.driver.find_element(By.NAME, self.EXPERIENCE_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, self.EXPERIENCE_ELE)))
    def experience(self,exp):
        for x in exp:
            self.get_experience().send_keys(x)
        time.sleep(2)

    def get_location(self):
        # return self.driver.find_element(By.NAME, self.LOCATION_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, self.LOCATION_ELE)))
    def location(self,loc):
        for x in loc:
            self.get_location().send_keys(x)
        time.sleep(2)

    def get_weekly_hr(self):
        # return self.driver.find_element(By.NAME,self.WEEKLY_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME,self.WEEKLY_ELE)))
    def weekely_hr(self,hr):
        for x in hr:
            self.get_weekly_hr().send_keys(x)
        time.sleep(2)

    def get_preferred_days(self):
        # return self.driver.find_element(By.XPATH,self.PREFFERED_DAYS_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PREFFERED_DAYS_ELE)))

    def Preferred_days(self):
        self.get_preferred_days().click()
        time.sleep(2)

    def get_p_d(self):
        # return self.driver.find_element(By.XPATH, self.SELECT_ALL_VAL).selectedIndex="3";
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.SELECT_ALL_VAL)))
    def p_d(self):
        self.get_p_d().click()
        time.sleep(2)

    def get_preferred_time(self):
        # return self.driver.find_element(By.XPATH,self.PREFFERED_TIME_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PREFFERED_TIME_ELE)))
    def preferred_time(self):
        self.get_preferred_time().click()
        time.sleep(2)

    def get_pt(self):
        # return self.driver.find_element(By.XPATH,self. P_T_VAL)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self. P_T_VAL)))
    def p_t(self):
        self.get_pt().click()
        time.sleep(2)

    def get_timezone(self):
        # return self.driver.find_element(By.NAME,self.TIMEZONE_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME,self.TIMEZONE_ELE)))
    def zone(self,tm):
        for x in tm:
            self.get_timezone().send_keys(x)
        self.get_timezone().send_keys(Keys.ARROW_DOWN)
        self.get_timezone().send_keys(Keys.ENTER)
        time.sleep(2)

    def get_desc(self):
        # return self.driver.find_element(By.XPATH,self. DESCRITPTION_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self. DESCRITPTION_ELE)))
    def desc(self,desc_val):
        for x in desc_val:
            self.get_desc().send_keys(x)
            time.sleep(2)

    def get_submit_ele(self):
        # return self.driver.find_element(By.XPATH,self.SUBMIT_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SUBMIT_BTN)))
    def submitNewCoach(self):
        self.get_submit_ele().click()
        time.sleep(2)

