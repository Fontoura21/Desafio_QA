import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

data = pd.read_csv('/Users/fontoura/Documents/Bridge/Testes_Bridge/tests/site/testes_cadastro.csv')

class TestLogin:
    def setup_class(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        logging.info('Webdriver initialized and window maximized.')

    def test_login(self):
        logging.info('Starting test login.')
        driver.get('https://desafio.qa.bridge.ufsc.br/cadastro')
        logging.info('Page loaded: https://desafio.qa.bridge.ufsc.br/cadastro')
        
        field_usuario = driver.find_element(By.ID, 'usuario')
        field_usuario.send_keys('pedrofontouras17@gmail.com')
        logging.info('Entered username.')
        
        field_password = driver.find_element(By.ID, 'password')
        field_password.send_keys('t67YtCAuuboUKMXgltQN93')
        logging.info('Entered password.')
        
        button_checkbox = driver.find_element(By.ID, 'termos-de-uso')
        button_checkbox.click()
        logging.info('Clicked on terms of use checkbox.')
        
        button_acess = driver.find_element(By.CLASS_NAME, 'btn-acessar')
        button_acess.click()
        logging.info('Clicked on access button.')
        
        time.sleep(2)
        button_acess_cadastro = driver.find_element(By.CLASS_NAME, 'btn-acessar')
        button_acess_cadastro.click()
        logging.info('Clicked on access registration button.')
        
        time.sleep(2)
        
        num_tests = 10
        random_indices = np.random.choice(data.index, size=num_tests, replace=False)
        random_rows = data.loc[random_indices]
        
        for _, row in random_rows.iterrows():
            driver.find_element(By.ID, "cpf").clear()
            driver.find_element(By.ID, "cpf").send_keys(str(row['cpf']))
            logging.info(f'Entered CPF: {row["cpf"]}')
            
            driver.find_element(By.ID, "cns").clear()
            driver.find_element(By.ID, "cns").send_keys(str(row['cns']))
            logging.info(f'Entered CNS: {row["cns"]}')
            
            driver.find_element(By.ID, "nome-completo").clear()
            driver.find_element(By.ID, "nome-completo").send_keys(row['nomeCompleto'])
            logging.info(f'Entered full name: {row["nomeCompleto"]}')
            
            driver.find_element(By.ID, "data-nascimento").clear()
            driver.find_element(By.ID, "data-nascimento").send_keys(row['dataNascimento'])
            logging.info(f'Entered date of birth: {row["dataNascimento"]}')
            
            driver.find_element(By.ID, "sexo").clear()
            driver.find_element(By.ID, "sexo").send_keys(row['sexo'])
            logging.info(f'Entered sex: {row["sexo"]}')
            
            driver.find_element(By.ID, "telefone-residencial").clear()
            driver.find_element(By.ID, "telefone-residencial").send_keys(str(row['telefoneResidencial']))
            logging.info(f'Entered home phone: {row["telefoneResidencial"]}')
            
            driver.find_element(By.ID, "telefone-celular").clear()
            driver.find_element(By.ID, "telefone-celular").send_keys(str(row['telefoneCelular']))
            logging.info(f'Entered mobile phone: {row["telefoneCelular"]}')
            
            button_acess_cadastro = driver.find_element(By.CLASS_NAME, 'btn-salvar')
            button_acess_cadastro.click()
            logging.info('Clicked save button.')
            time.sleep(1)

            mensagem = driver.find_element("xpath", '/html/body/div/footer/span')
            logging.info(f'message: {mensagem.text}')

    def teardown_class(self):
        driver.close()
        logging.info('Driver closed.')
