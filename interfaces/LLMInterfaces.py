from abc import ABC, abstractmethod

class LLMInterface(ABC):

  @abstractmethod
  def answer(self, command: str) -> str:
    pass