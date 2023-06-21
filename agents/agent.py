# Import NLP API
from models import LLM_model_api
from typing import Type
from interfaces.toolInterfaces import ToolInterface

from models import BERT_portuguese_model_api as LLM_BERT

# import requests library
import requests

class Agent:

  def __init__(self, tool: Type[ToolInterface]):
    self.__tool = tool

  def executeCommand(self, command: str) -> str:
    # Getting the requirements to execute the tool
    requirements_to_use = self.__tool.requirements_to_use()

    # Fulfilling the requirements to use the tool
    fulfilled_requirements = {}
    for requirement in requirements_to_use:
      # Fulfilling each requirements questioning to the LLM
      fulfilled_requirements[requirement] = LLM_BERT.getAnswer(command, requirement)

    url = self.__tool.run(fulfilled_requirements)

    # store the response of URL
    response = requests.get(url)
    print(response.json())
  
    # Return the json response
    return response.json()
