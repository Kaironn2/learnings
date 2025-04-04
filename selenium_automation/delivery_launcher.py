import time

from typing import Optional, Union, List, Dict, Any

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


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

        self.driver.execute_script("document.body.style.zoom='70%'")

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


        print('Aguardando 5 segundos para preencher a data inicio...')
        time.sleep(5)

        
        # Preenchendo as datas
        start_date_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'data-ini'))
        )
        start_date_field.clear()
        self.driver.execute_script('arguments[0].value = arguments[1];', start_date_field, start_date)

        print('Aguardando 5 segundos para preencher a data fim...')
        time.sleep(5)


        end_date_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'data-fim'))
        )
        end_date_field.clear()
        self.driver.execute_script('arguments[0].value = arguments[1];', end_date_field, end_date)

        print('Aguardando 5 segundos para encolher o filtro...')
        time.sleep(5)

        # Encolhendo o filtro
        period_filter.click()

        print('Aguardando 5 segundos para prosseguir para a pesquisa...')
        time.sleep(5)

        period_filter.click()
        time.sleep(1)

        input('Aperte enter para continuar...')


    def search_and_launch(self, order, delivery_date) -> Union[bool, str, str]:
        # Preenchendo o campo de pedido
        search_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'pesquisa-mini'))
        )
        search_field.clear()
        search_field.send_keys(order + Keys.ENTER)

        # Aguardando a página carregar
        # WebDriverWait(self.driver, 10).until(lambda d: d.find_element(By.TAG_NAME, 'body').get_attribute('style') == 'cursor: default;')
        time.sleep(2.5)
        
        # Expandindo as opções do funil do pedido
        options_funnel = self.driver.find_element(By.CSS_SELECTOR, "div[id^='button-navigate-'] button.button-navigate-funil")
        options_funnel.click()
        
        try:
            delivery_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'modalEntrega'))
            )
            input('Aguardando...')
            self.driver.execute_script('arguments[0].click();', delivery_button)
            # delivery_button.click()
        except TimeoutException:
            return False, order, delivery_date
        
        date_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'dataEntregaModal'))
        )
        self.driver.execute_script('arguments[0].value = arguments[1];', date_field, delivery_date)

        save_delivery_button = self.driver.find_element(By.XPATH, '//*[@id="modalEntrega"]/div[3]/button[2]')
        save_delivery_button.click()

        time.sleep(5)
        return True, order, delivery_date
