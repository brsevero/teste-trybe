#importando bibliotecas - retirar o time depois
import unittest
import time
from selenium import webdriver

class SiteTest(unittest.TestCase):

    #criando uma sessao do chrome nova "chromedriver precisa estar no mesmo local do python"
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        #navegando ate o site e esperando o caregamento
        self.driver.get("https://staging.app.betrybe.com/registration")
        self.driver.implicitly_wait(5)

    #testando o campo nome com uma string padrao e esperando 2 segundos
    def test_name(self):
        self.nome = self.driver.find_element_by_id("name")
        self.nome.send_keys("Ada Lovelace")
        self.nome.submit()
        time.sleep(2)

    #testando o campo email com uma string e esperando 2 segundos
    def test_email(self):
        self.email = self.driver.find_element_by_id("email")
        self.email.send_keys("Ada@example.com")
        self.email.submit()
        time.sleep(2)

    #testando o campo senha com uma senha forte padrao
    def test_senha(self):
        self.senha = self.driver.find_element_by_id("password")
        self.senha.send_keys("{Ada123}")
        self.senha.submit()
        self.botao = self.driver.find_element_by_class_name('icon').click()
        time.sleep(2)

    #testando o botao de acordo e esperando 2 segundos
    def test_agreement(self):
        self.agreement = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/form/div[4]/div/label/div').click()
        time.sleep(2)


    '''
    def test_old_account(self):
        self.conta_antiga = self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div/div[2]/div/div/p/a")
        self.conta_antiga.send_keys(Keys.RETURN)
        time.sleep(5)'''

    #encerando a sessao
    @classmethod
    def tearDownClass(self):
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()