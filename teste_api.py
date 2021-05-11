import unittest
import requests

class RestApiTest(unittest.TestCase):
    def setUp(self):
        pass
        self.APIUrl = "http://api.dataatwork.org/v1//jobs/autocomplete"

    #teste api com requisicao correta, begins_with é o parametro
    def teste_api_1(self):
        url = self.APIUrl + "?begins_with=soft"
        response = requests.get(url)
        self.assertEqual(response.status_code,200)
    
    #teste api com requisicao correta, contains é o parametro
    def teste_api_2(self):
        url = self.APIUrl + "?contains=soft"
        response = requests.get(url)
        self.assertEqual(response.status_code,200)

    #teste api com requisicao correta, ends_with é o parametro
    def teste_api_3(self):
        url = self.APIUrl + "?ends_with=soft"
        response = requests.get(url)
        self.assertEqual(response.status_code,404)


    #teste api com requisicao sem especificar os parametros
    def teste_api_4(self):
        response = requests.get(self.APIUrl)
        self.assertEqual(response.status_code,400)
    
    #teste api com um job que nao existe na api
    def teste_api_5(self):
        url = self.APIUrl + "?begins_with=porteiro"
        response = requests.get(url)
        self.assertEqual(response.status_code,404)



    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()