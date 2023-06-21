from interfaces.toolInterfaces import ToolInterface
from typing import Dict

import json

class ToolWhoCreateDocumentOfTCUReport(ToolInterface):

  name = 'Ferramenta para criar um relatorio do TCU' # Class variable. Shared among all objects
  description = 'Use essa ferramenta quando for para criar um relatorio do TCU' # Class variable. Shared among all objects

  def run(self, requirements: Dict[str, str]) -> str:
    print(requirements)

    # a Python object (dict):
    x = {
      "title": "Relatório de Gestão 2022",
      "subtitle": "SECRETARIA DE GESTÃO DE PESSOAS - COPAG",
      "tableDescription1": "Detalhamento da despesa de pessoal (ativo, inativo e pensionista), evolução dos últimos anos e justificativa para o aumento/diminuição:",
      "tableContentDescription1" : "Membros de poder e agentes políticos",
      "table1" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "tableContentDescription2" : "Servidores de Carreira vinculados ao órgão da unidade jurisdicionada",
      "table2" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "tableContentDescription3" : "Servidores de Carreira sem Vínculo com o órgão da unidade jurisdicionada",
      "table3" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "tableContentDescription4" : "Servidores sem vínculo com a administração pública (exceto temporários)",
      "table4" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "tableContentDescription5" : "Servidores Cedidos com ônus",
      "table5" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "tableContentDescription6" : "Servidores com contrato temporário",
      "table6" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "observation": "Justificativa variação: as despesas de 2022 superaram as despesas de 2021 por ter sido um ano eleitoral em que são pagas horas extras, jetons extraordinários e gratificação de juízes e de procuradores auxiliares. Além disso, houve reestruturação interna do Tribunal, com a criação de novos cargos em comissão (Resolução TRE-RS n. 390/2022), que contribuíram para aumentar a despesa.",
      "table200" : 
          [
         { "CARGOS GERENCIAIS": "CJ4", "QUANTIDADE DE CARGOS GERENCIAIS": 1 ,"PERCENTUAL OCUPADO POR SERVIDORES EFETIVOS": "100,00%"},
         { "CARGOS GERENCIAIS": "CJ3", "QUANTIDADE DE CARGOS GERENCIAIS": 8 ,"PERCENTUAL OCUPADO POR SERVIDORES EFETIVOS": "100,00%"},
         { "CARGOS GERENCIAIS": "CJ2", "QUANTIDADE DE CARGOS GERENCIAIS": 34 ,"PERCENTUAL OCUPADO POR SERVIDORES EFETIVOS": "97,14% (34 efetivos e 1 comissionado)"},
         { "CARGOS GERENCIAIS": "CJ1", "QUANTIDADE DE CARGOS GERENCIAIS": 16 ,"PERCENTUAL OCUPADO POR SERVIDORES EFETIVOS": "95,00% [19 efetivos (16 gerenciais, 3, não) e 1 comissionado]"},
         { "CARGOS GERENCIAIS": "FC6", "QUANTIDADE DE CARGOS GERENCIAIS": 224 ,"PERCENTUAL OCUPADO POR SERVIDORES EFETIVOS": "97,82% (224 efetivos, 4 removidos e 1 vago)"}
         ],
    }

    # convert into JSON:
    y = json.dumps(x)
    return y
    
  def requirements_to_use(self) -> str:
    # Requirements to use the tool
    requirements = ['Qual relatorio?', 'Qual o ano?']

    return requirements
    

class ToolWhoCreateWorkReportHistory(ToolInterface):

  name = 'Ferramenta para criar um relatorio funcional do servidor' # Class variable. Shared among all objects
  description = 'Use essa ferramenta quando for para criar um relatorio funcional do servidor' # Class variable. Shared among all objects

  def run(self, requirements: Dict[str, str]) -> str:
    print(requirements)

    # a Python object (dict):
    x = {
      "text": "A ficha funcional é o documento eletrônico que demonstra todas as ocorrências funcionais já registradas: investidura, movimentação e vacância de cargos e funções, averbação de tempo de serviço, auxílios, benefícios, dependentes, descontos, faltas, folgas e licenças, gratificações, substituições e vantagens pessoais."
    }

    # convert into JSON:
    y = json.dumps(x)
    return y
    
  def requirements_to_use(self) -> str:
    # Requirements to use the tool
    requirements = ['Qual o tipo de relatorio?', 'Para qual servidor?', 'Qual a matricula?']
    return requirements
  
    
