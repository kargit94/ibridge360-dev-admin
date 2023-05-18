import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseFunc


class AddNewServiceProvider(BaseFunc):
    def __init__(self, driver):
        self.driver = driver

    # ELEMENT LOCATOR:
    NEW_SERVICE_PROVIDER_BTN='//button/span[text()="Add New Service Provider"]'
    IMG_ELE="//div/input[@id='contained-button-file']"
    PROVIDER_NAME_ELE='//div/input[@name="providerName"]'
    EMAIL_ELE= '//div/input[@name="email"]'
    PCN_ELE= '//div/input[@name="contactName"]'
    PH_NO_ELE='//div/input[@name="phoneNumber"]'
    ADDRESS_ELE= '//div/input[@name="address"]'
    CITY_ELE= '//div/input[@name="city"]'
    STATE_ELE='//div/input[@name="state"]'
    ZIP_CODE_ELE='//div/input[@name="zipCode"]'
    PROVIDER_GST_ELE='//div/input[@id="providerGST"]'
    PANCARD_ELE='//div/input[@id="panCard"]'
    SERVICE_DESC_ELE= '//textarea[@id="description"]'
    SUBMIT_BTN= '//button/span[text()="Submit"]'

    def get_addNewSP_btn(self):
        # return self.driver.find_element(By.XPATH,self.NEW_SERVICE_PROVIDER_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.NEW_SERVICE_PROVIDER_BTN)))
    def clickAddNewServiceProvider(self):
        self.get_addNewSP_btn().click()
        time.sleep(2)

    def get_img_ele(self):
        # return self.driver.find_element(By.XPATH,self.IMG_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.IMG_ELE)))
    def Img_ele(self):
        self.get_img_ele().send_keys('C:/Users/91733/Desktop/py1.jpeg')
        time.sleep(2)

    def get_providerName_ele(self):
        # return self.driver.find_element(By.XPATH,self.PROVIDER_NAME_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PROVIDER_NAME_ELE)))
    def providerName(self,P_name):
        for x in P_name:
            self.get_providerName_ele().send_keys(x)
        time.sleep(2)

    def get_email_ele(self):
        # return self.driver.find_element(By.XPATH,self.EMAIL_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.EMAIL_ELE)))
    def email(self,mail):
        for x in mail:
            self.get_email_ele().send_keys(x)
            time.sleep(2)

    def get_PCN_ele(self):
        # return self.driver.find_element(By.XPATH,self.PCN_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PCN_ELE)))
    def PCN(self,contact_name):
        for x in contact_name:
            self.get_PCN_ele().send_keys(x)
        time.sleep(2)

    def get_ph_no_ele(self):
        # return self.driver.find_element(By.XPATH,self.PH_NO_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PH_NO_ELE)))
    def ph_no(self,number):
        for x in number:
            self.get_ph_no_ele().send_keys(x)
        time.sleep(2)

    def get_add_ele(self):
        # return self.driver.find_element(By.XPATH,self.ADDRESS_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.ADDRESS_ELE)))
    def address_ele(self,add):
        for x in add:
            self.get_add_ele().send_keys(x)
        time.sleep(2)

    def get_city_ele(self):
        # return self.driver.find_element(By.XPATH,self.CITY_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.CITY_ELE)))
    def city(self,city_name):
        for x in city_name:
            self.get_city_ele().send_keys(x)
        time.sleep(2)

    def get_state_ele(self):
        # return self.driver.find_element(By.XPATH,self.STATE_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.STATE_ELE)))
    def state_ele(self,st_name):
        for x in st_name:
            self.get_state_ele().send_keys(x)
        time.sleep(2)

    def get_zipcode_ele(self):
        # return self.driver.find_element(By.XPATH,self.ZIP_CODE_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.ZIP_CODE_ELE)))
    def zipcode_ele(self,zc):
        for x in zc:
            self.get_zipcode_ele().send_keys(x)
        time.sleep(2)

    def get_providerGST_ele(self):
        # return self.driver.find_element(By.XPATH,self.PROVIDER_GST_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PROVIDER_GST_ELE)))
    def Provider_GST(self,PGST):
        for x in PGST:
            self.get_providerGST_ele().send_keys(x)
        time.sleep(2)

    def get_pancard_ele(self):
        # return self.driver.find_element(By.XPATH,self.PANCARD_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.PANCARD_ELE)))
    def Pancard_ele(self,Pncrd):
        for x in Pncrd:
            self.get_pancard_ele().send_keys(x)
        time.sleep(2)

    def get_service_desc(self):
        # return self.driver.find_element(By.XPATH,self.SERVICE_DESC_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SERVICE_DESC_ELE)))
    def Service_desc(self,S_desc):
        for x in S_desc:
            self.get_service_desc().send_keys(x)
        time.sleep(2)
    def get_submit_btn(self):
        # return self.driver.find_element(By.XPATH,self.SUBMIT_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SUBMIT_BTN)))
    def submit(self):
        self.get_submit_btn().click()
        time.sleep(2)