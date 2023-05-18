import time

import pytest
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.AddNewPrgmList import AddNewPrgrmlist
from pages.AddNewSchedulingList import AddNewSchedulingList
from pages.AddNewServiceProvider import AddNewServiceProvider
from pages.Add_New_Coach import AddnewCoach
from pages.Coach_list import coachList
from pages.Counselling_request import Counsellingrequest
from pages.Create_batch import CreateBatch
from pages.Program_list import Programlist
from pages.Scheduling_list import SchedulingList
from pages.Service_provider import SearchServiceProvider
from pages.User_completed_task import UserCompletedTask
from pages.learners import learnerPage
from pages.login_ibridge360_admin_prod import loginIbridge360
from pages.program_batch_list import ProgramBatchList


@ddt
class TestAdminibridge360():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://dev.ibridge360.com")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.XPATH, '//a[@class="jss4" and  text()="Sign In"]').click()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ls = loginIbridge360(self.driver)
        self.lp = learnerPage(self.driver)
        self.cl=coachList(self.driver)
        # self.cl=EditCoachList()
        self.Anc = AddnewCoach(self.driver)
        self.Pl=Programlist(self.driver)
        self.APl=AddNewPrgrmlist(self.driver)
        self.SSP=SearchServiceProvider(self.driver)
        self.ANSP = AddNewServiceProvider(self.driver)
        self.CR=Counsellingrequest(self.driver)
        self.PBL=ProgramBatchList(self.driver)
        self.CB=CreateBatch(self.driver)
        self.SL=SchedulingList(self.driver)
        self.CSL=AddNewSchedulingList(self.driver)
        self.UCT=UserCompletedTask(self.driver)
        self.ut.Utilities()

    @data(('ibridge@gmail.com','Ibridge@2021'))
    @data(('Leena G'))
    @data(('suraj'))
    @data(('James','peterson','james@gmail.com','Password#12','Python','IT','CSS','5years','Bangalore','6','Asia/Kolkata',"Python is a high-level, general-purpose programming language"))
    @data(('React Basics',' ',' '))
    @data(('linux','6 hours','Power BI','React JS',' ',' ','12 months','23-04-2023','30-05-2023',' ','30000','JHF'))
    @data(('Aroha Technologies'))
    @data(('Wipro','wipro1@gmail.co.in','Kumar','0123456789','RV road','Bangalore','Karnataka','560027','123-456-789','ABC-456-789','JHFJH'))
    @data(('veeranna bhrungi'))
    @data((' ','AnkitaBharti',' '))
    @data((' ','02-04-2023','30-06-2023'))
    @data(('New introduction'))
    @data(('Angular basics',' ','02/04/203','26/05/2023','iLearn','JHF'))
    @data(('test123'))
    @unpack
    def test_loginIbridge360(self,username_field,password_field):
        self.ls.loginIbridge360(username_field,password_field)
    def test_learner(self,lname):
        self.lp.learnerPage(lname)
    def test_EditCoachList(self):
        self.cl.EditCoachList()
    def test_coachList(self,sname):
        self.cl.coachList(sname)
    def test_AddnewCoach(self,fname,lname,mail,pwd,ex,ind,sk,exp,loc,hr,tm,desc):
        self.Anc.AddnewCoach(fname,lname,mail,pwd,ex,ind,sk,exp,loc,hr,tm,desc)
    def test_Programlist(self,Plname,lname,user,bat):
        self.Pl.Programlist(Plname,lname,user,bat)
    def test_AddNewPrgrmlist(self,Program_name,valuePP,Total_hours,Courses,Lval,SCT_value,Prov,p_duration,Program_start_date,Program_end_date,ment,Price,desc):
        self.APl.AddNewPrgrmlist(Program_name,valuePP,Total_hours,Courses,Lval,SCT_value,Prov,p_duration,Program_start_date,Program_end_date,ment,Price,desc)
    def test_SearchServiceProvider(self,SPV):
        self.SSP.SearchServiceProvider(SPV)
    def test_AddNewServiceProvider(self,P_name,mail,contact_name,number,add,city_name,st_name,zc,PGST,Pncrd,S_desc):
        self.ANSP.AddNewServiceProvider(P_name,mail,contact_name,number,add,city_name,st_name,zc,PGST,Pncrd,S_desc)
    def test_Counsellingrequest(self,CRV):
        self.CR.Counsellingrequest(CRV)
    def test_ProgramBatchList(self,PBl_value,BUV,users):
        self.PBL.ProgramBatchList(PBl_value,BUV)
    def test_CreateBatch(self,B_title,program,Batch_start_date,Batch_end_date):
        self.CB.CreateBatch(B_title,program,Batch_start_date,Batch_end_date)
    def test_SchedulingList(self,SSL):
        self.SL.SchedulingList(SSL)
    def test_AddNewSchedulingList(self,title,bvalue,Schedule_start_date,Schedule_end_date,t_value,s_d):
        self.CSL.AddNewSchedulingList(title,bvalue,Schedule_start_date,Schedule_end_date,t_value,s_d)
    def test_UserCompletedTask(self,UCTval):
        self.UCT.UserCompletedTask(UCTval)