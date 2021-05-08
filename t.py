import unittest
import json
import urllib
import urllib.request

class RestApiTest(unittest.TestCase):
    def setUp(self):
        #define API url and API key
        self.APIUrl = "http://api.dataatwork.org/v1/jobs/autocomplete"
        self.particula = "software"

    def teste_jobs_autocomplete(self):
        #define api response
        testurl = (self.APIUrl + "?begins_with=" + self.particula)
        #print (testurl)
        response = urllib.request.urlopen(testurl)

        #read response
        html = response.read()

        #print response
        #print(html)

        #read as json data
        json_data = json.loads(html)
        print(json_data)

    def tearDown(self):
        print("rodou")

if __name__ == "__main__":
    unittest.main()
