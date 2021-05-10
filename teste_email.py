from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import unittest

def set_chrome_options() -> None:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

class TesteEmail(unittest.TestCase):

    #criando uma sessao do chrome
    def setUp(self):
        self.driver = webdriver.Chrome(options=set_chrome_options())

        #navegando ate o site e esperando o carregamento
        self.driver.get("https://staging.app.betrybe.com/registration")

    #teste com o email feito apenas de numeros e com o padrao de email
    def test_3(self):
        self.nome = self.driver.find_element_by_id("name")
        self.nome.send_keys("Ada lovelace")
        self.nome.submit()

        self.email = self.driver.find_element_by_id("email")
        self.email.send_keys("12345678@exemple.com")
        self.email.submit()

        self.senha = self.driver.find_element_by_id("password")
        self.senha.send_keys("{Ada123}")
        self.senha.submit()
        self.botao = self.driver.find_element_by_class_name('icon').click()

        self.agreement = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/form/div[4]/div/label/div').click()

        self.submit = self.driver.find_element_by_class_name('btn.btn-primary.btn-base').click()
        time.sleep(10)
        self.url = self.driver.current_url
        #print("Url do teste 3 :" + self.url)
        self.assertEqual(self.url,"https://staging.app.betrybe.com/registration")

    #teste com o email apenas de numeros e sem o padrao de email
    def test_4(self):
        self.nome = self.driver.find_element_by_id("name")
        self.nome.send_keys("Ada lovelace")
        self.nome.submit()

        self.email = self.driver.find_element_by_id("email")
        self.email.send_keys("123456789")
        self.email.submit()

        self.senha = self.driver.find_element_by_id("password")
        self.senha.send_keys("{Ada123}")
        self.senha.submit()
        self.botao = self.driver.find_element_by_class_name('icon').click()

        self.agreement = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/form/div[4]/div/label/div').click()

        self.submit = self.driver.find_element_by_class_name('btn.btn-primary.btn-base').click()
        time.sleep(10)
        self.url = self.driver.current_url
        #print("Url do teste 4 :" + self.url)
        self.assertEqual(self.url,"https://staging.app.betrybe.com/registration")

    #teste de email feito de uma string sem o padrao de email
    def test_5(self):
        self.nome = self.driver.find_element_by_id("name")
        self.nome.send_keys("Ada lovelace")
        self.nome.submit()

        self.email = self.driver.find_element_by_id("email")
        self.email.send_keys("meuemail")
        self.email.submit()

        self.senha = self.driver.find_element_by_id("password")
        self.senha.send_keys("{Ada123}")
        self.senha.submit()
        self.botao = self.driver.find_element_by_class_name('icon').click()

        self.agreement = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/form/div[4]/div/label/div').click()

        self.submit = self.driver.find_element_by_class_name('btn.btn-primary.btn-base').click()
        time.sleep(10)
        self.url = self.driver.current_url
        #print("Url do teste 5 :" + self.url)
        self.assertEqual(self.url,"https://staging.app.betrybe.com/registration")

    #teste do email feito sem a primeira parte do padrao de email
    def test_6(self):
        self.nome = self.driver.find_element_by_id("name")
        self.nome.send_keys("Ada lovelace")
        self.nome.submit()

        self.email = self.driver.find_element_by_id("email")
        self.email.send_keys("@exemple.com")
        self.email.submit()

        self.senha = self.driver.find_element_by_id("password")
        self.senha.send_keys("{Ada123}")
        self.senha.submit()
        self.botao = self.driver.find_element_by_class_name('icon').click()

        self.agreement = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/form/div[4]/div/label/div').click()

        self.submit = self.driver.find_element_by_class_name('btn.btn-primary.btn-base').click()
        time.sleep(10)
        self.url = self.driver.current_url
        #print("Url do teste 6 :" + self.url)
        self.assertEqual(self.url,"https://staging.app.betrybe.com/registration")

    #teste do email feito sem a segunda parte de email
    def test_7(self):
        self.nome = self.driver.find_element_by_id("name")
        self.nome.send_keys("Ada lovelace")
        self.nome.submit()

        self.email = self.driver.find_element_by_id("email")
        self.email.send_keys("ada@")
        self.email.submit()

        self.senha = self.driver.find_element_by_id("password")
        self.senha.send_keys("{Ada123}")
        self.senha.submit()
        self.botao = self.driver.find_element_by_class_name('icon').click()

        self.agreement = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/form/div[4]/div/label/div').click()

        self.submit = self.driver.find_element_by_class_name('btn.btn-primary.btn-base').click()
        time.sleep(10)
        self.url = self.driver.current_url
        #print("Url do teste 7 :" + self.url)
        self.assertEqual(self.url,"https://staging.app.betrybe.com/registration")

    #teste de email com espaco em branco na primeira parte do padrao de email
    def test_8(self):
        self.nome = self.driver.find_element_by_id("name")
        self.nome.send_keys("Ada lovelace")
        self.nome.submit()

        self.email = self.driver.find_element_by_id("email")
        self.email.send_keys("ada lovelace@exemple.com")
        self.email.submit()

        self.senha = self.driver.find_element_by_id("password")
        self.senha.send_keys("{Ada123}")
        self.senha.submit()
        self.botao = self.driver.find_element_by_class_name('icon').click()

        self.agreement = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/form/div[4]/div/label/div').click()

        self.submit = self.driver.find_element_by_class_name('btn.btn-primary.btn-base').click()
        time.sleep(10)
        self.url = self.driver.current_url
        #print("Url do teste 8 :" + self.url)
        self.assertEqual(self.url,"https://staging.app.betrybe.com/registration")

    #teste de email com espaco em branco na segunda parte do padrao de email
    def test_9(self):
        self.nome = self.driver.find_element_by_id("name")
        self.nome.send_keys("Ada lovelace")
        self.nome.submit()

        self.email = self.driver.find_element_by_id("email")
        self.email.send_keys("adalovelace@exe mple.com")
        self.email.submit()

        self.senha = self.driver.find_element_by_id("password")
        self.senha.send_keys("{Ada123}")
        self.senha.submit()
        self.botao = self.driver.find_element_by_class_name('icon').click()

        self.agreement = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/form/div[4]/div/label/div').click()

        self.submit = self.driver.find_element_by_class_name('btn.btn-primary.btn-base').click()
        time.sleep(10)
        self.url = self.driver.current_url
        #print("Url do teste 9 :" + self.url)
        self.assertEqual(self.url,"https://staging.app.betrybe.com/registration")

    #teste de email sem o ponto na segunda parte
    def test_10(self):
        self.nome = self.driver.find_element_by_id("name")
        self.nome.send_keys("Ada lovelace")
        self.nome.submit()

        self.email = self.driver.find_element_by_id("email")
        self.email.send_keys("adalovelace@exemplecom")
        self.email.submit()

        self.senha = self.driver.find_element_by_id("password")
        self.senha.send_keys("{Ada123}")
        self.senha.submit()
        self.botao = self.driver.find_element_by_class_name('icon').click()

        self.agreement = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/form/div[4]/div/label/div').click()

        self.submit = self.driver.find_element_by_class_name('btn.btn-primary.btn-base').click()
        time.sleep(10)
        self.url = self.driver.current_url
        #print("Url do teste 10 :" + self.url)
        self.assertEqual(self.url,"https://staging.app.betrybe.com/registration")


    #encerando a sessao
    def tearDown(self):
        self.driver.close()