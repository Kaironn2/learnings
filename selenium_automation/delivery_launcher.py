import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DeliveryLauncher:

    def __init__(self):
        self.chromedriver_path = chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()

    
    def login(self, username, password, url):
        self.driver.maximize_window()
        self.driver.get(url)

        username_textfield = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'usuario'))
        )
        username_textfield.send_keys(username)

        password_textfield = self.driver.find_element(By.ID, 'senha')
        password_textfield.send_keys(password)

        login_button = self.driver.find_element(By.ID, 'loginbtn')
        login_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'sidebar-item-inicio'))
        )

    
    def orders_page(self, orders_url, start_date, end_date):
        self.driver.get(orders_url)

        time.sleep(5)

        # Expandindo o filtro
        filter_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'link-pesquisa'))
        )
        filter_button.click()


        # Selecionando o filtro de período
        period_filter = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'opc-periodo'))
        )
        period_filter.click()

        
        # Preenchendo as datas
        start_date_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'data-ini'))
        )
        start_date_field.clear()
        self.driver.execute_script('arguments[0].value = arguments[1];', start_date_field, start_date)

        time.sleep(5)

        end_date_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'data-fim'))
        )
        end_date_field.clear()
        self.driver.execute_script('arguments[0].value = arguments[1];', end_date_field, end_date)

        time.sleep(5)

        # Encolhendo o filtro
        period_filter.click()

        input('Press Enter to continue...')
