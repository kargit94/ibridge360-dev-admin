import time

from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseFunc


class loginIbridge360(BaseFunc):
    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)
        self.driver = driver


    #ELEMENT LOCATORS:
    USER_FIELD_ELE='email'
    PASSWORD_ELE='password'
    LOGIN_BTN='MuiButton-label'

    def get_user_filed_ele(self):
        # return self.driver.find_element(By.NAME,self.USER_FIELD_ELE)
        return WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.NAME,self.USER_FIELD_ELE)))
    def login_ibridge(self,username_field):
        for x in username_field:
            self.get_user_filed_ele().send_keys(x)
        time.sleep(2)

    def get_pwd_ele(self):
        #return self.driver.find_element(By.NAME,self.PASSWORD_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME,self.PASSWORD_ELE)))
    def pwd_ele(self,password_field):
        for x in password_field:
            self.get_pwd_ele().send_keys(x)
        time.sleep(2)

    def get_logn_btn(self):
        #return self.driver.find_element(By.CLASS_NAME,self.LOGIN_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,self.LOGIN_BTN)))
    def click_loginBtn(self):
        self.get_logn_btn().click()
        time.sleep(1)

    def loginIbridge360(self, username_field, password_field):
        pass



