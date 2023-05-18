from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseFunc():
    def __init__(self,driver):
        self.driver=driver

    def wait_presence_of_element_located(self,name_type,ele_type):
        wait=WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((name_type,ele_type)))

    def presence_of_all_elements_located(self,id_type,ele_type):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located((id_type,ele_type)))