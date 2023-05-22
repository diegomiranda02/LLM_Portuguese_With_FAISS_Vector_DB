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

  def run(self, requirements: Dict[str, str]) -> str:
    print(requirements)
    
    # a Python object (dict):
    x = {
      "text": "A ficha funcional é o documento eletrônico que demonstra todas as ocorrências funcionais já registradas: investidura, movimentação e vacância de cargos e funções, averbação de tempo de serviço, auxílios, benefícios, dependentes, descontos, faltas, folgas e licenças, gratificações, substituições e vantagens pessoais.",
      "age": 30,
      "city": "New York",
      "technologies" : 
          [
         { "Courses": "Spark", "Fee": 22000,"Duration":"40Days"},
         { "Courses": "PySpark","Fee": 25000,"Duration":"60Days"},
         { "Courses": "Hadoop", "Fee": 23000,"Duration":"50Days"}
         ]
    }

    # convert into JSON:
    y = json.dumps(x)
    return y
    
  def requirements_to_use(self) -> str:
    # Requirements to use the tool
    requirements = ['Qual relatorio?', 'Em que mes?', 'Qual ano?']
    return requirements