from abc import ABC, abstractmethod
from typing import Dict

class ToolInterface(ABC):

  @abstractmethod
  def run(self, requirements: Dict[str, str]) -> str:
    pass

  @abstractmethod
  def requirements_to_use(self) -> str:
    pass