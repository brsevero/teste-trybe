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

class TesteBotao(unittest.TestCase):

    #criando uma sessao do chrome
    def setUp(self):
        self.driver = webdriver.Chrome(options=set_chrome_options())
        self.driver.get("https://staging.app.betrybe.com/registration")

    #teste criar conta sem marcar os termos de uso
    def test_16(self):
        self.nome = self.driver.find_element_by_id("name")
        self.nome.send_keys("Ada lovelace")
        self.nome.submit()

        self.email = self.driver.find_element_by_id("email")
        self.email.send_keys("adalovelace@exemple.com")
        self.email.submit()

        self.senha = self.driver.find_element_by_id("password")
        self.senha.send_keys("AbAb!@12")
        self.senha.submit()

        self.botao = self.driver.find_element_by_class_name('icon').click()

        self.submit = self.driver.find_element_by_class_name('btn.btn-primary.btn-base').click()
        time.sleep(10)
        self.url = self.driver.current_url
        #print("Url do teste 16 :" + self.url)
        self.assertEqual(self.url,"https://staging.app.betrybe.com/registration")

    #testando o link ao clicar na logo
    def test_17(self):
        self.simbol = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div[1]/a').click()
        time.sleep(10)
        self.url = self.driver.current_url
        #print("Url do teste 17 :" + self.url)
        self.assertEqual(self.url,"https://staging.app.betrybe.com/login")


    #testando o link no clique aqui
    def test_18(self):
        self.conta_antiga = self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div/div[2]/div/div/p/a").click()
        time.sleep(10)
        self.url = self.driver.current_url
        #print("Url do teste 18 :" + self.url)
        self.assertEqual(self.url,"https://staging.app.betrybe.com/login")
    
    #encerando a sessao
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()