class ToolWhoCreateFinancialReport(ToolInterface):

  name = 'Ferramenta para criar um relatorio financeiro' # Class variable. Shared among all objects
  description = 'Use essa ferramenta quando for para criar um relatorio financeiro' # Class variable. Shared among all objects

  # Requirements 
  WHICH_REPORT = 'Qual relatorio?'
  WHICH_MONTH = 'Em que mes?'
  WHICH_YEAR = 'Qual ano?'

  # System URL
  SYSTEM_URL = 'http://localhost:8088/report'

  def run(self, requirements: Dict[str, str]) -> str:
    print(requirements)

    print("URL: {}?reportType={}&month={}&year={}".format(self.SYSTEM_URL, 
                           requirements[self.WHICH_REPORT], 
                           requirements[self.WHICH_MONTH], 
                           requirements[self.WHICH_YEAR]
                           ))
    
    return "{}?reportType={}&month={}&year={}".format(self.SYSTEM_URL, 
                           requirements[self.WHICH_REPORT], 
                           requirements[self.WHICH_MONTH], 
                           requirements[self.WHICH_YEAR]
                           )
    
  def requirements_to_use(self) -> str:
    # Requirements to use the tool
    requirements = [self.WHICH_REPORT, self.WHICH_MONTH, self.WHICH_YEAR]
    return requirements
  
class ToolWhichAddNewEmployent(ToolInterface):

  name = 'Ferramenta para cadastrar um novo funcionario' # Class variable. Shared among all objects
  description = 'Use essa ferramenta quando for para cadastrar um novo funcionario' # Class variable. Shared among all objects

  # Requirements 
  EMPLOYEE_NAME = 'Qual o nome do empregado?'
  CPF = 'Qual CPF?'
  RG = 'Qual RG?'
  RG_ISSUANCE_DATE = "Quando foi emitida a RG?"
  RG_ISSUER = "Qual foi o emissor da RG?"
  EMPLOYEE_ADDRESS = "Onde a empregado reside?"
  EMPLOYEE_ADDRESS_NUMBER = "Qual o numero da residencia?"
  EMPLOYEE_ADDRESS_COMPLEMENT = "Qual o complemento?"
  EMPLOYEE_APARTMENT_NUMBER = "Qual apartamento?"
  EMPLOYEE_CONDOMINIUM = "Qual condominio?"
  EMPLOYEE_CEP = "Qual CEP?"
  EMPLOYEE_NEIGHBORHOOD = "Qual bairro?"
  EMPLOYEE_STATE = "Em qual estado?"
  EMPLOYEE_SALARY = "Qual o salario?"
  EMPLOYEE_WORKLOAD = "Qual a carga horaria?"
  EMPLOYEE_HOUR_A_DAY = "Quantas horas por dia?"
  EMPLOYEE_CONTRACT = "Qual o regime de contratacao?"

  # System URL
  SYSTEM_URL = 'http://localhost:8088/addEmployee?'\
                'employee_name={}&'\
                'CPF={}&'\
                'RG={}&'\
                'RG_issuance_date={}&'\
                'RG_issuer={}&'\
                'employee_address={}&'\
                'employee_address_number={}&'\
                'employee_address_complement={}&'\
                'employee_apartment_number={}&'\
                'employee_condominium={}&'\
                'employee_CEP={}&'\
                'employee_neighborhood={}&'\
                'employee_state={}&'\
                'employee_salary={}&'\
                'employee_worload={}&'\
                'employee_hour_a_day={}&'\
                'employee_contract={}'

  def run(self, requirements: Dict[str, str]) -> str:
    print(requirements)

    print("URL: " + self.SYSTEM_URL.format(
                           requirements[self.EMPLOYEE_NAME], 
                           requirements[self.CPF], 
                           requirements[self.RG],
                           requirements[self.RG_ISSUANCE_DATE],
                           requirements[self.RG_ISSUER],
                           requirements[self.EMPLOYEE_ADDRESS],
                           requirements[self.EMPLOYEE_ADDRESS_NUMBER],
                           requirements[self.EMPLOYEE_ADDRESS_COMPLEMENT],
                           requirements[self.EMPLOYEE_APARTMENT_NUMBER],
                           requirements[self.EMPLOYEE_CONDOMINIUM],
                           requirements[self.EMPLOYEE_CEP],
                           requirements[self.EMPLOYEE_NEIGHBORHOOD],
                           requirements[self.EMPLOYEE_STATE],
                           requirements[self.EMPLOYEE_SALARY],
                           requirements[self.EMPLOYEE_WORKLOAD],
                           requirements[self.EMPLOYEE_HOUR_A_DAY],
                           requirements[self.EMPLOYEE_CONTRACT]
                           ))
    
    return self.SYSTEM_URL.format(
                           requirements[self.EMPLOYEE_NAME], 
                           requirements[self.CPF], 
                           requirements[self.RG],
                           requirements[self.RG_ISSUANCE_DATE],
                           requirements[self.RG_ISSUER],
                           requirements[self.EMPLOYEE_ADDRESS],
                           requirements[self.EMPLOYEE_ADDRESS_NUMBER],
                           requirements[self.EMPLOYEE_ADDRESS_COMPLEMENT],
                           requirements[self.EMPLOYEE_APARTMENT_NUMBER],
                           requirements[self.EMPLOYEE_CONDOMINIUM],
                           requirements[self.EMPLOYEE_CEP],
                           requirements[self.EMPLOYEE_NEIGHBORHOOD],
                           requirements[self.EMPLOYEE_STATE],
                           requirements[self.EMPLOYEE_SALARY],
                           requirements[self.EMPLOYEE_WORKLOAD],
                           requirements[self.EMPLOYEE_HOUR_A_DAY],
                           requirements[self.EMPLOYEE_CONTRACT]
                           )
    
  def requirements_to_use(self) -> str:
    # Requirements to use the tool
    requirements = [self.EMPLOYEE_NAME, self.CPF, self.RG, self.RG_ISSUANCE_DATE, self.RG_ISSUER, self.EMPLOYEE_ADDRESS, self.EMPLOYEE_ADDRESS_NUMBER, 
                    self.EMPLOYEE_ADDRESS_COMPLEMENT, self.EMPLOYEE_APARTMENT_NUMBER, self.EMPLOYEE_CONDOMINIUM, self.EMPLOYEE_CEP, self.EMPLOYEE_NEIGHBORHOOD, 
                    self.EMPLOYEE_STATE, self.EMPLOYEE_SALARY, self.EMPLOYEE_WORKLOAD, self.EMPLOYEE_HOUR_A_DAY, self.EMPLOYEE_CONTRACT]
    return requirements


