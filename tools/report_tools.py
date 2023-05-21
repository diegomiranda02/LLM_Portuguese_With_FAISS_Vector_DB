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
      "name": "Teste",
      "age": 30,
      "city": "New York"
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
      "name": "Teste",
      "age": 30,
      "city": "New York"
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
      "name": "Teste",
      "age": 30,
      "city": "New York"
    }

    # convert into JSON:
    y = json.dumps(x)
    return y
    
  def requirements_to_use(self) -> str:
    # Requirements to use the tool
    requirements = ['Qual relatorio?', 'Em que mes?', 'Qual ano?']
    return requirements