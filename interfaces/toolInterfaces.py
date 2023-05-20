from abc import ABC, abstractmethod

class ToolInterface(ABC):

  @abstractmethod
  def run(self, command: str) -> str:
    pass