class ToolWhichCreatesAReportOfTheMostSoldProducts(ToolInterface):

  name = 'Ferramenta para criar um relatorio dos produtos mais vendidos' # Class variable. Shared among all objects
  description = 'Use essa ferramenta quando for para criar um relatorio dos produtos mais vendidos' # Class variable. Shared among all objects

  def run(self, requirements: Dict[str, str]) -> str:
    print(requirements)
    
    # a Python object (dict):
    x = {
      "text": "Principais Produtos Vendidos",
      "products" : 
          [
         { "Produtos": "Queijo de coalho", "1o Trimestre": 22000.00, "2o Trimestre": 10000.00, "3o Trimestre": 15000.00, "4o Trimestre": 32000.00, "Total": 79000.00},
         { "Produtos": "Carne", "1o Trimestre": 22000.00, "2o Trimestre": 10000.00, "3o Trimestre": 15000.00, "4o Trimestre": 32000.00, "Total": 79000.00},
         { "Produtos": "Cafe", "1o Trimestre": 22000.00, "2o Trimestre": 10000.00, "3o Trimestre": 15000.00, "4o Trimestre": 32000.00, "Total": 79000.00},
         { "Produtos": "Molho de Pimenta", "1o Trimestre": 22000.00, "2o Trimestre": 10000.00, "3o Trimestre": 15000.00, "4o Trimestre": 32000.00, "Total": 79000.00},
         { "Produtos": "Queijo gorgonzola", "1o Trimestre": 22000.00, "2o Trimestre": 10000.00, "3o Trimestre": 15000.00, "4o Trimestre": 32000.00, "Total": 79000.00},
         { "Produtos": "Geleia", "1o Trimestre": 22000.00, "2o Trimestre": 10000.00, "3o Trimestre": 15000.00, "4o Trimestre": 32000.00, "Total": 79000.00},
         { "Produtos": "Agua Sanitaria", "1o Trimestre": 22000.00, "2o Trimestre": 10000.00, "3o Trimestre": 15000.00, "4o Trimestre": 32000.00, "Total": 79000.00},
         { "Produtos": "Sabao", "1o Trimestre": 22000.00, "2o Trimestre": 10000.00, "3o Trimestre": 15000.00, "4o Trimestre": 32000.00, "Total": 79000.00},
         { "Produtos": "Suco", "1o Trimestre": 22000.00, "2o Trimestre": 10000.00, "3o Trimestre": 15000.00, "4o Trimestre": 32000.00, "Total": 79000.00},
         { "Produtos": "Legumes", "1o Trimestre": 22000.00, "2o Trimestre": 10000.00, "3o Trimestre": 15000.00, "4o Trimestre": 32000.00, "Total": 79000.00}
         ]
    }

    # convert into JSON:
    y = json.dumps(x)
    return y
    
  def requirements_to_use(self) -> str:
    # Requirements to use the tool
    requirements = ['Qual relatorio?', 'Quais produtos?', 'Listar quantos produtos mais vendidos?', 'Ordenado por qual campo?']
    return requirements
  

