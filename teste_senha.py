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

class TesteSenha(unittest.TestCase):

    #criando uma sessao do chrome
    def setUp(self):
        self.driver = webdriver.Chrome(options=set_chrome_options())

        #navegando ate o site e esperando o carregamento
        self.driver.get("https://staging.app.betrybe.com/registration")

    #teste senha sem o tamanho minimo
    def test_11(self):
        self.nome = self.driver.find_element_by_id("name")
        self.nome.send_keys("Ada lovelace")
        self.nome.submit()

        self.email = self.driver.find_element_by_id("email")
        self.email.send_keys("adalovelace@exemple.com")
        self.email.submit()

        self.senha = self.driver.find_element_by_id("password")
        self.senha.send_keys("Ab1!")
        self.senha.submit()
        self.botao = self.driver.find_element_by_class_name('icon').click()

        self.agreement = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/form/div[4]/div/label/div').click()

        self.submit = self.driver.find_element_by_class_name('btn.btn-primary.btn-base').click()
        time.sleep(10)
        self.url = self.driver.current_url
        #print("Url do teste 11 :" + self.url)
        self.assertEqual(self.url,"https://staging.app.betrybe.com/registration")

    #teste senha sem letra mauscula
    def test_12(self):
        self.nome = self.driver.find_element_by_id("name")
        self.nome.send_keys("Ada lovelace")
        self.nome.submit()

        self.email = self.driver.find_element_by_id("email")
        self.email.send_keys("adalove@lolace.com")
        self.email.submit()

        self.senha = self.driver.find_element_by_id("password")
        self.senha.send_keys("ab1!1234")
        self.senha.submit()
        self.botao = self.driver.find_element_by_class_name('icon').click()

        self.agreement = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/form/div[4]/div/label/div').click()

        self.submit = self.driver.find_element_by_class_name('btn.btn-primary.btn-base').click()
        time.sleep(10)
        self.url = self.driver.current_url
        #print("Url do teste 12 :" + self.url)
        self.assertEqual(self.url,"https://staging.app.betrybe.com/registration")

    #teste de senha sem letra minuscula
    def test_13(self):
        self.nome = self.driver.find_element_by_id("name")
        self.nome.send_keys("Ada lovelace")
        self.nome.submit()

        self.email = self.driver.find_element_by_id("email")
        self.email.send_keys("adalovelace@exemple.com")
        self.email.submit()

        self.senha = self.driver.find_element_by_id("password")
        self.senha.send_keys("AB1!1234")
        self.senha.submit()
        self.botao = self.driver.find_element_by_class_name('icon').click()

        self.agreement = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/form/div[4]/div/label/div').click()

        self.submit = self.driver.find_element_by_class_name('btn.btn-primary.btn-base').click()
        time.sleep(10)
        self.url = self.driver.current_url
        #print("Url do teste 13 :" + self.url)
        self.assertEqual(self.url,"https://staging.app.betrybe.com/registration")
    #teste senha sem numeros
    def test_14(self):
        self.nome = self.driver.find_element_by_id("name")
        self.nome.send_keys("Ada lovelace")
        self.nome.submit()

        self.email = self.driver.find_element_by_id("email")
        self.email.send_keys("adalovelace@exemple.com")
        self.email.submit()

        self.senha = self.driver.find_element_by_id("password")
        self.senha.send_keys("Ab!@#$%&")
        self.senha.submit()
        self.botao = self.driver.find_element_by_class_name('icon').click()

        self.agreement = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/form/div[4]/div/label/div').click()

        self.submit = self.driver.find_element_by_class_name('btn.btn-primary.btn-base').click()
        time.sleep(10)
        self.url = self.driver.current_url
        #print("Url do teste 14 :" + self.url)
        self.assertEqual(self.url,"https://staging.app.betrybe.com/registration")

    #teste senha sem caracteres especiais
    def test_15(self):
        self.nome = self.driver.find_element_by_id("name")
        self.nome.send_keys("Ada lovelace")
        self.nome.submit()

        self.email = self.driver.find_element_by_id("email")
        self.email.send_keys("adalovelace@exemple.com")
        self.email.submit()

        self.senha = self.driver.find_element_by_id("password")
        self.senha.send_keys("AbAbAB12")
        self.senha.submit()
        self.botao = self.driver.find_element_by_class_name('icon').click()

        self.agreement = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/form/div[4]/div/label/div').click()

        self.submit = self.driver.find_element_by_class_name('btn.btn-primary.btn-base').click()
        time.sleep(10)
        self.url = self.driver.current_url
        #print("Url do teste 15 :" + self.url)
        self.assertEqual(self.url,"https://staging.app.betrybe.com/registration")

    #encerando a sessao
    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()