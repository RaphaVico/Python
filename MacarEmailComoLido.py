import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

url = 'https://accounts.google.com'
email = 'seuemail@gmail.com'
senha = 'suasenha'
driver = webdriver.Chrome()


if __name__ == '__main__':
############### LOGIN NO EMAIL ##################

    driver.get('http://www.gmail.com.br')
    login = driver.find_element_by_xpath('//*[@id="identifierId"]')
    login.send_keys(email, Keys.RETURN)
    time.sleep(3)
    pasw = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    pasw.send_keys(senha, Keys.RETURN)

    time.sleep(2)
#################### MARCA EMAIL COMO LIDOS ##################
    while True:
        
        mais = driver.find_element_by_xpath('//*[@id=":33"]/span').click()
        time.sleep(0.2)
        marcar = driver.find_element_by_xpath('//*[@id=":kr"]/div').click()  
        time.sleep(1)
        numero = driver.find_element_by_xpath('//*[@id=":il"]/span/span[1]/span[2]')
        if numero.text == '5.548':
            break
        proximo = driver.find_element_by_xpath('//*[@id=":io"]/img').click()
        time.sleep(1)

             
    
    driver.close()