class ToolWhichCreatesAFinancialReportComparingYearOverYear(ToolInterface):

  name = 'Ferramenta para criar um relatorio financeiro comparando ano a ano' # Class variable. Shared among all objects
  description = 'Use essa ferramenta quando for para criar um relatorio financeiro comparando ano a ano' # Class variable. Shared among all objects

  def run(self, requirements: Dict[str, str]) -> str:
    print(requirements)

    # a Python object (dict):
    x = {
      "title": "Relatório de Gestão 2022",
      "subtitle": "SECRETARIA DE GESTÃO DE PESSOAS - COPAG",
      "tableDescription1": "Detalhamento da despesa de pessoal (ativo, inativo e pensionista), evolução dos últimos anos e justificativa para o aumento/diminuição:",
      "tableContentDescription1" : "Despesas Financeiras",
      "table1" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "tableContentDescription2" : "Despesas com Pessoal",
      "table2" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "tableContentDescription3" : "Receita de Vendas dos Produtos",
      "table3" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "tableContentDescription4" : "Receita de Vendas dos Servicos",
      "table4" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "tableContentDescription5" : "Receita de Vendas de Cursos (incluindo cursos in company)",
      "table5" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "tableContentDescription6" : "Despesas de Juros/Multas",
      "table6" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "observation": "Justificativa variação: as despesas de 2022 superaram as despesas de 2021 por ter sido um ano eleitoral em que são pagas horas extras, jetons extraordinários e gratificação de juízes e de procuradores auxiliares. Além disso, houve reestruturação interna do Tribunal, com a criação de novos cargos em comissão (Resolução TRE-RS n. 390/2022), que contribuíram para aumentar a despesa.",
      "table200" : 
          [
         { "CARGOS GERENCIAIS": "CJ4", "QUANTIDADE DE CARGOS GERENCIAIS": 1 ,"PERCENTUAL OCUPADO POR SERVIDORES EFETIVOS": "100,00%"},
         { "CARGOS GERENCIAIS": "CJ3", "QUANTIDADE DE CARGOS GERENCIAIS": 8 ,"PERCENTUAL OCUPADO POR SERVIDORES EFETIVOS": "100,00%"},
         { "CARGOS GERENCIAIS": "CJ2", "QUANTIDADE DE CARGOS GERENCIAIS": 34 ,"PERCENTUAL OCUPADO POR SERVIDORES EFETIVOS": "97,14% (34 efetivos e 1 comissionado)"},
         { "CARGOS GERENCIAIS": "CJ1", "QUANTIDADE DE CARGOS GERENCIAIS": 16 ,"PERCENTUAL OCUPADO POR SERVIDORES EFETIVOS": "95,00% [19 efetivos (16 gerenciais, 3, não) e 1 comissionado]"},
         { "CARGOS GERENCIAIS": "FC6", "QUANTIDADE DE CARGOS GERENCIAIS": 224 ,"PERCENTUAL OCUPADO POR SERVIDORES EFETIVOS": "97,82% (224 efetivos, 4 removidos e 1 vago)"}
         ],
    }

    # convert into JSON:
    y = json.dumps(x)
    return y
    
  def requirements_to_use(self) -> str:
    # Requirements to use the tool
    requirements = ['Qual relatorio?', 'Qual o ano?']

    return requirements
