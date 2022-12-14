from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time



driver = webdriver.Chrome(executable_path=r'C:\Users\User\Desktop\payton_prodgect\chromedriver.exe')
driver.maximize_window()



driver.get('https://www.anekdot.ru/')
prekol = driver.find_elements_by_class_name('text')


driver.get('https://mail.ru/')
driver.find_element_by_id('mailbox:login').send_keys('ivanoxenkryt')
driver.find_element_by_id('mailbox:submit').click()
time.sleep(2)
driver.find_element_by_id('mailbox:password').send_keys('qwzerev3')
driver.find_element_by_id('mailbox:submit').click()
time.sleep(5)

driver.get('https://otvet.mail.ru/')
rzaka =  random.choice(prekol)
print(rzaka)



tab = driver.find_elements_by_class_name('q--li--text')
link =  random.choice(tab).get_attribute('href')
driver.get(link)

time.sleep(5)
driver.find_element_by_class_name('autosize_B1kkDlxi').send_keys(str(rzaka))
driver.find_element_by_class_name('btn__submit_1j49aTnK').click()










