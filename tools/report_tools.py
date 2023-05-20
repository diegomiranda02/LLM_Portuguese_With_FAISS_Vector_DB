from interfaces.toolInterfaces import ToolInterface

class ToolWhoCreateDocumentOfTCUReport(ToolInterface):

  name = 'Ferramenta para criar um relatorio do TCU' # Class variable. Shared among all objects
  description = 'Use essa ferramenta quando for para criar um relatorio do TCU' # Class variable. Shared among all objects

  def __call__(self):
    print('called')

  def __init__(self, command: str) -> None:
    self.__command = command

  def run(self) -> str:
    if self.__verify_command_type(self.__command):

      self.__who_is_the_person()
      self.__search_the_person_id_via_API()
      self.__create_the_document_using_the_person_data()

      return 'Result of the command {}'.format(self.__command)
    else:
      return 'Error executing command {}'.format(self.__command) # How to concatenate with a string + 'The command must be a string'

  def which_year(self) -> str:
   return 'Qual o ano?'

  def __search_the_person_id_via_API(self) -> None:
    print('searching the person ID via API')

  def __create_the_document_using_the_person_data(self) -> None:
    print('creating the document using the person data')

  def __verify_command_type(self, command: str) -> bool:
    if isinstance(command, str):
      return True
    else:
      return False
    

class ToolWhoCreateWorkReportHistory(ToolInterface):

  name = 'Ferramenta para criar um relatorio funcional do servidor' # Class variable. Shared among all objects
  description = 'Use essa ferramenta quando for para criar um relatorio funcional do servidor' # Class variable. Shared among all objects

  def __call__(self):
    print('called')

  def __init__(self, command: str) -> None:
    self.__command = command

  def run(self) -> str:
    if self.__verify_command_type(self.__command):

      self.__who_is_the_person()
      self.__search_the_person_id_via_API()
      self.__create_the_document_using_the_person_data()

      return 'Result of the command {}'.format(self.__command)
    else:
      return 'Error executing command {}'.format(self.__command) # How to concatenate with a string + 'The command must be a string'

  def who_is_the_person(self) -> str:
    return 'Para qual servidor?'

  def which_matricula(self) -> None:
    return 'Qual a matricula?'

  def __create_the_document_using_the_person_data(self) -> None:
    print('creating the document using the person data')

  def __verify_command_type(self, command: str) -> bool:
    if isinstance(command, str):
      return True
    else:
      return False