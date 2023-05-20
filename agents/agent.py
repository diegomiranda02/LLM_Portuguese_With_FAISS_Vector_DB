# Import NLP API
from models import LLM_model_api
from typing import Type

class Agent:

  def __init__(self):
    self.__tool_to_execute = None

  def chooseTool(self, command: str) -> None:
    print('Tool Chosen')
    self.__tool_to_execute = Tool('Tool Chosen')
    print('Execute')
    self.executeCommand(command)
    print('End')

  def executeCommand(self, command: str) -> None:
    print('LLM Chosen')
    LLM_model_api.getAnswer(command)
    print('Tool to execute')
    self.__tool_to_execute.run()