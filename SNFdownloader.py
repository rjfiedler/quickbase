import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

SNFcsv = pd.read_csv('SNFcsv.csv')
SNFIDs = SNFcsv['SNF_ID']

def clean(x):
    ID = str(x)
    y = ID.replace(',', '')
    int(y)
    return y

SNFIDs = SNFIDs.apply(clean)
SNFIDs = SNFIDs.astype('int')
print(SNFIDs.head(5))

browser = webdriver.Chrome()
browser.get('http://www.appliedmaterials.com/suppliers')
try:
    Loginelem = browser.find_element_by_link_text('Login')
    print('Found <%s> element' % (Loginelem.text))
except:
    print('no login element found')
Loginelem.click()
try:
    Usernameelem = browser.find_element_by_id('username')
    print('Found <%s> element' % (Usernameelem.tag_name))
except:
    print('no Username element found')
Usernameelem.send_keys('rfiedler@carlton-bates.com')
Passwordelem = browser.find_element_by_id('password')
Passwordelem.send_keys('510Rf327!!!!')
LoginForApplications = browser.find_element_by_id('btnSubmit_6')
LoginForApplications.click()
Proceedelem = browser.find_element_by_id('sn-postauth-proceed_2')
Proceedelem.click()
SupplierPortalelem = browser.find_element_by_partial_link_text('Supplier Portal')
SupplierPortalelem.click()
browser.get('https://esupplier.amat.com/_forms/,DanaInfo=supplierportal+default.aspx?ReturnUrl=%2fsites%2fSNF%2f_layouts%2fAuthenticate.aspx%3fSource%3d%252Fsites%252FSNF%252FSitePages%252FSNF%2520Requests%252Easpx&Source=%2Fsites%2FSNF%2FSitePages%2FSNF%20Requests.aspx')
handle = browser.window_handles
browser.switch_to_window(handle[0])

username = browser.find_element_by_id('ctl00_PlaceHolderMain_signInControl_UserName')
username.send_keys('rfiedler@carlton-bates.com')
password = browser.find_element_by_id('ctl00_PlaceHolderMain_signInControl_password')
password.send_keys('510Rf327!!!!')
Signin = browser.find_element_by_id('ctl00_PlaceHolderMain_signInControl_login')
Signin.click()

toclick = browser.find_element_by_id('ctl00_m_g_edcf72c6_b6b4_43a9_8ff7_d40361e11610_ctl00_ddlParamType1')
toclick.click()
toclick = browser.find_element_by_xpath('//*[@id="ctl00_m_g_edcf72c6_b6b4_43a9_8ff7_d40361e11610_ctl00_ddlParamType1_DropDown"]/div/ul/li[2]')
toclick.click()
searchbox = browser.find_element_by_id('ctl00_m_g_edcf72c6_b6b4_43a9_8ff7_d40361e11610_ctl00_textfield1')
searchbox.send_keys(str(SNFIDs[0]))
search = browser.find_element_by_id('search')
search.click()
print('starting sleep')
time.sleep(15)
print('done sleeping')
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()


for snf in SNFIDs:
    searchbox = browser.find_element_by_id('ctl00_m_g_edcf72c6_b6b4_43a9_8ff7_d40361e11610_ctl00_textfield1')
    searchbox.clear()
    searchbox.send_keys(str(snf))
    search = browser.find_element_by_id('search')
    search.click()
    time.sleep(1)
    link = browser.find_element_by_link_text(str(snf))
    link.click()
    time.sleep(1)
    pyautogui.moveTo(1388, 265)
    pyautogui.click(1388, 265)
    time.sleep(1)
    pyautogui.moveTo(1635, 159)
    pyautogui.click(1635, 159)
    time.sleep(1)


