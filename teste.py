#importando bibliotecas - retirar o time depois
import unittest
import time
from selenium import webdriver

class SiteTestStandard(unittest.TestCase):

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
        time.sleep(2)
        self.nome = self.driver.find_element_by_id("name")
        self.nome.send_keys("Ada Lovelace")
        self.nome.submit()

    #testando o campo email com uma string e esperando 2 segundos
    def test_email(self):
        time.sleep(2)
        self.email = self.driver.find_element_by_id("email")
        self.email.send_keys("Ada@example.com")
        self.email.submit()

    #testando o campo senha com uma senha forte padrao
    def test_senha(self):
        time.sleep(2)
        self.senha = self.driver.find_element_by_id("password")
        self.senha.send_keys("{Ada123}")
        self.senha.submit()
        self.botao = self.driver.find_element_by_class_name('icon').click()

    #testando o botao de acordo e esperando 2 segundos
    def test_agreement(self):
        time.sleep(2)
        self.agreement = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/form/div[4]/div/label/div').click()
    
    #testando o botao de criar conta
    def test_submit(self):
        time.sleep(2)
        self.submit = self.driver.find_element_by_class_name('btn.btn-primary.btn-base').click()

    #encerando a sessao
    @classmethod
    def tearDownClass(self):
        time.sleep(5)
        self.driver.close()
        print("passou no teste basico")
        print('--------------------------------------------------------------------')

class SitetestLinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://staging.app.betrybe.com/registration")
    
    #testando o link de clique aqui
    def test_old_account(self):
        self.conta_antiga = self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div/div[2]/div/div/p/a").click()
        self.url = self.driver.current_url
        print(self.url)

    #testando o link ao clicar na logo
    def test_click_on_simbol(self):
        self.simbol = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div[1]/a').click()
        self.url = self.driver.current_url
        print(self.url)
    
    def tearDown(self):
        self.driver.close()




if __name__ == "__main__":
    unittest.main()