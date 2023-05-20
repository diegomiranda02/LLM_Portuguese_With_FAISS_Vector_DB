from abc import ABC, abstractmethod

class ToolInterface(ABC):

  @abstractmethod
  def run(self, command: str) -> str:
    pass

  @abstractmethod
  def requirements_to_use(self) -> str:
    pass