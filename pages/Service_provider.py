import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import BaseFunc


class SearchServiceProvider(BaseFunc):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Element locator:
    SERVICE_PROVIDER_BTN= '//div/span[text()="Service Provider"]'
    SEARCH_SP_VALUE='//div/input[@placeholder="Search"]'
    TABLE_BODY_ELE='//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div/div/table/tbody/tr[1]'
    EIT_BTN='//button/span[text()="Edit"]'
    SAVE_BTN = '//button/span[text()="Save"]'

    def get_service_provider_btn(self):
        # return self.driver.find_element(By.XPATH,self.SERVICE_PROVIDER_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SERVICE_PROVIDER_BTN)))
    def clickServiceProvider(self):
        self.get_service_provider_btn().click()
        time.sleep(2)

    def get_searchSP_value(self):
        # return self.driver.find_element(By.XPATH,self.SEARCH_SP_VALUE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SEARCH_SP_VALUE)))

    def SearchSP(self,SPV):
        for x in SPV:
            self.get_searchSP_value().send_keys(x)
            self.get_searchSP_value().send_keys(Keys.ENTER)
        time.sleep(2)

    def get_tbody(self):
        # return self.driver.find_element(By.XPATH,self.TABLE_BODY_ELE)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.TABLE_BODY_ELE)))
    def tbody(self):
        self.get_tbody().click()
        time.sleep(2)

    def get_edit_btn(self):
        # return self.driver.find_element(By.XPATH,self.EIT_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.EIT_BTN)))
    def clickEdit(self):
        self.get_edit_btn().click()
        time.sleep(2)

    def get_save_btn(self):
        # return self.driver.find_element(By.XPATH,self.SAVE_BTN)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.SAVE_BTN)))
    def clicksave(self):
        self.get_save_btn().click()
        time.sleep(2)





