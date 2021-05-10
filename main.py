import unittest
from teste_padrao import TestePadrao
from teste_nome import TesteNome
from teste_email import TesteEmail
from teste_senha import TesteSenha
from teste_botao import TesteBotao
from teste_api import RestApiTest

#pegando todos os testes e criando uma instancia
padrao = unittest.TestLoader().loadTestsFromTestCase(TestePadrao)
nome = unittest.TestLoader().loadTestsFromTestCase(TesteNome)
email = unittest.TestLoader().loadTestsFromTestCase(TesteEmail)
senha = unittest.TestLoader().loadTestsFromTestCase(TesteSenha)
botao = unittest.TestLoader().loadTestsFromTestCase(TesteBotao)
api = unittest.TestLoader().loadTestsFromTestCase(RestApiTest)

#criando um test suite combinando os testes
teste_suite = unittest.TestSuite([padrao, nome, email, senha, botao, api])

#rodando os testes combinados
unittest.TextTestRunner(verbosity=2).run(teste_suite)
