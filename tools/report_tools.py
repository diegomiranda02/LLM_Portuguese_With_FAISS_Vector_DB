from interfaces.toolInterfaces import ToolInterface

class ToolWhoCreateDocumentOfTCUReport(ToolInterface):

  name = 'Ferramenta para criar um relatorio do TCU' # Class variable. Shared among all objects
  description = 'Use essa ferramenta quando for para criar um relatorio do TCU' # Class variable. Shared among all objects

  def run(self) -> str:
    return ''
    
  def requirements_to_use(self) -> str:
    # Requirements to use the tool
    requirements = ['Qual relatorio?', 'Qual o ano?']

    return requirements
    

class ToolWhoCreateWorkReportHistory(ToolInterface):

  name = 'Ferramenta para criar um relatorio funcional do servidor' # Class variable. Shared among all objects
  description = 'Use essa ferramenta quando for para criar um relatorio funcional do servidor' # Class variable. Shared among all objects

  def run(self) -> str:
    return ''
    
  def requirements_to_use(self) -> str:

    # Requirements to use the tool
    requirements = ['Qual o tipo de relatorio?', 'Para qual servidor?', 'Qual a matricula?']
    return requirements
  
    
class ToolWhoCreateFinancialReport(ToolInterface):

  name = 'Ferramenta para criar um relatorio financeiro' # Class variable. Shared among all objects
  description = 'Use essa ferramenta quando for para criar um relatorio financeiro' # Class variable. Shared among all objects

  def run(self) -> str:
    return ''
    
  def requirements_to_use(self) -> str:
    # Requirements to use the tool
    requirements = ['Qual relatorio?', 'Em que mes?', 'Qual ano?']
    return requirements