from typing import Type
from interfaces.toolInterfaces import ToolInterface
from models.LLM_model_api import LLM_MODEL

class ToolFactory:

    def __init__(self):
        self._tools = {}
        self.__llm_model = LLM_MODEL()

    def register_tool(self, description: str, tool: Type[ToolInterface]) -> None:
        self._tools[description] = tool

    def get_tool(self, command: str):
        tool_description = self.__llm_model.getAnswer(command, 4)
        return self._tools.get(tool_description)
    
    def get_tools_description_list(self):
        return list(self._tools.keys())
    
    def generate_tools_vector_database(self):
        print('TOOL FACTORY ENCONDING DATA')
        self.__llm_model.encodeData(self.get_tools_description_list())
        print('TOOL FACTORY ENCONDING DATA FINISHED')