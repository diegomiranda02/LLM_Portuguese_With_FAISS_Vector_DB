# Import NLP API
from models import LLM_model_api
from typing import Type
from interfaces.toolInterfaces import ToolInterface

from models import BERT_portuguese_model_api as LLM_BERT

# import urllib library
from urllib.request import urlopen

# Import json package to load json from the URL response
import json

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

    #return self.__tool.run(fulfilled_requirements)

    url = self.__tool.run(fulfilled_requirements)

    print("AGENT ACCESSING URL: {}".format(url))

    # store the response of URL
    response = urlopen(url)
  
    # storing the JSON response from url in data
    data_json = json.loads(response.read())
  
    # Return the json response
    return data_json