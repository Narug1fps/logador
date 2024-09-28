from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re


driver_path = './chromedriver.exe'


login_url = 'https://cas.correios.com.br/login?service=https%3A%2F%2Fmeucorreios.correios.com.br%2Fcore%2Fseguranca%2Fservice.php'


service = Service(driver_path)


driver = webdriver.Chrome(service=service)

def check_pending_package(username, password):
    driver.get(login_url)
    
    username_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')
    
    username_input.send_keys(username)
    password_input.send_keys(password)
    
    password_input.send_keys(Keys.RETURN)
    
    time.sleep(5)  


with open("message.txt", "r") as file:
    
    for line in file:
        message = line.strip()  
        if message:  
            username = re.match(r'^[^:]+', message).group().strip()
            password = re.search(r'(?<=:).+', message).group().strip()
            print(username, password)
            check_pending_package(username, password)


driver.quit()
