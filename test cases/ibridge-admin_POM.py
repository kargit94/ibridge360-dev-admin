import time

import self
import softest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#driver=webdriver.Chrome(executable_path="E:\\Ibridge automation\chromedriver")
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


class Adminibridge360():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://dev.ibridge360.com")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.XPATH, '//a[@class="jss4" and  text()="Sign In"]').click()
    def test_ibridge(self):

        # Login
        ls=loginIbridge360(self.driver)
        username_field='ibridge@gmail.com'
        ls.login_ibridge(username_field)
        password_field = 'Ibridge@2021'
        ls.pwd_ele(password_field)

        # Clicking on the 'Login' button
        ls.click_loginBtn()

        #click on Learners tab
        lp = learnerPage(self.driver)
        lp.clickOnLearners()

        # Search in Learners tab
        # lname='Leena G'
        # lp.searchLname(lname)

        #Coach list tab
        cl=coachList(self.driver)
        cl.clickOnCoachList()

        # Click on Add New coach Btn
        Anc = AddnewCoach(self.driver)
        Anc.clickOnAddNewCoach()

        # upload file
        Anc.clickChooseFile()

        fname = 'James'
        Anc.fn(fname)
        lname = 'peterson'
        Anc.ln(lname)
        mail = 'james@gmail.com'
        Anc.email(mail)
        pwd = 'Password#12'
        Anc.password(pwd)
        ex='Python'
        Anc.expert(ex)
        ind = 'IT'
        Anc.industry(ind)
        sk = 'CSS'
        Anc.skills(sk)
        exp = '5years'
        Anc.experience(exp)
        loc = 'Bangalore'
        Anc.location(loc)
        hr = '6'
        Anc.weekely_hr(hr)

        Anc.Preferred_days()
        Anc.p_d()
        Anc.preferred_time()
        Anc.p_t()
        tm='Asia/Kolkata'
        Anc.zone(tm)
        desc = "Python is a high-level, general-purpose programming language"
        Anc.desc(desc)
        Anc.submitNewCoach()

        # Search coach list
        sname='suraj'
        cl.SearchCoachList(sname)
        cl.clicktable()

        #Edit the coach list
        cl.EditCoachList()

        # upload files
        cl.uploadCL()
        cl.SubmitEditedCoachList()


        #Program List
        # Pl=Programlist(self.driver)
        # Pl.clickProgramlist()

        #Search
        # Plname='React Basics'
        # Pl.searchPrgmList(Plname)

        #click on prgm info
        # Pl.clickPrgmInfo()
        # Pl.clickPIEdit()
        # Pl.clickChooseFile()
        # Pl.uploadProgramContentImag()
        # Pl.AddProgramProfileImageself='C:/Users/91733/Desktop/py1.jpeg'
        # Pl.AddProgramContentImage='C:/Users/91733/Desktop/py1.jpeg'
        # Pl.submit()

        #Add Learners
        # lname='React Basics'
        # Pl.SearchLname(lname)

        #click on add learners
        # Pl.ClickAddLearner()
        # user=' '
        # Pl.addUser(user)
        # bat = ' '
        # Pl.Select_batch(bat)
        # Pl.lsubmit()

        #Add New Program
        # APl=AddNewPrgrmlist(self.driver)
        # APl.clickAddNewProgram()
        # APl.PP_img()
        # APl.PC_img()
        # Program_name='Cyber Security'
        # APl.AddNewProgram(Program_name)

        # add program path
        # APl.PrgmPath()
        # APl.PPadd()
        # valuePP='linux'
        # APl.PP(valuePP)
        # APl.PPdone()
        # Total_hours = '6 hours'
        # APl.Totalhr(Total_hours)
        # Courses='Power BI'
        # APl.Slcourses(Courses)
        # APl.LPath()
        # APl.Ladd()
        # Lval='React JS'
        # APl.Lvalue(Lval)
        # APl.Ldone()
        # SCT_value=' '
        # APl.cap(SCT_value)
        # Prov = ' '
        # APl.Service(Prov)
        # p_duration='12 months'
        # APl.Pdur(p_duration)
        # Program_start_date='23-04-2023'
        # APl.Prgrmdate(Program_start_date)
        # APl.Pdate_picker()
        # APl.sok()
        # Program_end_date = '30-05-2023'
        # APl.prgm_end_date(Program_end_date)
        # APl.pnxt_btn()
        # APl.year_month()
        # APl.Edate_picker()
        # APl.Eok()
        # ment=' '
        # APl.mentor(ment)
        # Price = '30000'
        # APl.PricePrgm(Price)
        # desc = 'JHF'
        # APl.prgm_desc(desc)
        # APl.submit()

        #Service Provider
        # SSP=SearchServiceProvider(self.driver)
        # SSP.clickServiceProvider()


        #Add New Service provider
        # ANSP = AddNewServiceProvider(self.driver)
        # ANSP.clickAddNewServiceProvider()
        # ANSP.Img_ele()
        # P_name='Wipro'
        # ANSP.providerName(P_name)
        # mail='wipro1@gmail.co.in'
        # ANSP.email(mail)
        # contact_name='Kumar'
        # ANSP.PCN(contact_name)
        # number='0123456789'
        # ANSP.ph_no(number)
        # add='RV road'
        # ANSP.address_ele(add)
        # city_name='Bangalore'
        # ANSP.city(city_name)
        # st_name='Karnataka'
        # ANSP.state_ele(st_name)
        # zc='560027'
        # ANSP.zipcode_ele(zc)
        # PGST='123-456-789'
        # ANSP.Provider_GST(PGST)
        # Pncrd='ABC-456-789'
        # ANSP.Pancard_ele(Pncrd)
        # S_desc='JHFJH'
        # ANSP.Service_desc(S_desc)
        # ANSP.submit()

        # SPV = 'Aroha Technologies'
        # SSP.SearchSP(SPV)
        # SSP.tbody()

        # Edit SP
        # SSP.clickEdit()
        # SSP.clicksave()

        #Counselling Request
        # CR=Counsellingrequest(self.driver)
        # CR.clickonConsellingrequest()
        # CRV='veeranna bhrungi'
        # CR.SearchCounsellingreq(CRV)

        # Program batch list
        # PBL=ProgramBatchList(self.driver)
        # PBL.clickonPBL()
        # PBl_value=' '
        # PBL.SearchPB(PBl_value)
        # PBL.clicktablerow()
        # BUV='AnkitaBharti'
        # PBL.serchBU(BUV)
        # PBL.clickRemove()

        # Add user
        # PBL.clickABlist()
        # users=' '
        # PBL.Adduser(users)
        # PBL.AUsubmit()

        #Create Batch
        # CB=CreateBatch(self.driver)
        # CB.clickCreateBatch()
        # B_title='testing batch2'
        # CB.inputBatch(B_title)
        # program=' '
        # CB.SDD(program)
        # Batch_start_date='02-04-2023'
        # CB.batch_date(Batch_start_date)
        # CB.B_date_picker()
        # CB.bok()

        # Batch_end_date = '30-06-2023'
        # CB.batch_end_date(Batch_end_date)
        # CB.nxt_btn()
        # CB.year_month()
        # CB.E_date_picker()
        # CB.EOK_ele()
        # CB.submit()

        #Scheduling list
        # SL=SchedulingList(self.driver)
        # SL.clickSchedulinglist()
        # SSL='New introduction'
        # SL.searchSL(SSL)
        # SL.calendaricon()
        # SL.cross()
        # SL.clickeditSL()
        # SL.submit()

    #Create schedule
        # CSL=AddNewSchedulingList(self.driver)
        # CSL.clickCreateSchedule()
        # title='Angular basics'
        # CSL.inputSL(title)

        # bvalue=' '
        # CSL.Sbtch(bvalue)
        # Schedule_start_date='02/04/203'
        # Schedule_end_date='26/05/2023'
        # CSL.Schedule_date(Schedule_start_date, Schedule_end_date)
        # t_value='iLearn'
        # CSL.task_type(t_value)
        # s_d = 'JHF'
        # CSL.s_desc(s_d)
        # CSL.submit()

        # User completed Task
        UCT=UserCompletedTask(self.driver)
        UCT.clickUCT()
        UCTval='test123'
        UCT.searchUCT(UCTval)

iobj=Adminibridge360()
iobj.test_ibridge()