from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class TestLogin:
    #def = funcao
    def setup_class(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
    time.sleep(2)
    def test_login(self):
    #define qual pagina deve abrir
        driver.get('https://github.com')

        #Procuramos pelo link de login
        btn_link_sign_in = driver.find_element(By.CLASS_NAME, 'HeaderMenu-link--sign-in')
        #Simulamos o clique no link
        btn_link_sign_in.click()

        #Realizamos uma captura de tela
        driver.save_screenshot('screen_00.png')

        #Aguarda dois segundos
        time.sleep(2)

        field_login = driver.find_element(By.ID, 'login_field')
        field_login.send_keys('imporer45')

        field_password = driver.find_element(By.ID, 'password')
        field_password.send_keys('326598741t5*')

        #Realizamos uma captura de tela
        driver.save_screenshot('screen_01.png')

        field_password.send_keys(Keys.RETURN)

        #Aguarda dois segundos
        time.sleep(2)

        #Realizamos uma captura de tela
        driver.save_screenshot('screen_02.png')

    #fecha o browser
    def teardown_class(self):
        driver.close()