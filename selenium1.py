import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
driver = webdriver.Chrome(executable_path='C:\\Users\\Panda\\Desktop\\selenio\\chromedriver.exe')
driver.get("http://localhost:8121") 
#elemento1 nombre de usuario
elemento1 = driver.find_element(By.ID, "user") 
elemento1.clear() 
elemento1.send_keys("root") 

#elemento2 password
elemento2 = driver.find_element(By.XPATH, "//*[@id='login']/div[2]/div[2]/input") 
elemento2.clear() 
elemento2.send_keys("password") 
driver.find_element(By.XPATH, "//*[@id='login']/div[3]/div/input").click() 
driver.get("http://localhost:8121") 
time.sleep(10) 

#elemento3 botón
driver.find_element(By.XPATH, "//*[@id='CreateTicketInQueue']/div[1]/input").click() 
time.sleep(10) 

#elemento4 campo del ticket
elemento4 = driver.find_element(By.XPATH, "//*[@id='TitleBox--_Ticket_Create_html--messagedetails----Q3JlYXRlIGEgbmV3IHRpY2tldCBpbiBHZW5lcmFs---0']/div/div/div[4]/div[2]/input") 
elemento4.send_keys("Selenium RT")  

#crear ticket
driver.find_element(By.XPATH, "//*[@id='SubmitTicket']/div[2]/input").click() 
driver.close()
